from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import *
from .forms import CustomAdmin

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "timestamp", "text", "img", "post_id")
    form = CustomAdmin


admin.site.register(model_or_iterable=Post, admin_class=PostAdmin)

