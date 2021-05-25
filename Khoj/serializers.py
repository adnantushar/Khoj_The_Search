from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ValuesStored



User = get_user_model()


class SearchFormSerializer(serializers.Serializer):
    startDateTime = serializers.DateTimeField(required=True, write_only=True)#format="%Y-%m-%d %H:%M:%S.%f%z"
    endDateTime = serializers.DateTimeField(required=True, write_only=True)
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return str(obj.user)

class SearchListSerializer(serializers.Serializer):

    status = serializers.CharField(default='Success', initial='Success')
    user_id = serializers.SerializerMethodField()
    payload = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        qs = obj.filter(id=1)[:1].get()
        id = qs.user.id
        return id

    def get_payload(self, obj):
        search = SearchSerializer(obj, many=True).data
        return search


class EmptySerializer(serializers.Serializer):
    pass


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValuesStored
        fields = ('timeStamp', 'inputValues')
