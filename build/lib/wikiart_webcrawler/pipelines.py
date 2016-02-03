# -*- coding: utf-8 -*-
from os import remove
import boto3
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from image_vectorizer.vectorizer import get_descriptor


class ArtworkDescriptorPipeline(ImagesPipeline):

    # initialize wikiart s3 bucket
    wikiart_bucket = boto3.resource('s3').Bucket('wikiart')

    def item_completed(self, results, artwork, info):
        """
        called after artwork image have been processed and ready for preprocessing
        to json serialization
        """

        # pull images that were downloaded well
        image_paths = [image['path'] for success, image in results if success]

        # if no image was downloaded, drop the item
        if not image_paths:
            raise DropItem("Item contains no images")

        # set the path to the Artwork's 'images' data member TODO revert to descriptor parsing
        artwork['descriptor'] = get_descriptor(image_paths[0])

        # unset 'image_urls' field for final parsing TODO restore field deletion
        del artwork['image_urls']

        # remove image file TODO restore image deletion for amazon
        self.wikiart_bucket.objects.all().delete()

        # return artwork
        return artwork
