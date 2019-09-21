from django.shortcuts import render
from learning_logs.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from learning_logs.form import *
# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request,'index.html')


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request,'new_topic.html',context)