from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import environ
import os
from MainApp.models import Item
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

DEFAULT_USER = env('DEFAULT_USER')
DEFAULT_USER_FIRST_NAME = env('DEFAULT_USER_FIRST_NAME')
DEFAULT_USER_MIDDLE_NAME = env('DEFAULT_USER_MIDDLE_NAME')
DEFAULT_USER_SECOND_NAME = env('DEFAULT_USER_SECOND_NAME')
DEFAULT_USER_EMAIL = env('DEFAULT_USER_EMAIL')
DEFAULT_USER_PHONE = env('DEFAULT_USER_PHONE')
#items = env('ITEMS')

# Create your views here.


items = Item.objects.all()


def home(request):
    context = {
        "name": f"{DEFAULT_USER}",
        "email": f"{DEFAULT_USER_EMAIL}"
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        "first_name": DEFAULT_USER_FIRST_NAME, 
        "second_name": DEFAULT_USER_SECOND_NAME,
        "middle_name": DEFAULT_USER_MIDDLE_NAME,
        "phone": DEFAULT_USER_FIRST_NAME,
        "email": DEFAULT_USER_FIRST_NAME
    }
    return render(request, "about.html", context)


def get_item(request, id:int):
    colors = []
    for i in items:
        if i.id == id:
            if i.colors.exists():
                colors = i.colors.all()    
            context = {
                "item": i,
                "colors":colors
            }
            return render(request, "item.html", context)
        
    text = f'Товар с id={id} не найден<br></br><a href="/items">назад к списку товаров</a>'
    return HttpResponseNotFound(text)
    

def get_items(request):
    context = {
        "items": items
    }
    return render(request, "items.html", context)

