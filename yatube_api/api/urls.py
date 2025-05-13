from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (PostViewset, CommentViewset,
                    GroupViewset, FollowViewset)

router = SimpleRouter()
router.register('posts', PostViewset)
router.register('groups', GroupViewset, basename='groups')
router.register('follow', FollowViewset, basename='follow')

comments_router = SimpleRouter()
comments_router.register('comments', CommentViewset, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/posts/<int:post_id>/', include(comments_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
