from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
import json
from PIL import Image, ImageOps
import urllib.request


# Create your views here.
from rest_framework.response import Response


@csrf_exempt
def operations(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print (request.body)
        pk = body['pk']
        image = body['image']
        urllib.request.urlretrieve(
            image,
            "gfg.png")
        image = Image.open("gfg.png")
        greyscale_image = image.convert('L')
        request.session['image'] = greyscale_image
        options = body['checkedOptions']
        if options['horizontal']:
           view = flip(request, greyscale_image, "horizontal")
        if options['vertical']:
            view = flip(request, greyscale_image, "vertical")
        else:
            pass
    return JsonResponse({'image': greyscale_image})
    #return render(request, 'index.html')

@csrf_exempt
def flip(request, image_got, rotate):
    if rotate == "vertical":
       image_flip_left = image_got.transpose(Image.FLIP_LEFT_RIGHT)
       request.session['image'] = image_flip_left
       view = thumbnail(request, request.session['image'])
    else:
        image_flip_top = image_got.transpose(Image.FLIP_TOP_BOTTOM)
        request.session['image'] = image_flip_top
        view = thumbnail(request, request.session['image'])


@csrf_exempt
def thumbnail(request, image_got):
    image = image_got.resize((50, 50))
    image.show()















@csrf_exempt
def resize():
    pass


@csrf_exempt
def rotate():
    pass









