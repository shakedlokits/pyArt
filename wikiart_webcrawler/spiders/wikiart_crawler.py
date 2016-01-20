import scrapy
import logging
from wikiart_webcrawler.items import Artwork

DEBUG = False


class WikiartSpider(scrapy.Spider):
    name = 'wikiart'
    start_urls = ['http://beta.wikiart.org/en/Alphabet']
    base_url = 'http://beta.wikiart.org'

    def parse(self, response):

        # TODO: remove extract_first to parse all
        for href in [response.css('.dictionaries-list .header a::attr(href)').extract_first()]:
            full_url = self.base_url+href

            if DEBUG:
                logging.debug(full_url)

            yield scrapy.Request(full_url, callback=self.parse_artist_group)

    def parse_artist_group(self, response):

        # TODO: remove extract_first to parse all
        for href in [response.css('.artists-list li a::attr(href)').extract_first()]:
            full_url = self.base_url+href

            if DEBUG:
                logging.debug("moving into group: "+href)

            yield scrapy.Request(full_url, callback=self.parse_artwork_list)

    def parse_artwork_list(self, response):

        # TODO: remove extract_first to parse all
        for href in [response.css("ul.title > li:first-child > a::attr(href)").extract_first()]:
            full_url = self.base_url+href

            if DEBUG:
                logging.debug("moving into artist: "+href)

            yield scrapy.Request(full_url, callback=self.parse_artwork)

    def parse_artwork(self, response):
        content_selector = response.css('.main-content')

        if DEBUG:
            logging.debug("parsing artist: "+response.url)

        artwork = Artwork()
        artwork['image_urls'] = content_selector.css(".image img::attr(src)").extract()
        artwork['style'] = content_selector.css(".info > dl:nth-child(4) a::text").extract()

        yield artwork




