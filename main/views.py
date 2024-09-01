from django.shortcuts import render

from goods.models import Category


def index(request):
    
    context = {
        'title': "Главная",
        'welcome': "Добро пожаловать в Pizza House",
        'about': "Здесь, вы не сможете уйти с пустым желудком!",
    }
    return render(request, "main/index.html", context)



def contact(request):
    context = {
        'title': "Контакты",
        'about': "Свяжитесь с нами по телефону: 8800553535",
    }
    return render(request, "main/contact.html", context)

def cart(request):
    return render(request, "main/cart.html")

