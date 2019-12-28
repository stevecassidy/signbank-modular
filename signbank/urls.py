from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from pages.models import Page

admin.autodiscover()


sitemap_dict = {
    'queryset':  Page.objects.all(),
}


if settings.SHOW_NUMBERSIGNS:
    numbersigns_view = TemplateView.as_view(template_name='numbersigns/numbersigns.html')
else:
    numbersigns_view = TemplateView.as_view(template_name='numbersigns/underconstruction.html')


urlpatterns = [

    path('dictionary/', include('dictionary.urls', namespace='dictionary')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('video/', include('video.urls', namespace='video')),

    path('logout.html', auth_views.LogoutView.as_view(),
                        {'next_page': "/"}, "logout"),

    path('spell/twohanded.html', TemplateView.as_view(template_name='fingerspell/fingerspellingtwohanded.html')),
    path('spell/practice.html', TemplateView.as_view(template_name='fingerspell/fingerspellingpractice.html')),
    path('spell/onehanded.html', TemplateView.as_view(template_name='fingerspell/fingerspellingonehanded.html')),
    path('numbersigns.html', numbersigns_view),

    path('accounts/', include('allauth.urls')),

    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    path('summernote/', include('django_summernote.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': {'pages': GenericSitemap(sitemap_dict, priority=0.6)}},
        name='cached-sitemap'),

    path('test/<videofile>', TemplateView.as_view(template_name="test.html")),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
