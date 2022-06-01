from django.urls import re_path
from .views import FileView, FileViewTour

urlpatterns = [
    re_path(r'upload', FileView.as_view(), name='file-upload'),
    re_path(r'upload_tour', FileViewTour.as_view(), name='file-upload-tour'),

]
