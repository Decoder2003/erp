from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager 
from django.utils import timezone
from django.utils.timezone import now

INFINITE = 4294967295

class User(AbstractUser):    
    class type(models.TextChoices):
        student = "STUDENT", "student"
        staff = "STAFF", "staff"
        alumni = "ALUMNI", "alumni"
    username = None
    user_image = models.ImageField(upload_to='userImages/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    summary = models.TextField(max_length=250)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=100)
    role = models.CharField(choices=type.choices, default=type.student, max_length=10)
    phone_number = models.IntegerField(null=True,unique=True)

    # for backend functionality and for logs
    rp_token = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_logged = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class institution(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class degree(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class field_of_study(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class education(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(institution, on_delete=models.CASCADE)
    field_of_study = models.ForeignKey(field_of_study, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now, null=True)
    def __str__(self):
        return f"{self.id}"

class feed(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content  = models.TextField(max_length=INFINITE)
    time_stamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.id}"
    
class image(models.Model):
    feedId = models.ForeignKey(feed, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to="feedImages/", default="null")
    def __str__(self):
        return f"{self.id}"

class interaction(models.Model):
    class type(models.TextChoices):
        like = "LIKE", "like"
        comment = "COMMENT", "comment"
        share = "SHARE", "share"
    feedId = models.ForeignKey(feed, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    interaction_type = models.CharField(choices=type.choices, max_length=10)
    def __str__(self):
        return f"{self.id}"
    
class group(models.Model):
    name = models.CharField(max_length=100)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    description = models.TextField(max_length=250)
    image_url = models.ImageField(upload_to="groupImages/", default="null")
    def __str__(self):
        return f"{self.id}"

class group_membership(models.Model):
    groupId = models.ForeignKey(group, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id}"    

class post(models.Model):
    groupId = models.ForeignKey(group, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=INFINITE)
    time_stamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.id}"

class event(models.Model):
    groupId = models.ForeignKey(group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=INFINITE)
    time_stamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.id}"