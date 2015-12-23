from django.conf.urls.defaults import patterns, include, url
from tf import views
from tf.views import *
from django.contrib import admin
admin.autodiscover()
    
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
  
urlpatterns = patterns('',
                       
    (r'^admin/', include(admin.site.urls)),

    (r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'./templates/'}), 

    (r'^$',main_page),
    (r'^registe/',registe),
    (r'^login/$',login),

    (r'^search_form/$', views.search_form),
    (r'^search_result/$', views.search_result),
    (r'^summary/$',views.summary),
    (r'^add_form/$',views.add_form),
    (r'^add_result/$',views.add_result),
    
    (r'^computer/$',views.computer),
    (r'^robot/$',views.robot),
    (r'^sensor/$',views.sensor),
    (r'^to_be_lent/$',views.to_be_lent),
    (r'^lending/$',views.lending),
    (r'^return_submit/$',views.return_submit),
    (r'^to_be_given/$',views.to_be_given),
    (r'^to_be_deleted/$',views.to_be_deleted),

    (r'^update/$', views.update),
    (r'^lend/$',views.lend),
    (r'^give/$', views.give),
    (r'^delete/$',views.delete),

    (r'^update_submit/$', views.update_submit),
    (r'^lend_submit/$', views.lend_submit),
    (r'^give_submit/$', views.give_submit),
    (r'^delete_submit/$', views.delete_submit),

                                 
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^myweb/', include('myweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
)

