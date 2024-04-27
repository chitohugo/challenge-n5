from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from traffic_violations.models import Infraction, Vehicle, User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data


class VehicleSerializer(serializers.ModelSerializer):
    make = serializers.SlugRelatedField(slug_field='name', read_only=True)
    owner = serializers.SlugRelatedField(slug_field='full_name', read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'patent', 'color', 'make', 'owner']


class InfractionSerializer(serializers.ModelSerializer):
    patent = serializers.CharField(write_only=True)
    vehicle = VehicleSerializer(source='patent', read_only=True)

    class Meta:
        model = Infraction
        fields = ['id', 'vehicle', 'patent', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at', 'vehicle']
