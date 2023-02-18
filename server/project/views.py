from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy


from project.models import *
from project.forms import RegisterUserForm, LoginForm, ChangeProfile
from project.utils import BaseMixin


class HomeProject(BaseMixin, ListView):

    model = Posts
    context_object_name = 'posts'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Головна сторінка', profile=f'profile/{self.request.user}/')
        
        return context | mixin


    def get_queryset(self):
        return Posts.objects.filter(is_published=True).order_by('-pk')


class AllPosts(BaseMixin, ListView):

    model = Posts
    context_object_name = 'posts'
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Всі категорії', cat_selected=0)

        return context | mixin



class CategoryListView(BaseMixin, ListView):
    model = Posts
    template_name = 'posts.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        mixin = self.get_user_context(title='Категорія - ' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id)


        return context | mixin

    def get_queryset(self):
        return Posts.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class ShowPostListView(BaseMixin, DetailView):
    model = Posts
    template_name = 'show_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title=context['post'].title)

        return context | mixin

    
class RegisterUser(BaseMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Реєстрація')

        return context | mixin

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')

    
    def get_success_url(self) -> str:
        return reverse('profile', kwargs={'username': self.request.user})


class LoginUser(BaseMixin, LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Вхід')

        return context | mixin

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.request.user})


def logout_user(request):
    logout(request)

    return redirect('home')



# class ProfileUser(BaseMixin, CreateView):

#     form_class = ChangeProfile
#     template_name = 'profile.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         mixin = self.get_user_context(title=f'Особистий кабінет - {self.request.user}')

#         return context | mixin


#     def form_valid(self, form):

#         return redirect('home')

class ProfileUser(BaseMixin, DetailView):

    model = Profile
    slug_url_kwarg = 'username'
    slug_field = 'username'
    template_name = 'profile.html'
    context_object_name = 'user_profile'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title=context['user_profile'].username)

        return context | mixin



# def profile_user(request, username):
#     print(request.user.username)
#     context_dict = {}
    
#     get_user = get_object_or_404(User, username=username)
#     user_profile = Profile.objects.get(user=get_user)
#     context_dict['user_profile'] = user_profile

#     return render(request, 'profile.html', context_dict)


def about(request):
    return HttpResponse('Hello!')


class AllUsers(BaseMixin, ListView):
    model = Profile
    template_name = 'index.html'
    context_object_name = 'users'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Всі користувачі')

        return context | mixin


    def get_queryset(self):
        return Profile.objects.all()