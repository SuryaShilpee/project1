from django.conf.urls import include, url
import project1.views as views


urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^insert_data/$', views.insert_data),
    url(r'^updated_data/$', views.updated_data2),
    # url(r'^updated_data2/$', views.updated_data),

]
