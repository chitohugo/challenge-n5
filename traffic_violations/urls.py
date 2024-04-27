from django.urls import path, include
from rest_framework.routers import DefaultRouter

from traffic_violations.views import InfractionViewSet, RegisterView

router = DefaultRouter()

router.register(r'infractions', InfractionViewSet, basename='infraction')
register = RegisterView.as_view()

urlpatterns = [
    path('', include(router.urls)),
    path('register', register),
]
