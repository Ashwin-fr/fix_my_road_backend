from django.db import models
from django.contrib.auth.models import User

# schema => Issue 
# fields => owner (FK to User), title, description, image, location, status, created_at, updated_at, category.

# schema => StillPresent
# fields => owner (FK to User), issue (FK to Issue), created_at.  

class Issue(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    ]

    CATEGORY_CHOICES = [
        ('pothole', 'Pothole'),
        ('streetlight', 'Streetlight'),
        ('garbage', 'Garbage'),
        ('drainage', 'Drainage'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='issues')
    
    title = models.CharField(max_length=100)
    
    description = models.TextField()
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    image = models.ImageField(upload_to='issues/', blank=True, null=True)
    
    location = models.CharField(max_length=255, blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def still_present_count(self):
       
        return self.stillpresent_set.count()

    def __str__(self):
       
        return self.title


class StillPresent(models.Model):
   
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
   
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
   
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
       
        unique_together = ('owner', 'issue')  # Prevent duplicate “still present” from same user

    def __str__(self):
       
        return f"{self.user.username} marked {self.issue.title}"
