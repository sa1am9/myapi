from rest_framework import serializers
from post.models import Post
from account.models import Account

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=Account.objects.all(), slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'count_like', 'count_unlike', 'date')
