import json

from django.http import JsonResponse

from django.http.response import HttpResponseBadRequest, HttpResponse

from grocery_list.models import List


def get_list(request):
    items = List.objects.all().order_by('due_date')
    jsonized = [{'title': i.name(), 'done': i.is_done, 'due': i.due_date} for i in items]
    return JsonResponse(jsonized, safe=False)


def add_list_item(request):
    if request.is_ajax() and request.method == 'POST':
        items = json.loads(request.body)
        for list_item in items:
            List.add(list_item['title'], list_item['due'])

        return HttpResponse('')
    else:
        return HttpResponseBadRequest("Bad request")


def set_done(request, item_id, checked):
    try:
        list_item = List.objects.get(id=item_id)
        list_item.is_done = checked == 'true'
        list_item.save()
        return HttpResponse('')
    except:
        return HttpResponseBadRequest("Bad request")