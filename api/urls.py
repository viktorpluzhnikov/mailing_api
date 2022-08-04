from django.urls import path, include
from rest_framework import routers

from .views import MailingViewSet, ClientViewSet, MessageViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('mailing', MailingViewSet)
router.register('client', ClientViewSet)
router.register('message', MessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

