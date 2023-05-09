from django.shortcuts import render, redirect
from .models import HomePage, AboutPageInfo, AboutChef, Menu, MenuCategory, Book
from .forms import BookForm
# Create your views here.

def index(request):
    home_page = HomePage.objects.all()[0]
    return render(request, 'main/index.html', context={
        'link':'index',
        'home_page':home_page
    })

def about(request):
    about_info = AboutPageInfo.objects.all()[0]
    about_chef = AboutChef.objects.all()
    return render(request, 'main/about.html', context={
        'link':'about',
        'about_info':about_info,
        'about_chef':about_chef
        
    })

def booking(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'main/booking.html', context={
        'link':'booking',
        'form':form
        
    })

def contact(request):
    return render(request, 'main/contact.html', context={
        'link':'contact'
        
    })

def menu(request):
    menu_list = MenuCategory.objects.all()
    return render(request, 'main/menu.html', context={
        'link':'menu',
        'menu_list':menu_list
        
    })

def service(request):
    return render(request, 'main/service.html', context={
        'link':'service'
        
    })