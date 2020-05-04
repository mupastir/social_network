from rest_framework import serializers

from social_network.users.api.serializers import AuthorOutputSerializer

from social_network.posts.models import Like, Post


class PostInputSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    content = serializers.CharField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'id')
        read_only_fields = ('author', 'id')

    def create(self, validated_data):
        validated_data.update({'author': self.context['request'].user})
        return super().create(validated_data)


class PostOutputSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    content = serializers.CharField()
    author = AuthorOutputSerializer()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'likes', 'id')

    def get_likes(self, obj):
        return obj.like_set.objects.count()


class PostLikeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data.update({'author': self.context['request'].user,
                               'post': self.context['request'].data['post']})
        return super().create(validated_data)

    class Meta:
        model = Like
        fields = ('author', 'post')
        read_only_fields = ('author', 'post')
