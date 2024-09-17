from django.db import models
from django.contrib.auth.models import User

# Item Model
class Item(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('clothes', 'Clothes'),
        ('books', 'Books'),
        ('other', 'Other')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)  # Who donated this item

    def __str__(self):
        return self.name

# Institution Model (e.g., Educational Institutions, Orphanages, Old Age Homes)
class Institution(models.Model):
    INSTITUTION_TYPE_CHOICES = [
        ('education', 'Educational Institution'),
        ('old_age', 'Old Age Home'),
        ('orphanage', 'Orphanage'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=INSTITUTION_TYPE_CHOICES)
    address = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

# Sponsorship Model
class Sponsorship(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(User, on_delete=models.CASCADE)
    date_sponsored = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sponsorship of {self.item.name} by {self.sponsor.username}"

# Chat Model
class Chat(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.user.username} with {self.institution.name}"
