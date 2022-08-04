from django_filters import rest_framework as filters
from models import Client


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ClientFilter(filters.FilterSet):
    phoneNumber = CharFilterInFilter(field_name='client_phoneNumber')
    tag = filters.CharFilter

    class Meta:
        model = Client
        fields = ['phoneNumber', 'tag']