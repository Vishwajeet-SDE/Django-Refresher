from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Student(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('alumni', 'Alumni'),
    )

    # 🔹 Basic Info
    student_id = models.CharField(
        max_length=20,
        unique=True,
        db_index=True
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    # 🔹 Contact Info
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Enter a valid phone number."
            )
        ]
    )

    address = models.TextField(blank=True)

    # 🔹 Academic Info
    course = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    enrollment_date = models.DateField(default=timezone.now)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    # 🔹 System Fields
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
