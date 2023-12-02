from django.shortcuts import render
from django.http import HttpResponse
from FirstDjango import settings
# import environ
# import os


# Create your views here.

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]



def home(request):
    text = """
    <h1>Изучаем django</h1>
    <strong>Автор</strong>: <i>Ермишев А.В.</i>
    """
    return HttpResponse(text)

def about(request):
    text = f"""
    Имя: <strong>{settings.DEFAULT_USER_FIRST_NAME}</strong>
    <br></br>
    Отчество: <strong>{settings.DEFAULT_USER_MIDDLE_NAME}</strong>
    <br></br>
    Фамилия: <strong>{settings.DEFAULT_USER_SECOND_NAME}</strong>
    <br></br>
    телефон: <strong>{settings.DEFAULT_USER_PHONE}</strong>
    <br></br>
    email: <strong>{settings.DEFAULT_USER_EMAIL}</strong>
    <br></br>
    """
    return HttpResponse(text)

def get_item(request, id):
    item = None
    for i in items:
        if i["id"] == id:
            item = i
    if item:
        text =  f'Название: {item["name"]}, кол-во: {item["quantity"]}<br></br><a href="/items">назад к списку товаров</a>'
    else:
        text = f'Товар с id={id} не найден<br></br><a href="/items">назад к списку товаров</a>'

    return HttpResponse(text)

def get_items(request):
    text = f"""
        <ul>{''.join([f'<li>{i["id"]}: {i["name"]} <a href="/item/{i["id"]}">Страница{i["name"]}</a></li><br></br>' for i in items])}</ul>
            """
    return HttpResponse(text)
# <a href="URL">...</a>
# <a name="идентификатор">...</a>