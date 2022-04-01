from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import categories, photographer, photos, BackgroundImage
from django.template import RequestContext
import random,math
from math import ceil
# Create your views here.
def index(request):
    query=photos.objects.all().count()
    while True:
        r1=random.randrange(1,query)
        check=query-r1
        if check <6:
            r1=random.randrange(1,query)
        else :
            break
    n=2
    Photos=[]
    photo= photos.objects.values('category')
    category= {item["category"] for item in photo}
    for cat in category:
        pics=photos.objects.filter(category=cat)[:1]
        Photos.append([pics, n])
         
    contex = {
        'Images':Photos,
        'Photo': photos.objects.all()[r1:query][:6],
        'Category':categories.objects.all(),
        'photographers':photographer.objects.all(),
        'backimage':BackgroundImage.objects.all(),
    }
    return render(request, 'index.html', contex)

def contact(request):
    contex = {
         'Category':categories.objects.all(),
        'backimage':BackgroundImage.objects.all(),
    }
    return render(request, 'contact.html', contex)

def about(request):
    contex = {
         'Category':categories.objects.all(),
        'backimage':BackgroundImage.objects.all(),
    }
    return render(request, 'about.html', contex)

def single(request):
    n=1
    Photos=[]
    photo= photos.objects.values('category')
    category= {item["category"] for item in photo}
    for cat in category:
        pics=photos.objects.filter(category=cat)[:3]
        Photos.append([pics, n])

    contex = {
        'Photos':Photos,
        'Category':categories.objects.all(),
        'backimage':BackgroundImage.objects.all()
    }
    return render(request, 'single.html',contex)
 

def category(request,categoryid):
    response=get_object_or_404(categories,Name__exact=categoryid).Name
    categoryid2=categories.objects.get(Name=categoryid).id
    query=photos.objects.only("id").filter(category__exact=categoryid2)
    if len(query) == 0:
        query=photos.objects.only("id")
    images=list(query)
    random_image=random.choice(images)
    if response is not None:
        contex = {
            'Category_Name':categoryid,
            'Category':categories.objects.all(),
            'Photo':photos.objects.filter(category__exact=categoryid2),
            'backimage':photos.objects.get(image_id__exact=random_image)
        }
        return render(request, 'category.html', contex)

def download(request,categoryid,photoid):
    imageid=get_object_or_404(photos,image_id__exact=photoid)
    response=get_object_or_404(categories,Name__exact=categoryid).Name
    categoryid2=categories.objects.get(Name=categoryid).id
    query=photos.objects.only("id").filter(category__exact=categoryid2)
    check=photos.objects.filter(category__exact=categoryid2).filter(image_id__exact=photoid)
    if not check.exists()  :
        return render(request,'404.html')
    if len(query) == 0:
        query=photos.objects.only("id")
    images=list(query)
    random_image=random.choice(images)
    print(check)
    if response is not None:
        contex = {
            'Category_Name':categoryid,
            'Category':categories.objects.all(),
            'Photo':photos.objects.filter(category__exact=categoryid2),
            'image':imageid,
        }
    return render(request,'download_page.html',contex)
   
def handler404(request, *args, **argv):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response