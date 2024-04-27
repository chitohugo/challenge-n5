from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from common.base_model import Base, AbstractBase
from common.generate_id_official import generator_id
from common.validates import validate_patent


class User(AbstractUser, Base):
    pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Person(AbstractBase, models.Model):
    email = models.EmailField(unique=True, blank=False, null=False)
    dni = models.IntegerField(unique=True, blank=False, null=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class Vehicle(Base):
    patent = models.CharField(max_length=50, unique=True, validators=[validate_patent], blank=False, null=False)
    color = models.CharField(max_length=50, blank=False, null=False)
    make = models.ForeignKey("Make", on_delete=models.CASCADE, blank=False, null=False, related_name="vehicles")
    owner = models.ForeignKey("Person", on_delete=models.CASCADE, blank=False, null=False, related_name="vehicles")

    def __str__(self):
        return self.patent

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"


class PoliceOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id_official = models.IntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.id_official})'

    class Meta:
        verbose_name = "Oficial de Policía"
        verbose_name_plural = "Oficiales de Policía"

    @receiver(post_save, sender=User)
    def create_official(sender, instance, created, **kwargs):
        if created:
            id_official = generator_id()
            PoliceOfficer.objects.create(user=instance, id_official=id_official)


class Make(Base, models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Marca de Vehículo"
        verbose_name_plural = "Marcas de Vehículos"


class Model(Base):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    make = models.ForeignKey("Make", on_delete=models.CASCADE, blank=False, null=False, related_name="models")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Modelo de Vehículo"
        verbose_name_plural = "Modelos de Vehículos"


class Infraction(Base, models.Model):
    patent = models.ForeignKey("Vehicle", on_delete=models.CASCADE, blank=False, null=False, related_name="infractions")
    comment = models.TextField(blank=False, null=False)
    created_by = models.ForeignKey("PoliceOfficer", on_delete=models.CASCADE, blank=False, null=False, related_name="infractions")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Infracción Vehícular"
        verbose_name_plural = "Infracciones Vehículares"
