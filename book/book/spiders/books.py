import scrapy

from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):

        items=BookItem()

        all_books=response.css('article.product_pod')

        for books in all_books:

            name=books.css('.product_pod a::text').extract()
            price=books.css('.price_color::text').extract()

            photo=(books.css("img").xpath("@src").extract())



            items['name']=name
            items['price']=price
            items['photo']=photo
            yield items

