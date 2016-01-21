import scrapy


# artwork item deployed to
class Artwork(scrapy.Item):
    image_urls = scrapy.Field()
    descriptor = scrapy.Field()
    style = scrapy.Field()
