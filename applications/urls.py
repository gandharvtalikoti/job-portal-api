from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ApplicantViewSet,
    JobViewSet,
    apply_for_job,
    ApplicationListView,
    ApplicationUpdateView
)

router = DefaultRouter()
router.register(r'applicants', ApplicantViewSet, basename='applicant')
router.register(r'jobs', JobViewSet, basename='job')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/apply/', apply_for_job, name='apply'),
    path('api/applications/', ApplicationListView.as_view(), name='applications-list'),
    path('api/applications/<int:pk>/', ApplicationUpdateView.as_view(), name='applications-update'),
]
