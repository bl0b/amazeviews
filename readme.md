# Amazeviews

Fetch those reviews for your books.

# What is it?

Amazeviews is a scraper. Give it your ASINs and it will fetch the reviews and output them in, say, a CSV file.

# How to run it

You need [scrapy](https://scrapy.org/) installed. Then you can run amazeviews with a simple commandline:

> $ cd where/I/put/amazeviews
> $ scrapy crawl reviews -a book=MY_BOOK_ASIN,ANOTHER_ASIN,... -o into_this_file.csv

If you wish to fetch the reviews from a particular subset of amazon domains, add the tld attribute:

> $ scrapy crawl reviews -a book=MY_BOOK_ASIN,ANOTHER_ASIN,... -a tld=com,co.uk,com.au -o into_this_file.csv
