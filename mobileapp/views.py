from django.shortcuts import render, redirect
from mobileapp.models import Category_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def index_page(request):
    return render(request, "index.html")
def add_categories(request):
    return render(request, "Addcategories.html")
def add_products(request):
    cat = Category_Db.objects.all()
    return render(request, "AddProducts.html", {'cat':cat})
def save_category(request):
    if request.method=="POST":
        cat = request.POST.get('category')
        desc = request.POST.get('description')
        img = request.FILES['image']
        obj = Category_Db(Category_Name=cat, Description=desc, Category_Image=img)
        obj.save()
        return redirect(add_categories)
def display_category(request):
    cat = Category_Db.objects.all()
    return render(request, "Display_Category.html", {'cat':cat})
def edit_category(request, cat_id):
    cat = Category_Db.objects.get(id=cat_id)
    return render(request,"Edit_Category.html", {'cat':cat})
def update_category(request, cat_id):
    if request.method=="POST":
        cat = request.POST.get('category')
        desc = request.POST.get('description')
        try:
             img = request.FILES['image']
             fs = FileSystemStorage()
             file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Category_Db.objects.get(id=cat_id).Category_Image
        Category_Db.objects.filter(id=cat_id).update(Category_Name=cat, Description=desc, Category_Image=file)
        return redirect(display_category)

def login_page(request):
    return render(request, "Admin_login.html")
def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pswd)
            if user is not None:
                login(request, user)
                return  redirect(index_page)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)