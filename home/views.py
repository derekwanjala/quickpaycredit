from email.mime import image
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . models import FAQ, ContactForm, ContactMessage, Service, Slider, About, Vision

def home(request):
    services = Service.objects.order_by('-created')[:6]
    slider = Slider.objects.all
    about = About.objects.all()
    return render(request, 'index.html', {'slider': slider, 'services': services, 'about': about})


def about(request):
    about = About.objects.all
    vision = Vision.objects.all
    services = Service.objects.order_by('-created')[:6]
    return render(request, 'about.html', {'about': about, 'vision': vision, 'services': services})


def service(request):
    services = Service.objects.all()
    about = About.objects.all()
    return render(request, 'service.html', {'services': services, 'about': about})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    about = About.objects.all()
    return render(request, 'service_detail.html', {'service': service, 'about': about})


def contact(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.first_name = form.cleaned_data['first_name']  # get form input data
            data.last_name = form.cleaned_data['last_name']  # get form input data
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(
                request, "Your message has been sent. Thank you for your message! We'll reach out as soon as possible.")
            return HttpResponseRedirect('/contact')
    form = ContactForm
    about = About.objects.all()
    services = Service.objects.order_by('-created')[:6]
    return render(request, 'contact.html', {'form': form, 'about': about, 'services': services})


def faq(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.first_name = form.cleaned_data['first_name']  # get form input data
            data.last_name = form.cleaned_data['last_name']  # get form input data
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(
                request, "Your message has been sent. Thank you for your message! We'll reach out as soon as possible.")
            return HttpResponseRedirect('/contact')
    faq = FAQ.objects.all()
    form = ContactForm
    about = About.objects.all()
    services = Service.objects.order_by('-created')[:6]
    return render(request, 'faq.html', {'faq': faq, 'form': form, 'about': about, 'services': services})

