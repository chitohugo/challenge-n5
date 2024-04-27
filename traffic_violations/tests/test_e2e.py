import pytest

from traffic_violations.models import PoliceOfficer


class TestViews:
    """A class with tests for the Tasks and Record views
    """

    @pytest.fixture
    def client(self, token, api_client):
        """Method with authenticated client

        Args:
            token: Access token
            api_client: instance of APIClient

        Returns:
            A client with authorization
        """
        api_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token['access']}",
        )
        return api_client

    @pytest.mark.django_db
    def test_register_user(self, api_client):
        """Test registering a user

        Args:
            api_client: instance of api_client

        Returns:
            None
        """
        payload = {
            "first_name": "Jennifer",
            "last_name": "Mitchell",
            "email": "jennifer.m@outlook.com",
            "password": "congueJenn",
            "password2": "congueJenn",
            "username": "absentsteam"
        }
        response = api_client.post('/api/v1/register', data=payload)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_generate_infractions(self, client, infraction):
        """Test create an infractions report

        Args:
            client: api_client with authorization
            infraction: instance of Infraction

        Returns:
            None
        """
        email = "annaking@hotmail.com"

        response = client.get(f'/api/v1/infractions/generate-inform/?email={email}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_create_infraction(self, client, vehicle, user):
        """Test create an infractions report

        Args:
            client: api_client with authorization
            infraction: instance of Infraction

        Returns:
            None
        """
        officer_police = PoliceOfficer.objects.get(user=user)
        payload = {
            "patent": vehicle,
            "comment": "Conducir bajo el efectos del alcohol",
            "created_by": officer_police
        }

        response = client.post(f'/api/v1/infractions/', data=payload)
        assert response.status_code == 201

