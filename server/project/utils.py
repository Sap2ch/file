from .models import *
from django.db.models import Count, Q
from django.urls import reverse
from django.views.generic import ListView


class BaseMixin:
    # paginate_by = 5

    def get_user_context(self, **kwargs):
        
        menu = [
            {'title': 'Про нас', 'url_name': 'about'},
            {'title': "Зворотній зв'язок", 'url_name': 'callback'},
            {'title': 'Оплата', 'url_name': 'payments'},
            {'title': 'Користувачі', 'url_name': 'users'},
        ]

        cats = Category.objects.filter(posts__is_published=True).annotate(Count('posts')).order_by('pk')
        # profiles = Profile.objects.filter(username__contains='ROOT')


        context = kwargs
        context['menu'] = menu
        context['cats'] = cats
        # context['profiles'] = profiles

        if 'cat_selected' not in context:
            context['cat_selected'] = None
            

        return context

