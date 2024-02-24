from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def search(request):
    return render(request,'search.html')
def packages(request):
    return render(request,'packages.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')
def Testimonial(request):
    return render(request,'Testimonial.html')