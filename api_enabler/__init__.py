def autodiscover():
    """
    Auto discovers api.py modules in all of INSTALLED_APPS and fails silently
    if not present. This registers all the URLs specified in the api.py module. 
    """
    from django.conf import settings
    from django.conf.urls.defaults import patterns, include, url
    from django.utils.importlib import import_module
    
    urlpatterns = patterns('')
    
    for app in settings.INSTALLED_APPS:
        try:
            mod = import_module('%s.api' % (app, ))
            urlpatterns += patterns('',
                url(r'^%s/' % (mod.API_URL_PREFIX, ), include(mod)),
            )
        except:
            pass
        
    return urlpatterns
