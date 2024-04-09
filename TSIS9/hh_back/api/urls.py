from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('companies/', views.ListCompanies.as_view(), name='list_companies'),
    path('companies/<int:id>/', views.RetrieveCompany.as_view(), name='retrieve_company'),
    path('companies/<int:id>/vacancies/', views.ListCompanyVacancies.as_view(), name='company_vacancies_list'),
    path('vacancies/', views.ListVacancies.as_view(), name='list_vacancies'),
    path('vacancies/<int:id>/', views.RetrieveVacancy.as_view(), name='retrieve_vacancy'),
    path('vacancies/top_ten/', views.TopTenVacanciesList.as_view(), name='top_ten_vacancies_list'),
]