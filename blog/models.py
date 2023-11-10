from django.db import models
from static import images
# Create your models here.


class Main(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images")
    icon = models.FileField(upload_to="images")


class Settings(models.Model):
    sevice_title = models.CharField(max_length=200)
    service_description = models.TextField(blank=True, null=True)

    mics_title = models.CharField(max_length=120)
    mics_description = models.TextField(blank=True, null=True)

    clint_command = models.CharField(max_length=120)
    clint_command_description = models.TextField(blank=True, null=True)


class Service(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images")


class About(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images")


class Mics(models.Model):
    image = models.FileField(upload_to="")
    mics_link = models.URLField(max_length=200)


class Comments(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)


class CallBack(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)

    input_name = models.CharField(max_length=200)
    input_email = models.CharField(max_length=150)
    input_phone = models.IntegerField(blank=True, null=True)
    input_comment = models.TextField(blank=True, null=True)


class Contact(models.Model):
    icon = models.FileField(upload_to="images")
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    facebook_icon = models.FileField(upload_to="images")
    facebook_link = models.URLField(max_length=200)

    twitter_icon = models.FileField(upload_to="images")
    twitter_link = models.URLField(max_length=200)

    instagram_icon = models.FileField(upload_to="images")
    instagram_link = models.URLField(max_length=200)

    email_subscribe = models.CharField(max_length=200)

    info_title = models.CharField(max_length=200)
