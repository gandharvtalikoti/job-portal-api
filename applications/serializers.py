from rest_framework import serializers
from .models import Applicant, Job, Application


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['id', 'name', 'email', 'phone', 'resume', 'applied_on']
        read_only_fields = ['id', 'applied_on']  # these are auto-generated, so users can’t edit them


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'posted_on']
        read_only_fields = ['id', 'posted_on']


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.PrimaryKeyRelatedField(queryset=Applicant.objects.all())
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())

    class Meta:
        model = Application
        fields = ['id', 'applicant', 'job', 'status', 'applied_on']
        read_only_fields = ['id', 'applied_on']

    def validate(self, attrs):
        """
        Custom validation:
        - Prevent duplicate applications (same applicant applying for same job)
        """
        applicant = attrs.get('applicant')
        job = attrs.get('job')

        # only check for duplicates if this is a new application (not an update)
        if self.instance is None and Application.objects.filter(applicant=applicant, job=job).exists():
            raise serializers.ValidationError("This applicant has already applied for this job.")

        return attrs
