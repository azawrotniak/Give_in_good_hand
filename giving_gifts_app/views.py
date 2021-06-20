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


class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, "giving_gifts_app/register.html")

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')




