# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import logging
from image_vectorizer.vectorizer import vectorize


class ImageParserPipeline(ImagesPipeline):

    # TODO calls downloader, see if needed
    # def get_media_requests(self, artwork, info):
    #     for image_url in artwork['image_urls']:
    #         yield scrapy.Request(image_url)

    def item_completed(self, results, artwork, info):

        # pull images that were downloaded well
        image_paths = [image['path'] for success, image in results if success]

        # if no image was downloaded, drop the item
        if not image_paths:
            raise DropItem("Item contains no images")

        # set the path to the Artwork's 'images' data member
        artwork['descriptor'] = vectorize(image_paths)

        # return artwork
        return artwork

# TODO add preprocessing pipeline
