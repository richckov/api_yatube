from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404

from posts.models import Post, Group
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import AuthorOnly, GroupOnlyGet


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOnly, permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(
    viewsets.ReadOnlyModelViewSet,
    viewsets.GenericViewSet
):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (GroupOnlyGet, permissions.IsAuthenticated)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOnly, permissions.IsAuthenticated)

    def get_post(self):
        post_id = self.kwargs.get("post_id")
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)
