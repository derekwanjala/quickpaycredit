from django.contrib import admin

from .models import FAQ, Company, ContactMessage, Service, About, Slider, Vision

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company', 'mobile', 'email', 'status', 'created']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'created']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['subtitle', 'hero_text', 'status', 'created']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'subject', 'created', 'status']
    readonly_fields = ('first_name', 'last_name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'status']


@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_detail']
