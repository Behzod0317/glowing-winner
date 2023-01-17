from django.shortcuts import render
from .models import News
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def get_list(requests, ):
    all_news = News.objects.all()


    data = [
        {'id':i.id,
        'name':i.name,
        'text':i.text,
        } for i in all_news
    ]

    return JsonResponse(data=data, safe=False)

def get_news(requests, id):
    try:
        i = News.objects.get(id=id)
    except:
        return JsonResponse(data={'error':'news not found'})

    data = [
        {'id':i.id,
        'name':i.name,
        'text':i.text,
        } 
    ]

    return JsonResponse(data=data, safe=False)

@csrf_exempt
def add_news(requests, ):
    
 
    name = requests.POST['name']
    text = requests.POST['text']
    try:

        data = News(name=name,text=text)
        data.save()
    except:
        return JsonResponse(data={"error":"something went wrong"})


    return JsonResponse(data={'success':f"News id {data.id}"},safe=False)