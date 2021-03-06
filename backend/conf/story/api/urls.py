from django.urls import path
from story.api import views

urlpatterns = [
    path('story/', views.get_root_stories_view),
    path('login/', views.user_login_view),
    path('register/', views.user_registration_view),
    path('story/branch/', views.get_nth_best_branch),
    path('story/next/', views.get_nth_child),
    path('story/prev/', views.get_parent),
    path('story/comment/', views.comment_view),
    path('vote/', views.vote_entity),
    path('profile/', views.profile_view),
    path('follow/', views.follow)
]