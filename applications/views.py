from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny


from .models import Applicant, Job, Application
from .serializers import ApplicantSerializer, JobSerializer, ApplicationSerializer


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all().order_by('-applied_on')
    serializer_class = ApplicantSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]  # enables ?search=
    search_fields = ['name', 'email']  # search by name or email


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_on')
    serializer_class = JobSerializer
    permission_classes = [AllowAny]


class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all().order_by('-applied_on')
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]


class ApplicationUpdateView(APIView):
    permission_classes = [AllowAny]

    def patch(self, request, pk):
        app = get_object_or_404(Application, pk=pk)
        serializer = ApplicationSerializer(app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def apply_for_job(request):
    """
    POST /api/apply/
    Expected JSON: { "applicant": applicant_id, "job": job_id }
    """
    serializer = ApplicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
