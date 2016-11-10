from __future__ import unicode_literals
from django import forms
from django.db import models

# Create your models here.
from django.forms import ModelForm


class User(models.Model):

    username = models.CharField(primary_key=True, max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    upload_date = models.DateTimeField(auto_now_add=True)
    confirm_password = models.CharField(max_length=64)
    type = models.BooleanField(default=False)


    def __unicode__(self):
        return str(self.username)

    def clean_username(self):
        user = self.cleaned_data['username']
        user_validation = User.objects.get(username=user)
        return user

    def clean_password(self):
        pwd = self.cleaned_data['password']
        return pwd


class SignUpForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']


class Restaurant(models.Model):

    restaurant_name = models.CharField(max_length=64, primary_key=True)
    tag = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    upload_date = models.DateTimeField(auto_now_add=True)
    picture_location = models.CharField(max_length=256)


class Comments(models.Model):

    comment_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=512)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)


class UploadRestaurantForm(ModelForm):

    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'tag', 'address', 'description']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

    def clean_username(self):
        user_name = self.cleaned_data['username']
        return user_name

    def clean_password(self):
        pwd = self.cleaned_data['password']
        return pwd



