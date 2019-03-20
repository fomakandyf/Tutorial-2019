"""
Definition of urls for DjangoWeb.
"""

from datetime import datetime
from DjangoWeb import urls
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
admin.autodiscover()

import app.forms
import app.views
import polls.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', app.views.home, name='home'),
    path('polls', polls.views.index, name='index'),
    path('polls/<int:question_id>', polls.views.detail, name='detail'),
    path('polls/<int:question_id>/results', polls.views.results, name='results'),
    path('polls/<int:question_id>/vote', polls.views.vote, name='vote'),
    path('contact', app.views.contact, name='contact'),
    path('about', app.views.about, name='about'),
    path('login',
        LoginView.as_view(),
        {
            'template_name': 'app/registration/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    path('logout',
        LogoutView.as_view(),
        {
            'template_name': 'app/registration/loggedoff.html',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    path('admin/doc', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path('admin', admin.site.urls),
]
