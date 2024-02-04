from django.shortcuts import render
from django.http import JsonResponse
from .models import MMDQuickFavorites
from ..mmdlist.models import MMDInfo

# Create your views here.
def post(request):
    # GET 방식 호출에만 반응 / 파라메터 유무 검사
    if (request.method == 'GET' 
        and 'act' in request.GET
        and 'key' in request.GET 
        and 'user' in request.GET):
        # save action
        if (request.GET['act'] == 'save' and 'data' in request.GET):
            newData = MMDQuickFavorites()
            newData.AccessKey = request.GET['key']
            newData.Username = request.GET['user']
            newData.Data = request.GET['data']
            newData.save()
            return render(request, 'quickload.html', {'result':'Save Success'})
        # load action
        elif (request.GET['act'] == 'load'):
            datas = MMDQuickFavorites.objects.filter(AccessKey=request.GET['key'], Username=request.GET['user']).values('Data')
            if (datas.count() > 0):
                return render(request, 'quickload.html', {'result':datas.first()['Data']})
            else:
                return render(request, 'quickload.html', {'result':'No Data'})
        # load mmdlist action
        elif (request.GET['act'] == 'list'):
            listSet = MMDInfo.objects.all()
            if (listSet.count() > 0):
                dictionaries = [ obj.as_dict() for obj in listSet ]
                return render(request, 'quickload.html', {'result':dictionaries})
            else:
                return render(request, 'quickload.html', {'result':'No Data'})
    # parameter error
    return render(request, 'quickload.html', {'result':'Incorrect Parameter'})