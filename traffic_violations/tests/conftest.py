import pytest
from rest_framework.test import APIClient

from traffic_violations.models import User, PoliceOfficer, Person, Vehicle, Make, Model, Infraction


@pytest.fixture(scope="function")
def api_client():
    yield APIClient()


@pytest.fixture
def user():
    payload = {
        "first_name": "Testing",
        "last_name": "Testing",
        "email": "testing@test.com",
        "password": "Testing",
        "username": "testing"
    }
    user = User.objects.create(**payload)
    user.set_password(payload['password'])
    user.save()
    return user

@pytest.fixture
def person(user):
    payload = {
        "first_name": "Anna",
        "last_name": "King",
        "email": "annaking@hotmail.com",
        "dni": 96345678
    }
    instance = Person.objects.create(**payload)
    instance.save()
    return instance


@pytest.fixture
def make():
    payload = {
        "name": "Ferrari",
    }
    instance = Make.objects.create(**payload)
    instance.save()
    return instance


@pytest.fixture
def model(make):
    payload = {
        "name": "F500",
        "make": make
    }
    instance = Model.objects.create(**payload)
    instance.save()
    return instance


@pytest.fixture
def vehicle(make, person):
    payload = {
        "patent": "AW 346 ED",
        "color": "Rojo",
        "make": make,
        "owner": person
    }
    instance = Vehicle.objects.create(**payload)
    instance.save()
    return instance


@pytest.fixture
def infraction(vehicle, user):
    police_officer = PoliceOfficer.objects.get(user=user)
    payload = {
        "patent": vehicle,
        "comment": "Vuelta en U",
        "created_by": police_officer
    }
    instance = Infraction.objects.create(**payload)
    instance.save()
    return instance


@pytest.fixture
def token(user, api_client):
    payload = {
        "username": "testing",
        "password": "Testing"
    }
    response = api_client.post('/api/v1/sign-in', data=payload)
    print(response.json())
    return response.json()
