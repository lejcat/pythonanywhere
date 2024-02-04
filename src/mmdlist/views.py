# views.py
from django.shortcuts import render
from .models import MMDInfo

def ViewList(request):
    mmd_all = MMDInfo.objects.all()#모든 행을 전부 가져오라는 뜻
    return render(request, 'list.html', {"mmdlist":mmd_all})