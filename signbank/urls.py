from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import logout

from django.contrib import admin
admin.autodiscover()


if settings.SHOW_NUMBERSIGNS:
    numbersigns_view = TemplateView.as_view(template_name='numbersigns/numbersigns.html')
else:
    numbersigns_view = TemplateView.as_view(template_name='numbersigns/underconstruction.html')


urlpatterns = [
    #url(r'^$', flatpageviews.flatpage, {'url': '/'}, name='root_page'),

    url(r'^dictionary/', include('dictionary.urls', namespace='dictionary')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^video/', include('video.urls', namespace='video')),

    #(r'^register.html', 'signbank.views.index'),
    url(r'^logout.html', logout,
                        {'next_page': "/"}, "logout"),


    url(r'^spell/twohanded.html$', TemplateView.as_view(template_name='fingerspell/fingerspellingtwohanded.html')),
    url(r'^spell/practice.html$', TemplateView.as_view(template_name='fingerspell/fingerspellingpractice.html')),
    url(r'^spell/onehanded.html$', TemplateView.as_view(template_name='fingerspell/fingerspellingonehanded.html')),
    url(r'^numbersigns.html$', numbersigns_view),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # special admin sub site
#    url(r'^publisher/', include(publisher_admin.urls)),


    url(r'^summernote/', include('django_summernote.urls')),


    url(r'^test/(?P<videofile>.*)$', TemplateView.as_view(template_name="test.html")),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
