import pytest
from django.db import IntegrityError

from traffic_violations.models import User, Person, Vehicle, Make, Infraction

object_user = {
    "first_name": "Testing",
    "last_name": "Testing",
    "email": "testing@test.com",
    "password": "Testing",
    "username": "testing"
}


class TestModels:
    """Tests for the models"""

    @pytest.mark.django_db
    def test_user_created_successfully(self, user):
        """Verifies that a user is saved in the database"""
        assert User.objects.filter(username=user.username).exists()

    @pytest.mark.django_db
    def test_username_must_be_unique(self, user):
        """Verifies that the username field is unique"""
        with pytest.raises(IntegrityError):
            User.objects.create(**object_user)

    @pytest.mark.django_db
    def test_person_created_successfully(self, person):
        """Verifies that a person is saved in the database"""
        assert Person.objects.filter(dni=person.dni).exists()

    @pytest.mark.django_db
    def test_vehicle_created_successfully(self, vehicle):
        """Verifies that a vehicle is saved in the database"""
        assert Vehicle.objects.filter(id=vehicle.id).exists()

    @pytest.mark.django_db
    def test_make_created_successfully(self, make):
        """Verifies that a make is saved in the database"""
        assert Make.objects.filter(name=make.name).exists()

    @pytest.mark.django_db
    def test_infraction_created_successfully(self, infraction):
        """Verifies that an infraction is saved in the database"""
        assert Infraction.objects.filter(patent=infraction.patent).exists()
