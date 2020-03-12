from __future__ import unicode_literals
from django.db import models
import re
from django.core.files.storage import FileSystemStorage 

# Create your models here
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        phone_regex = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be longer than 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be longer than 2 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        if not phone_regex.match(postData['phone']):
            errors['phone'] = 'Phone is not in the right format'
        if len(postData['birthday']) < 2:
            errors['birthday'] = "Birthday must be longer than 2 characters"
        if len(postData['password']) < 4:
            errors['password'] = "Password should be at least 4 characters"
        if postData['password'] != postData['password_confirm']:
            errors['password_confirm'] = 'Password does not match. Try Again'
            # Checking unique email
        all_users = User.objects.all()
        if len(all_users.filter(email=postData['email'])) > 0:
            errors['email'] = 'This email address already exists'
        return errors

    def socialvalidate(self, postData):
        errors = {}
        if len(postData['linkedin']) < 2:
            errors['linkedin'] = "Linkedin must be longer than 2 characters"
        if len(postData['facebook']) < 2:
            errors['facebook'] = "facebook must be longer than 2 characters"
        if len(postData['instagram']) < 2:
            errors['instagram'] = "instagram must be longer than 2 characters"
        if len(postData['website']) < 2:
            errors['website'] = "website must be longer than 2 characters"
        return errors
    
    def edit_validate(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        phone_regex = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
        website_regex_short = re.compile(r'^[a-zA-Z]+\.[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
        website_regex_long = re.compile(r'^[a-zA-Z]+\.[a-zA-Z0-9.+_-]+\.[a-zA-Z]+\/[a-zA-Z0-9.+_-]+$')
        linkedin_regex = re.compile(r'^[a-zA-Z]+\/[a-zA-Z0-9.+_-]+$')
        facebook_regex = re.compile(r'^[a-zA-Z0-9.+_-]+$')
        instagram_regex = re.compile(r'^[a-zA-Z0-9.+_-]+$')
        
        
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be longer than 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be longer than 2 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        if not phone_regex.match(postData['phone']):
            errors['phone'] = 'Phone is not in the right format'
        if len(postData['birthday']) < 2:
            errors['birthday'] = "Birthday must be longer than 2 characters"
        if not website_regex_long.match(postData['website']) and not website_regex_short.match(postData['website']):
            errors['website'] = "Please provide a website like www.website.com or www.website.com/example"
        if not linkedin_regex.match(postData['linkedin']):
            errors['linkedin'] = "Please provide 'in/firstname-lastname' or 'company/firstname-lastname from your linkedin url"
        if not facebook_regex.match(postData['facebook']):
            errors['facebook'] = "Please provide '/firstname.lastname' or '/businessname from your facebook url"
        if not instagram_regex.match(postData['instagram']):
            errors['instagram'] = "Please provide '@username from your instagram account"
        return errors


profile_pics = FileSystemStorage(location='/static/media')

class User(models.Model):
    first_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
    email = models.CharField(max_length=45, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(null=True)
    password = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    objects = UserManager()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    google = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    def __repr__(self):
            return f"<Wizard object: {self.first_name} ({self.id})>"

