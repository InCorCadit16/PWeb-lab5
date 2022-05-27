from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('news/', include('news.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    re_path(r'.*', RedirectView.as_view(pattern_name='main')),
    path('', RedirectView.as_view(pattern_name='main')),
]
