from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('<int:record_id>', views.news, name="record"),
    path('add', views.create_record, name="create-record"),
    path('my', views.my_records, name="my-records"),
    path('edit/<int:record_id>', views.edit_record, name="edit-record"),
    path('delete/<int:record_id>', views.delete_record, name="delete-record")
]
