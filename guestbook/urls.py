from django.contrib import admin
from django.urls import path
import visitor.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', visitor.views.guestbook, name='guestbook'),
    path('submit/',visitor.views.submit, name='submit'),
]
