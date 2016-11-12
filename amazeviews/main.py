from amazeviews.spiders.reviews import Reviews

__author__ = 'damien'

from scrapy.crawler import CrawlerProcess
import sys

tld = sys.argv[1]
book_id = sys.argv[2]
print book_id

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'DOWNLOAD_HANDLERS': {'s3': None}
})

process.crawl(Reviews)
process.start()  # the script will block here until the crawling is finished
