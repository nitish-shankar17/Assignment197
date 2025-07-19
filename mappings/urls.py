from django.urls import path
from . import views

urlpatterns = [
    path('', views.MappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:pk>/', views.MappingDetailView.as_view(), name='mapping-detail'),
    path('<int:patient_id>/', views.PatientDoctorsView.as_view(), name='patient-doctors'),
]