from django.conf.urls import *

import nexus

nexus.autodiscover()

urlpatterns = patterns('',
    url(r'', include(nexus.site.urls)),
)
