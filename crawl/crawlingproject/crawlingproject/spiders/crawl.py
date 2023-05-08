from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "mulai"
    # allowed_domains = ["toscrape.com"]
    # start_urls = ["https://books.toscrape.com/"]
    allowed_domains = ["www.timeshighereducation.com"]
    start_urls = ["https://www.timeshighereducation.com/world-university-rankings/2023/"]

    rules = (
        # Rule(LinkExtractor(allow="catalogue/category")),
        # Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
        Rule(LinkExtractor(allow="world-ranking#!"), callback="parse_item"),
        # yang dimaskdu dinsin adalah bagaimana pattern yang akan digunakan saat aakan mencsrape web/crawl
    )

    # def parse_item(self, response):
    #     yield {
    #         "title": response.css(".product_main h1::text").get(),
    #         "price": response.css(".price_color::text").get(),
    #         "availability": response.css(".availability::text")[1].get().replace("\n", "").replace(" ", "").replace("Instock", "").replace("available", "").replace("(", "").replace(")", "")
    #     } 
    def parse_item(self, response):
        yield {
            "title": response.css(".ranking-institution-title::text").get()
        } 