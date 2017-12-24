from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', Mainpage, name="Home_page"),
    path('post/<post_id>', Postpage, name="Post_page"),
    path('about', About, name="About_page"),
    path('pics', Pictures, name="Pictures_page"),
    path('contacts', Contacts, name="Contacts_page")
]  # + [static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)]

