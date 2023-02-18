from project.views import *
from django.urls import path, re_path


urlpatterns = [
    path('', HomeProject.as_view(), name='home'),
    path('about/', about, name='about'),
    path('callback/', about, name='callback'),
    path('payments/', HomeProject.as_view(), name='payments'),

    path('category/all/', AllPosts.as_view(), name='all'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name='category'),
    path('post/<slug:post_slug>/', ShowPostListView.as_view(), name='post'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<slug:username>/', ProfileUser.as_view(), name='profile'),
    path('users/', AllUsers.as_view(), name='users'),
    # path('profile/<slug:username>/', profile_user, name='profile'),
]
