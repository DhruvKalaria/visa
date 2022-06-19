from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from .views import FileView, FileViewTour, FileViewWork, SearchAPIView, FileViewGet, FileViewTourGet, FileViewWorkGet, \
    FileViewContact, StudySearchSet, TourSearchSet, WorkSearchSet

router = routers.DefaultRouter()
router.register('search',StudySearchSet,basename='search-study')
router.register('searchTour',TourSearchSet,basename='search-tour')
router.register('searchWork',WorkSearchSet,basename='search-work')

urlpatterns = [
    path('',include(router.urls)),
    url(r'study/search', SearchAPIView.as_view(), name='search'),
    url(r'upload', FileView.as_view(), name='file-upload'),
    url(r'student/get', FileViewGet.as_view(), name='file-upload'),
    url(r'study/<int:pk>/', FileView.as_view(), name='file-upload'),
    url(r'study/(?P<passport>.+)/$', FileView.as_view(), name='file-upload'),
    url(r'tour', FileViewTour.as_view(), name='file-upload-tour'),
    url(r'visit/get', FileViewTourGet.as_view(), name='file-upload'),
    url(r'tour/<int:pk>/', FileViewTour.as_view(), name='file-upload-tour'),
    url(r'work', FileViewWork.as_view(), name='file-upload-work'),
    url(r'contact', FileViewContact.as_view(), name='file-upload-contact'),
    url(r'business/get', FileViewWorkGet.as_view(), name='file-upload'),
    url(r'work', FileViewWork.as_view(), name='file-upload-work'),

]

app_name = 'images'
