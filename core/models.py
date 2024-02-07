from django.db import models

# Create your models here.

class WaitlistEmail(models.Model):
    email = models.CharField(max_length=130, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Waitlist Emails"

    def __str__(self):
        return self.email