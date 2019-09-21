from django.urls import path

from . import views

urlpatterns = [
    #主页
    path('', views.index, name='index'),
    #显示所有主题
    path('topics/$', views.topics, name='topics'),
    #显示特定主题的页面
    path('topics/(?p<topic_id>\d)/$', views.topic, name='topic'),
    #用于添加新主题的网页
    path('new_topic/',views.new_topic,name='new_topic')
]