from django.shortcuts import render
from .serializers import MailingSerializer, ClientSerializer, MessageSerializer
from rest_framework import viewsets
from .models import Mailing, Client, Message
from django_filters.rest_framework import DjangoFilterBackend
from filter import ClientFilter


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
    filter_backends = (DjangoFilterBackend)
    filterset_class = ClientFilter


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
