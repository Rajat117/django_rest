from blog.models import Blog
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = []
