from django.urls import path
from myapp.views import index, contacts, indexItem

urlpatterns = [
    # http://127.0.0.1:8000/myapp/
    path('', index),
    path('<int:id>/', indexItem),
    # http://127.0.0.1:8000/hello/contacts/
#     path('contacts/', contacts),
]
