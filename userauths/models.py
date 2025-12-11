from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField
import shortuuid
from django.db.models.signals import post_save


MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other")
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)


IDENTITY_TYPE = (
    ("national_id_card", "National ID Card"),
    ("drivers_licence", "Drives Licence"),
    ("international_passport", "International Passport")
)


class User(AbstractUser):
    uid = ShortUUIDField(length=10, max_length=10, alphabet=shortuuid.get_alphabet())
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    pid = ShortUUIDField(length=10, max_length=10, alphabet=shortuuid.get_alphabet())
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    
    image = models.ImageField(upload_to="image", default='avatar.png')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    verified = models.BooleanField(default=False)
    
    # KYC
    marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40)
    gender = models.CharField(choices=GENDER, max_length=40)
    identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140)
    identity_image = models.ImageField(upload_to="kyc", null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    # Address
    current_address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # Contact Detail
    mobile = models.CharField(max_length=1000)
    fax = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)    


class Complain(models.Model):
    cid = ShortUUIDField(length=10, max_length=10, alphabet=shortuuid.get_alphabet())
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering = ['-date']
    
