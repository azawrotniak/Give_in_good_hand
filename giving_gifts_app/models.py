from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField  # https://github.com/stefanfoulis/django-phonenumber-field

TYPE_INSTITUTION = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=128)
    type = models.IntegerField(choices=TYPE_INSTITUTION, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = PhoneNumberField(null=False, blank=False, unique=False)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=5)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=128, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )


    def __str__(self):
        return f"{self.user} -> {self.institution}"