from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator

import uuid


class Mailing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    tag = models.CharField(max_length=8, blank=True, null=True)
    #time_zone = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    send_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    id_client = models.ForeignKey('Client', on_delete=models.PROTECT, related_name='client')
    id_mailing = models.ForeignKey('Mailing', on_delete=models.PROTECT, related_name='mailing')