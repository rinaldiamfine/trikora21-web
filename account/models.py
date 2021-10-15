from django.db import models
from django.utils import timezone
import os, random
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
# from global_data.models import Template, Language

GENDER_CHOICES = (
    ('n', 'Not Selected'),
	('m', 'Male'),
	('f', 'Female'),
)
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address!")
        if not password:
            raise ValueError("Users must have a password!")
        
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user
    
class User(AbstractBaseUser):
    email       = models.EmailField(max_length=50, unique=True)
    username    = models.CharField(max_length=50, null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)
    admin       = models.BooleanField(default=False)
    staff       = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_staff(self):
        return self.staff

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    instance_name = instance._meta.object_name
    model_id = instance.id
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image_assets/{instance_name}/{model_id}/{final_filename}".format(instance_name=instance_name, model_id=str(model_id), final_filename=final_filename)

@receiver(post_save, sender=User)
def create_profile_user(sender, instance, created, **kwargs):
    if created:
        user_email = instance.email
        profile_name = user_email.split('@')[0].replace('-', ' ').replace('.', ' ')
        email = user_email
        capitalize_profile_name = profile_name.capitalize()
        Profile.objects.create(profile_user=instance, name=capitalize_profile_name, active=True)
    
class Profile(models.Model):
    name            = models.CharField(max_length=50, null=True, blank=True)
    title           = models.CharField(max_length=50, null=True, blank=True)
    photo           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    phone           = PhoneNumberField(blank=True)
    email           = models.EmailField(max_length=50, blank=True)
    active          = models.BooleanField(default=True)
    profile_user    = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio             = models.TextField(blank=True)
    # template        = models.ForeignKey(Template, on_delete=models.SET_NULL, blank=True, null=True)
    #ADDRESS
    street          = models.CharField(max_length=50, null=True, blank=True)
    street2         = models.CharField(max_length=50, null=True, blank=True)
    zip             = models.CharField(max_length=10, null=True, blank=True)

    birthday        = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    gender          = models.CharField(max_length=5, choices=GENDER_CHOICES, null=True, blank=True)

    # languages       = models.ManyToManyField(Language)


    #SOFTSKILLS -> SKILL (SOFT) -> VALUE
    #EDUCATION HISTORY -> SCHOOL -> START - FINISH - DESCRIPTION
    #WORK EXPERIENCE -> COMPANY -> START - FINISH - DESCRIPTION
    #PROFESSIONAL AND SKILLS -> SKILL (PROFESSIONAL) -> VALUE 
    #LANGUAGES M2M
    #HOBBIES M2M

    def __str__(self):
        return self.name

    # def __name__(self):
    #     return "Profile"