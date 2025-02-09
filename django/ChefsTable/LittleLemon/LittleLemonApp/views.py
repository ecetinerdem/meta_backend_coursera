from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from LittleLemonApp.forms import LogForm

#from .models import Menu
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello World!")

def homepage(request):
    content = "<html><body><h1>Welcome to Little Lemon</h1></body></html>"
    return HttpResponse(content)

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon"""
    return HttpResponse(text)

def menuitems(request, dish):
    menu = {
        "pasta": "Pasta is a type of noodle made from wheat, eggs and water",
        "falafel": "Falafel is a deep fried balls made out of beans",
        "cheesecake": "Cheesecake is a type of desert made with cream, soft cheese on top of cookie, pastry crumbs or graham crakers and fruit sauce topping",
    }
    
    description = menu[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description)

def shift_form(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "shift.html", context)

def about(request):
    about_content = {"about": "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, "about.html", about_content)
# Create view for Menu

def menu_pic(request):
    about_menu = {"cheesecake": "Cheesecake is a type of desert made with cream, soft cheese on top of cookie, pastry crumbs or graham crakers and fruit sauce topping"}
    return render(request, "menu.html", about_menu)