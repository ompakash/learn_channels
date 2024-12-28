from django.shortcuts import render
from .models import *
# Create your views here.
def index(request, group_name):
    print('Group name:',group_name)
    group = Group.objects.filter(name=group_name).first()
    chats = []
    if group:
        chats = Chat.objects.filter(group=group)
    else:
        group = Group.objects.create(name=group_name)
    return render (request, 'myapp/index.html',{'groupname' : group_name, 'chats':chats})