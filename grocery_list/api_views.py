import json

from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from grocery_list.models import List


def get_list(request):
    items = List.objects.all().order_by('due_date')
    jsonized = [{'id': i.id, 'title': i.name(), 'done': i.is_done, 'due': i.due_date} for i in items]
    return JsonResponse(jsonized, safe=False)


@csrf_exempt
def add_list_item(request):
    if request.is_ajax() and request.method == 'POST':
        try:
            items = json.loads(request.body.decode('utf-8'))
            for list_item in items:
                List.add(list_item['title'], list_item['due'])

            return HttpResponse('')
        except Exception as e:
            raise e
    return HttpResponseBadRequest("Bad request")


@csrf_exempt
def set_done(request):
    if request.is_ajax() and request.method == 'POST':
        try:
            params = json.loads(request.body)
            list_item = List.objects.get(id=params['id'])
            list_item.is_done = params['checked']
            list_item.save()
            return HttpResponse('')
        except Exception as e:
            raise e
    return HttpResponseBadRequest("Bad request")