from rest_framework import generics, status
from rest_framework.response import Response
from . import models
from .serializers import VacancySerializer, CompanySerializer
from django.shortcuts import get_object_or_404

class ListCompanies(generics.ListAPIView):
    queryset = models.Company.objects.all()
    serializer_class = CompanySerializer

class RetrieveCompany(generics.RetrieveAPIView):
    queryset = models.Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'

class ListCompanyVacancies(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs.get('id')
        return models.Vacancy.objects.filter(company_id=company_id)

class ListVacancies(generics.ListAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = VacancySerializer

class RetrieveVacancy(generics.RetrieveAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = VacancySerializer
    lookup_field = 'id'

class TopTenVacanciesList(generics.ListAPIView):
    queryset = models.Vacancy.objects.order_by('-salary')[:10]
    serializer_class = VacancySerializer

