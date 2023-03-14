from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
from django.urls import reverse


class Company(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    mobile = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    image = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    status=models.CharField(max_length=10,choices=STATUS)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.title

class Service(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    short_detail = models.CharField(max_length=500)
    detail = RichTextUploadingField(blank=True)
    icon = models.ImageField(upload_to='images/')
    icon_alt = models.CharField(max_length=160)    
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Services'
    
    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=160)
    detail = RichTextUploadingField(blank=True)
    short_detail = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title

class Slider(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    hero_text = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hero_text


class Vision(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_detail = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Vision'

    def __str__(self):
        return self.title
    


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=20)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'}),
        }


class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    question_number = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'FAQs'
    
    def __str__(self):
        return self.question
