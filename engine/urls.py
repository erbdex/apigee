from django.conf.urls import patterns, include, url
# from django.contrib import admin
from src.view import default, add_to_auction, get_bids, add_item

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'engine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', default),
    url(r'^auction', add_to_auction),
    url(r'^bid', get_bids),
    url(r'^item', add_item),
    url(r'', default),
)
