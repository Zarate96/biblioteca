from django.urls import path
from .views import *

urlpatterns = [
    path('create_author/', createAuthor, name="createAuthor"),
    path('list_author/', listAuthor, name="listAuthor"),
    path('update_author/<int:id>', updateAuthor, name="updateAuthor"),
    path('delete_author/<int:id>', deleteAuthor, name="deleteAuthor"),
]
