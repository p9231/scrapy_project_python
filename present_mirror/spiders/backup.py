import scrapy
from ..items import PresentMirrorItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_no = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1',

    ]

    # def parse(self, response):
    #     title = response.css('title::text').extract()
    #     yield {'titletext': title}

    def _parse(self, response):

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

        next_page = 'https://quotes.toscrape.com/page/'+str(QuoteSpider.page_no)+'/'

        if QuoteSpider.page_no < 11:
            QuoteSpider.page_no +=1
            yield response.follow(next_page, callback=self._parse)

        # next_page = response.css('li.next a::attr(href)').get()
        #
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self._parse)
