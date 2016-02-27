# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from image_vectorizer.vectorizer import get_descriptor
from PIL import Image
from io import BytesIO
import urllib
from skimage import img_as_float


class ArtworkDescriptorPipeline(object):

    def process_item(self, artwork, spider):
        """
        called after artwork image have been processed and ready for preprocessing
        to json serialization
        """

        # fetch image from url
        image = load_image(artwork['image_urls'][0])

        # evaluate and set Artwork's 'descriptor' data member from image
        artwork['descriptor'] = get_descriptor(image)

        # verify item validity
        # check descriptor length
        if len(artwork['descriptor']) != 97:
            raise DropItem("bad descriptor length: " + str(len(artwork['descriptor'])))

        # check style exists
        if len(artwork['style']) == 0:
            raise DropItem("no style tag")

        # unset 'image_urls' field for final parsing
        del artwork['image_urls']

        # return artwork
        return artwork


def load_image(image_path):

    # attempt to read image from url, drop item if fetch failed
    try:
        image_response = urllib.urlopen(image_path).read()
    except IOError:
        raise DropItem("Could not download image")

    # decode image response
    decoded = BytesIO(image_response)

    # convert to PIL image, ignores image dimension (:
    image = Image.open(decoded)

    # set image to floats
    float_image = img_as_float(image)

    return float_image