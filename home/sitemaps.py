from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'home:home',
            'about',
            'quickpayloans',
            'quickpayloans/<slug:slug>',
            'contact',
            'faq',
        ]

    def location(self, item):
        return reverse(item)