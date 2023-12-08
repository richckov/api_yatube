from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path
from .views import CommentViewSet, GroupViewSet, PostViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
    path('api-token-auth/', views.obtain_auth_token),
]
