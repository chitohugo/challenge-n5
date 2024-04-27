from django.http import Http404

from traffic_violations.models import Vehicle, Person, Infraction


class InfractionService:
    """Service class for managing infractions.

    """
    @classmethod
    def upload_infraction(cls, patent):
        """Retrieve a vehicle by its patent.

        Args:
            cls: The class itself.
            patent (str): The patent of the vehicle to retrieve.

        Returns:
            Vehicle: The vehicle object with the specified patent.

        Raises:
            Http404: If the vehicle with the given patent does not exist.
        """
        try:
            return Vehicle.objects.get(patent=patent)
        except Vehicle.DoesNotExist:
            raise Http404(f"Not found: {patent}")

    @classmethod
    def generate_inform(cls, email):
        """Generate infraction report for a person by their email.

        Args:
            cls: The class itself.
            email (str): The email of the person to generate the report for.

        Returns:
            QuerySet: A queryset containing all infractions related to the person with the specified email.

        Raises:
            Http404: If the person with the given email does not exist.
        """
        try:
            instance = Person.objects.get(email=email)
            infractions = Infraction.objects.filter(patent__owner_id=instance.id)
            return infractions
        except Person.DoesNotExist:
            raise Http404(f"Not found: {email}")
