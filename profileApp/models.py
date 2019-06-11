from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


class Address(models.Model):
    street_address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6)
    country = models.CharField(max_length=256)
    
    def __str__(self):
        return self.street_address


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    gender_choice = [
        (MALE,'Male'),
        (FEMALE,'Female'),
        (OTHER,'Other')
    ]
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=14)
    gender = models.CharField(max_length=1,
    choices = gender_choice,default=MALE)
    profile_pic = models.ImageField(upload_to='images/')
    date_birth = models.DateTimeField()
    permanent_address = models.OneToOneField(
        Address, on_delete = models.CASCADE,primary_key=True,)
    company_address = models.OneToOneField(Address,
    on_delete = models.CASCADE,related_name='comapny_address')
    friends = models.ManyToManyField('Profile',blank=True)

    def __str__(self):
        return self.name


