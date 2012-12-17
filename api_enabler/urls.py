from django.conf.urls.defaults import patterns, include, url
import api_enabler

api_url_conf = api_enabler.autodiscover()

urlpatterns = patterns('',
    url(r'', include(api_url_conf)),
)
