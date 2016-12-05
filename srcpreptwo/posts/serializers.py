from rest_framework import serializers, viewsets
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'content',
			'draft',
			'email',
				]

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
