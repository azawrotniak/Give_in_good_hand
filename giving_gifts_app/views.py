from django.views import View
from django.shortcuts import render


# Create your views here.
class LandingPage(View):
    def get(self, request):
        return render(request, "giving_gifts_app/index.html")


class AddDonation(View):
    def get(self, request):
        return render(request, "giving_gifts_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "giving_gifts_app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "giving_gifts_app/register.html")