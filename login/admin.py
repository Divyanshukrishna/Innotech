from django.contrib import admin
from login.models import data,UploadedImage
# Register your models here.

admin.site.register(data) 

admin.site.register(UploadedImage)
