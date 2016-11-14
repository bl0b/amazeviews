__author__ = 'damien'

from items import Review


def find_reviews(response):
    return response.css('.a-section.review')


def find_link_to_next_page(response):
    return response.xpath('//*[text()="Next"]/@href').extract_first()


def get_author_name(review):
    return review.xpath('descendant-or-self::node()//*[contains(@class, "author")]/text()').extract_first()


def get_author_url(review):
    return review.xpath('descendant-or-self::node()//*[contains(@class, "author")]/@href').extract_first()


def get_rating(review):
    return int(review.css('i[data-hook=review-star-rating]::attr(class)').re('a-star-([1-5])')[0])


def get_text(review):
    return '\\n'.join(review.css('[class~=review-text]::text').extract())


def get_id(review):
    return review.xpath('@id').extract_first()


def get_tld(response):
    return response.url.split('/')[2].split('amazon.')[-1]


def get_book_id(response):
    return response.url.split('/')[-2]


def make_item(spider, response, review):
    ret = Review()
    ret['amz_id'] = get_id(review)
    ret['author_name'] = get_author_name(review)
    ret['author_url'] = spider.make_url(response.url, get_author_url(review))
    ret['rating'] = get_rating(review)
    ret['book_id'] = get_book_id(response)
    ret['tld'] = get_tld(response)
    ret['text'] = get_text(review)
    return ret


def extract_items(spider, response):
    return map(lambda i: make_item(spider, response, i), find_reviews(response))


def get_review_page_links(response):
    return response.xpath('//a[contains(@href, "filterByStar")][contains(@class, "star")]/@href').extract()[::2]
