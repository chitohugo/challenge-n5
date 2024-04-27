from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from common.base_view import BaseView
from traffic_violations.models import Infraction, User, PoliceOfficer
from traffic_violations.serializers import InfractionSerializer, RegisterSerializer
from traffic_violations.services import InfractionService


class RegisterView(CreateAPIView):
    """View that handles user registrations.

    Note:
        You must send a Json object with the keys described below:
        - first_name (str, required): First Name
        - last_name (str, required): Last Name
        - password (str, required): Password
        - password2 (str, required): Password Confirmation
        - email (str, required): Email
        - username (str, required): Username

    Returns:
        Json object with the entered data.
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        """Perform actions when creating a user.

        Args:
            serializer (Serializer): The serializer instance.

        Returns:
            User: The created user object.
        """
        serializer.validated_data.pop('password2')
        user = User.objects.create(**serializer.validated_data)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(serializer.validated_data['password'])
        user.save()

        return user



class InfractionViewSet(BaseView):
    """A view set for managing infractions.

    Attributes:
        queryset (QuerySet): A queryset containing all infractions.
        serializer_class (Serializer): The serializer class for infractions.
        service (InfractionService): An instance of the infraction service.
    """
    queryset = Infraction.objects.all()
    serializer_class = InfractionSerializer
    service = InfractionService()

    def perform_create(self, serializer):
        """Perform actions when creating an infraction.

        Args:
            serializer (Serializer): The serializer instance.

        Returns:
            None
        """
        current_user = self.request.user
        official = PoliceOfficer.objects.get(user=current_user)
        patent = serializer.validated_data['patent']
        instance = self.service.upload_infraction(patent)
        serializer.save(patent=instance, created_by=official)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'email',
                openapi.IN_QUERY,
                description="Email to generate violation report.",
                type=openapi.TYPE_STRING
            ),
        ]
    )
    @action(detail=False, methods=['get'], url_path='generate-inform', permission_classes=[AllowAny])
    def generate_inform(self, request):
        """Generate an infraction report for a specified email.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The HTTP response containing the infraction report.
        """
        email = request.query_params.get('email', None)
        if email:
            response = self.service.generate_inform(email)
            serializer = InfractionSerializer(response, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
