from django.contrib.auth import authenticate, login, logout
from django.db.models import Count, Sum
from django.views import View
from django.shortcuts import render, redirect
from .models import Category, Donation, Institution, User


class LandingPage(View):
    template_name = "giving_gifts_app/index.html"

    def get(self, request, *args, **kwargs):
        quantity_bag = Donation.objects.all().aggregate(Sum('quantity'))
        quantity_institution = Donation.objects.all().aggregate(Count('institution', distinct=True))
        foundations = Institution.objects.filter(type=1)
        organizations = Institution.objects.filter(type=2)
        collections = Institution.objects.filter(type=3)
                
        context = {
            "quantity_bag": quantity_bag["quantity__sum"],
            "quantity_institution": quantity_institution["institution__count"],
            "foundations": foundations,
            "organizations": organizations,
            "collections": collections,
        }
        return render(request, self.template_name, context)


class AddDonation(View):
    def get(self, request):
        return render(request, "giving_gifts_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "giving_gifts_app/login.html")

    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(self.request, user)
            return redirect('/')
        else:
            return redirect('/register/')

class Logout(View):
        def get(self, request):
            logout(request)
            return redirect('/login/')


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, "giving_gifts_app/register.html")

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        #additionally do a validation in javascript
        if password == password2 and len(password)>=8 and hasNumbers(password):
            User.objects.create_user(email = email, password = password, first_name= first_name, last_name = last_name)
        return redirect('/login/')


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
