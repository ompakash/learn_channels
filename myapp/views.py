from django.shortcuts import render

# Create your views here.
def index(request, group_name):
    print('Group name:',group_name)
    return render (request, 'myapp/index.html',{'groupname' : group_name})