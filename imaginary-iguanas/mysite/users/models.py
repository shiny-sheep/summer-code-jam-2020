from django.contrib.auth.models import User
from django.db import models


class UserProfile(User):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("D", "Other")
    )

    image = models.ImageField(default="default_pfp.jpg", upload_to="profile_pics")
    gender = models.CharField(null=True, max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(null=True, max_length=2, help_text="ISO 639 country code.")
    city = models.CharField(null=True, max_length=50)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return f"{self.username} profile."
