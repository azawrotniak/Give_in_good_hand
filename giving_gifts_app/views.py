from django.db.models import Count, Sum
from django.views import View
from django.shortcuts import render
from .models import Category, Donation, Institution

# Create your views here.
class LandingPage(View):
    template_name = "giving_gifts_app/index.html"

    def get(self, request, *args, **kwargs):

        quantity_bag = Donation.objects.all().aggregate(Sum('quantity'))

        quantity_institution = Donation.objects.all().aggregate(Count('institution', distinct=True))
        
        context = {
            "quantity_bag": quantity_bag["quantity__sum"],
            "quantity_institution": quantity_institution["institution__count"],
        }
        return render(request, self.template_name, context)


class AddDonation(View):
    def get(self, request):
        return render(request, "giving_gifts_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "giving_gifts_app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "giving_gifts_app/register.html")