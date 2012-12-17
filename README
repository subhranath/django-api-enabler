A Django helper app to let you specify API urls from within the apps.

Why?
====
- Do you use multiple apps in your django project?
- Do you use the conventional django way of managing your urlconfs (where you include other urlconfs to your apps)?
- Do you wish to have URL prefix like '/api/' followed by your custom app prefix?
- Do you like to keep the URLconf at the app level for individual mappings?

If your answer is Yes to all, then this app is for you.

What?
=====
In simplest way, when your have your urlconf like:

urlpatterns = patterns('',
    # ... snip ...
    (r'^accounts/', include('accounts.urls')),
    (r'^analytics/', include('analytics.urls')),
    (r'^search/', include('search.urls')),
    (r'^r/', include('inventory.urls')),
    # ... snip ...
)

And you want to have APIs associated with different apps in your project like:
/api/accounts/
/api/analytics/
/api/search/
# ... and more ...
where the mapping to views remains within the individual apps.

How to use?
===========
- Include "api_enabler" in your INSTALLED_APPS.
- Add "url(r'^api/', include('api_enabler.urls'))" to your base urlconf. Preferably somewhere on top.
(Optional: You can change the string 'api' to whatever else you want as your root API prefix)
- Add a api.py urlconf module to each of the apps where you want API urls enabled. (* See below)
- API_URL_PREFIX in {{ app_name }}/api.py should be set to a custom url-slug to use as prefix for the app.

* (For e.g. if you want to enable APIs in your accounts app your accounts/api.py file should look like:
	from django.conf.urls.defaults import patterns, include, url
	
	urlpatterns = patterns('accounts.views.apis',
		...
	    url(r'^register/$', 'api_register_handler'),
	    url(r'^login/$', 'api_login_handler'),
	    url(r'^logout/$', 'api_logout_handler'),
		...
	)
	
	API_URL_PREFIX = 'accounts'
)

That's it! Now you can manage your API URLs with customizable slugs from within your app directory.

Features:
=========
- You can disable APIs associated with any particular app, by renaming your api.py of the app to anything else.
- To disable APIs for the entire project, just remove 'api_enabler' from your INSTALLED_APPS.

