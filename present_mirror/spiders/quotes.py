import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/',
        # 'https://www.spyder-ide.org/'
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}
