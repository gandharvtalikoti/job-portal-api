from django.db import models


# 1️⃣ Applicant Model
class Applicant(models.Model):
    name = models.CharField(max_length=100)  # applicant's full name
    email = models.EmailField(unique=True)   # unique email, acts like an ID
    phone = models.CharField(max_length=15, blank=True, null=True)  # optional phone number
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # optional file upload
    applied_on = models.DateTimeField(auto_now_add=True)  # automatically stores when created

    def __str__(self):
        # when we print the object, it shows nicely like "Alice <alice@email.com>"
        return f"{self.name} <{self.email}>"


# 2️⃣ Job Model
class Job(models.Model):
    title = models.CharField(max_length=100)  # job title
    description = models.TextField()          # details about the job
    posted_on = models.DateTimeField(auto_now_add=True)  # auto timestamp when job is added

    def __str__(self):
        return self.title


# 3️⃣ Application Model
class Application(models.Model):
    # status choices define what phase an application is in
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
    ]

    applicant = models.ForeignKey(
        Applicant,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='applied'
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # This line ensures that the same applicant cannot apply to the same job twice
        constraints = [
            models.UniqueConstraint(fields=['applicant', 'job'], name='unique_applicant_job')
        ]

    def __str__(self):
        # readable string when printed, ex: "alice@email.com -> Backend Dev (applied)"
        return f"{self.applicant.email} -> {self.job.title} ({self.status})"
