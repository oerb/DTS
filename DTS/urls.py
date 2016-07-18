from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from DTSERVER import views

admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'workinterval', views.Work_IntervalViewSet)
router.register(r'worktyp', views.WorktypViewSet)
router.register(r'worktime', views.WorktimeViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DTS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
