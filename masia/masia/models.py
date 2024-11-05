from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    name = models.CharField(max_length=150)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Activité"
        verbose_name_plural = "Activités"

class City(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ville"
        verbose_name_plural = "Villes"

class Entrepreneur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tagline = models.CharField("Titre", max_length=75, null=True, blank=True)
    avg_rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    photo = models.FileField(
        upload_to="entrepreneurs/photos", default="entrepreneurs/photos/avatar.png"
    )

    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    wphone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    waddress = models.TextField(blank=True, null=True)
    logo = models.FileField(
        upload_to="entrepreneurs/logos",
        default="entrepreneurs/logos/avatar.png",
        null=True,
        blank=True,
    )
    stamp = models.FileField(
        upload_to="entrepreneurs/stamps",
        null=True,
        blank=True,
    )
    verified = models.BooleanField(default=False)
    rfq = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    projects = models.IntegerField(default=0)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = "Entrepreneur"
        verbose_name_plural = "Entrepreneurs"

class RequestForQuote(models.Model):
    entrepreneur = models.ForeignKey(
        Entrepreneur, on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(default="")
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Demande de devis"
        verbose_name_plural = "Demandes de devis"
