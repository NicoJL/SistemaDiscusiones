from django.conf.urls import patterns, include, url
from .views import ExtraDataView , UserDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaDiscusiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^log-out/$', 'apps.users.views.LogOut' , name="logout"),
    url(r'^extra-data/$', ExtraDataView.as_view() , name="extra_data"),
    # url mandando el id url(r'^usuario/(?P<pk>[\d]+)/$', UserDetailView.as_view(), name='user_detail'),
 	url(r'^usuario/(?P<slug>[-\w]+)/$', UserDetailView.as_view(), name='user_detail'),
)
