from authentication.models import Person
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ['created_at', 'updated_at']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'min_length': 8
            }
        }

    def create(self, validated_data):
        person = super().create(validated_data)
        person.set_password(person.password)
        person.save()
        person.password = None
        return person


class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=8, max_length=50)
    confirm_new_password = serializers.CharField(min_length=8, max_length=50)

    def validate(self, data):
        """
        Check password is same or not
        """

        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError('Password doest not match!')
        return data
