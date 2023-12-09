from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import environ
import os

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

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]



def home(request):
    # text = f"""
    # <h1>Изучаем django</h1>
    # <strong>Автор</strong>: <i>{DEFAULT_USER}</i>
    # """
    # return HttpResponse(text)
    context = {
        "name": f"{DEFAULT_USER}",
        "email": f"{DEFAULT_USER_EMAIL}"
    }
    return render(request, 'index.html', context)


def about(request):
    text = f"""
    Имя: <strong>{DEFAULT_USER_FIRST_NAME}</strong>
    <br></br>
    Отчество: <strong>{DEFAULT_USER_MIDDLE_NAME}</strong>
    <br></br>
    Фамилия: <strong>{DEFAULT_USER_SECOND_NAME}</strong>
    <br></br>
    телефон: <strong>{DEFAULT_USER_PHONE}</strong>
    <br></br>
    email: <strong>{DEFAULT_USER_EMAIL}</strong>
    <br></br>
    """
    return HttpResponse(text)

def get_item(request, id:int):
    for i in items:
        if i["id"] == id:
            # text =  f"""
            # <h2>Название: {i["name"]}</h2> 
            # <p>Кол-во: {i["quantity"]}</p>
            # <a href="/items">назад к списку товаров</a>
            # """
            # return HttpResponse(text)
            context = {
                "name": i["name"],
                "quantity": i["quantity"],
                "q": False if i["quantity"] != 0 else True
            }
            return render(request, "item.html", context)
        
    text = f'Товар с id={id} не найден<br></br><a href="/items">назад к списку товаров</a>'
    return HttpResponseNotFound(text)
    

def get_items(request):
    # text = f"""
    #     <h2>Список товаров</h2>
    #     <ol>{''.join([f'<li><a href="/item/{i["id"]}">{i["name"]}</a></li>' for i in items])}</ol>
    #         """
    # return HttpResponse(text)
    context = {
        "items": items
    }
    
    return render(request, "items.html", context)