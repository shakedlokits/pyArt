# -*- coding: utf-8 -*-
from os import remove
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from image_vectorizer.vectorizer import get_descriptor


class ArtworkDescriptorPipeline(ImagesPipeline):

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

        # set the path to the Artwork's 'images' data member
        artwork['descriptor'] = get_descriptor(image_paths)

        # unset 'image_urls' field for final parsing
        del artwork['image_urls']

        # remove image file
        remove("./images/"+image_paths[0])

        # return artwork
        return artwork
