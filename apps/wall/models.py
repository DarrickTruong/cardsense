from __future__ import unicode_literals
from django.db import models
import re
from apps.login_register.models import User
from django.core.files.storage import FileSystemStorage

# Create your models here
class LeadManager(models.Manager):
    def validate(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be longer than 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be longer than 2 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        return errors

class LoyaltyManager(models.Manager):
    def validate(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be longer than 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be longer than 2 characters"
        if not email_regex.match(postData['email']):
            errors['email'] = 'Invalid email address!'
        return errors

class EventsManager(models.Manager):
    def validate(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(postData['what']) < 2:
            errors['what'] = "Please provide more information"
        if len(postData['where']) < 2:
            errors['where'] = "Please provide a location"
        if len(postData['when']) < 2:
            errors['when'] = "Please provide an event date"
        if len(postData['why']) < 2:
            errors['why'] = "Please provide a description for your event"
        
        return errors



# Need to Migrate
class Loyalty(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=12, blank=True)
    owner = models.ForeignKey(User, related_name='loyal_client', on_delete=models.CASCADE)
    objects = LoyaltyManager()
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review = models.TextField()
    author = models.ForeignKey(Loyalty, related_name='written_review', on_delete=models.CASCADE)
    user_reviewed = models.ForeignKey(User, related_name= 'my_review', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Lead(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=12, blank=True)
    owner = models.ForeignKey(User, related_name='my_lead', on_delete=models.CASCADE)
    objects = LeadManager()
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message = models.TextField()
    user_messaged = models.ForeignKey(User, related_name= 'messages', on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)
    author = models.ForeignKey(Lead, related_name='message_written', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
            return f"<Wizard object: {self.message} {self.user_messaged} {self.pinned} {self.author} {self.written_comment} ({self.id})>"

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name= 'comments', null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='my_comment', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __repr__(self):
            return f"<Wizard object: {self.comment} {self.message} {self.author} ({self.id})>"








event_pic = FileSystemStorage(location='/media')

class Event(models.Model):
    what = models.CharField(max_length=45)
    where = models.CharField(max_length=45)
    when = models.DateTimeField()
    why = models.TextField()
    owner = models.ForeignKey(User, related_name='my_event', null=True, on_delete=models.CASCADE)
    objects = EventsManager()
    event_pic = models.ImageField(upload_to='event_pic', null=True) 
    created_at = models.DateTimeField(auto_now_add=True)