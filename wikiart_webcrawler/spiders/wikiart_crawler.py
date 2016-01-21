import scrapy
import logging
from wikiart_webcrawler.items import Artwork

# debug prompt flag
DEBUG = False


class WikiartGlobalSpider(scrapy.Spider):
    """
    A crawler intended to crawl the entire wikiart database
    """

    name = 'wikiart_global'
    start_urls = ['http://beta.wikiart.org/en/Alphabet']
    base_url = 'http://beta.wikiart.org'

    def parse(self, response):
        """
        initializes spider with 'start_urls' http req response
        """

        # iterates over artists alphabet
        for href in [response.css('.dictionaries-list .header a::attr(href)').extract_first()]:

            # sets full url (instead of parse local)
            full_url = self.base_url+href

            if DEBUG:
                logging.debug(full_url)

            # requests next level with alphabet crawl callback function
            yield scrapy.Request(full_url, callback=self.parse_artist_group)

    def parse_artist_group(self, response):
        """
        called to crawl artist lists from alphabet pages http req response
        """

        # iterates over artists
        for href in [response.css('.artists-list li a::attr(href)').extract_first()]:

            # sets full url (instead of parse local)
            full_url = self.base_url+href

            if DEBUG:
                logging.debug("moving into group: "+href)

            # requests next level with artist crawl callback function
            yield scrapy.Request(full_url, callback=self.parse_artwork_list)

    def parse_artwork_list(self, response):
        """
        called to crawl artwork lists from artist pages http req response
        """

        # TODO: remove extract_first to parse all
        # iterates over artist artwork list
        for href in [response.css("ul.title > li:first-child > a::attr(href)").extract_first()]:

            # sets full url (instead of parse local)
            full_url = self.base_url+href

            if DEBUG:
                logging.debug("moving into artist: "+href)

            # requests next level with artwork crawl callback function
            yield scrapy.Request(full_url, callback=self.parse_artwork)

    @staticmethod
    def parse_artwork(response):
        """
        called to parse artwork from artworks list pages http req response
        """

        # focus on the information div
        content_selector = response.css('.main-content')

        if DEBUG:
            logging.debug("parsing artist: "+response.url)

        # create and Artwork Item and parse attributes
        artwork = Artwork()
        artwork['image_urls'] = content_selector.css(".image img::attr(src)").extract()
        artwork['style'] = content_selector.css(".info > dl:nth-child(4) a::text").extract()

        yield artwork




