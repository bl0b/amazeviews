import scrapy
from amazeviews.util import extract_items, find_link_to_next_page

__author__ = 'damien'


class Reviews(scrapy.Spider):
    name = "reviews"

    def make_url(self, source_url, url):
        if url.startswith('http'):
            return url

        return '/'.join(source_url.split('/')[:3]) + url

    def start_requests(self):
        books = getattr(self, 'book', None).split(',')
        tlds = getattr(self, 'tld', 'com,co.uk,de,fr,es,it,nl,co.jp,com.br,ca,com.mx,com.au,in').split(',')
        for book in books:
            for tld in tlds:
                url = ('https://www.amazon.%s/product-reviews/%s/%s'
                       % (tld, book, 'ref=cm_cr_arp_d_show_all?ie=UTF8&reviewerType=all_reviews'))
                yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        url = response.url
        print "Parsing", url
        for i in extract_items(self, response):
            yield i
        next_page = find_link_to_next_page(response)
        if next_page:
            yield scrapy.Request(self.make_url(response.url, next_page), callback=self.parse)
