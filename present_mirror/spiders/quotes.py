import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import PresentMirrorItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_no = 2
    start_urls = [
        'https://quotes.toscrape.com/login',

    ]

    def parse(self, response):

        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': "pradeep@gmail.com",
            'password': '12345'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        items = PresentMirrorItem()

        all_div_quote = response.css('div.quote')

        for quotes in all_div_quote:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items