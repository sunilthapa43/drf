#import json
#from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

#def api_home(request, *args, **kwargs):
#
#    print(request.GET) #url query params
#    body = request.body
#    
#
#    data = {}
#    try:
#        data = json.loads(body)
#    except: 
#        pass
#
#    print(data)
#    data['params'] = dict(request.GET)
#    data['headers'] = dict(request.headers)
#    print(request.headers)
#    data['content_type'] = request.content_type
#    return JsonResponse(data)
#


#def api_home(request, *args, **kwargs):
 #   model_data = Product.objects.all().order_by("?").first()
 #   data = {}
#
 #   if model_data:
 #       data['id'] = model_data.id
 #       data['title'] =model_data.title
 #       data['content'] =model_data.content
 #       data['price'] =model_data.price
#
 #   return JsonResponse(data)


# this is so long, why dont we use model_to_dict to get same result

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    """DRF API view"""

    #if request.method != "POST":
    #    return Response({"detail": "GET not allowed"},status=400)

    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields= ['id', 'title'])

    return Response(data, ) 

#lets use serializer