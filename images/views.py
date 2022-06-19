import operator
from functools import reduce

from django.core.mail import send_mail
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status, request, generics, filters, viewsets, mixins

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import File, Tour, Work
from .serializers import FileSerializer, FileSerializerTour, FileSerializerWork, FileSerializerContact


class StudySearchSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get_queryset(self):
        text = self.request.query_params.get('passport_number', None)
        # if not text:
        #     return self.queryset
        # else:
        text_seq = text.split(' ')
        text_qs = reduce(operator.and_,
                         (Q(passport_number__icontains=x) for x in text_seq))
        return self.queryset.filter(text_qs)


class TourSearchSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Tour.objects.all()
    serializer_class = FileSerializerTour

    def get_queryset(self):
        text = self.request.query_params.get('passport_number', None)
        # if not text:
        #     return self.queryset
        # else:
        text_seq = text.split(' ')
        text_qs = reduce(operator.and_,
                         (Q(passport_number__icontains=x) for x in text_seq))
        return self.queryset.filter(text_qs)


class WorkSearchSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Work.objects.all()
    serializer_class = FileSerializerWork

    def get_queryset(self):
        text = self.request.query_params.get('passport_number', None)
        # if not text:
        #     return self.queryset
        # else:
        text_seq = text.split(' ')
        text_qs = reduce(operator.and_,
                         (Q(passport_number__icontains=x) for x in text_seq))
        return self.queryset.filter(text_qs)


# class PurchaseList(generics.ListAPIView):
#     queryset = File.objects.all()
#     serializer_class = FileSerializer
#     filter_backends = (DjangoFilterBackend,SearchFilter)
#     filter_fields = ('name')
#     search_fields = ('name')
# serializer_class = TrackStudySerializer

# def get_queryset(self):
#     """
#     Optionally restricts the returned purchases to a given user,
#     by filtering against a `username` query parameter in the URL.
#     """
#     queryset = File.objects.all()
#     name = self.request.query_params.get('name')
#     if name is not None:
#         queryset = queryset.filter(name=name)
#     return queryset


class SearchAPIView(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        search_fields = ['passport']
        filter_backends = (filters.SearchFilter,)
        queryset = File.objects.all()
        file_serializer = FileSerializer(queryset, many=True)
        # return a Json response
        return JsonResponse(file_serializer.data, safe=False)


class FileViewGet(APIView):
    def get(self, request, format=None):
        files = File.objects.all()
        # serialize the task data
        file_serializer = FileSerializer(files, many=True)
        # return a Json response
        return JsonResponse(file_serializer.data, safe=False)


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    http_method_names = ['get', 'head', 'post']

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        # JsonResponse(request.data)
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileViewTourGet(APIView):
    def get(self, request, format=None):
        files = Tour.objects.all()
        # serialize the task data
        file_serializer = FileSerializerTour(files, many=True)
        # return a Json response
        return JsonResponse(file_serializer.data, safe=False)


class FileViewTour(APIView):
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'head', 'post']

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializerTour(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileViewWorkGet(APIView):
    def get(self, request, format=None):
        files = Work.objects.all()
        # serialize the task data
        file_serializer = FileSerializerWork(files, many=True)
        # return a Json response
        return JsonResponse(file_serializer.data, safe=False)


class FileViewWork(APIView):
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'head', 'post']

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializerWork(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileViewContact(APIView):
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'head', 'post']

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializerContact(data=request.data)
        # send_mail('Poland Embassy',
        #           'Your request has been sent successfully. Our employee will solve your request as soon as possible',
        #           'syedamar.abbas555@gmail.com',
        #           ['syedamer.abbas555@gmail.com'],
        #           fail_silently=False
        #           )
        if file_serializer.is_valid():
            file_serializer.save()
            return JsonResponse(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
