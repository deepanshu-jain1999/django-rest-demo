from rest_framework import serializers
from apps.models import Profile
from django.contrib.auth.models import User
import datetime


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    slug = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Profile
        fields = ['url', 'slug', 'title', 'owner', 'username', 'password', 'email', 'start_year', 'name', 'datafile']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        # read_only_fields = ('datafile')

    def validate(self, data):
        now = datetime.datetime.now().year
        if data['start_year'] > now:
            raise serializers.ValidationError("Enter correct join year")
        return data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedRelatedField(many=True, view_name='profile-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'profile')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(min_length=8)
    new_password = serializers.CharField(min_length=8)
    new_confirm_password = serializers.CharField(min_length=8)

    class Meta:
        def validate(self, attrs):
            old_password = attrs.get('old_password')
            new_password = attrs.get('new_password')
            new_confirm_password = attrs.get('new_confirm_password')

            if new_password != new_confirm_password:
                message = "Enter the same password"
                raise serializers.ValidationError(message)




