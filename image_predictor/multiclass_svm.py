from json import loads
from sklearn import svm
import numpy as np
from skimage import img_as_float
from PIL import Image
from image_vectorizer.vectorizer import get_descriptor

# NOTE: use like this
# predictor=MultiClassSVM('./data/wikiart_data.json')
# answer = predictor.predict('./data/dada_test.jpg')
# print(answer)

class ColorPrinter:

    # color data members
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_log(message, color):

        # evaluate even break length
        break_length = (60 - len(message))//2

        # print log message
        print color + '#'*break_length, message, '#'*break_length + ColorPrinter.ENDC


class MultiClassSVM:

    # classifier, X descriptors, y labels data members
    classifier = {}
    X = []
    y = []

    def __init__(self, file_path):

        # initialize multi-class classifier with one vs. one shape
        ColorPrinter.print_log("initializing SVM", ColorPrinter.HEADER)
        self.classifier = svm.SVC(decision_function_shape='ovo')

        # parse the training data from file
        ColorPrinter.print_log("parsing SVM data", ColorPrinter.HEADER)
        self.parse_training_data(file_path)

        # train svm in training data
        ColorPrinter.print_log("training SVM", ColorPrinter.HEADER)
        self.train_svm()

        ColorPrinter.print_log("SVM IS READY!", ColorPrinter.OKGREEN)

    def parse_training_data(self, file_path):

        # initialize file object from file_path
        with open(file_path, 'r') as f:

            # parse json objects line by line while removing '\n' symbols
            json_data = [loads(line.rstrip('\n')) for line in f]

            # extract image descriptors
            self.X = [artwork['descriptor'] for artwork in json_data]

            # extract image labels NOTE: added force encoding to ascii
            self.y = [artwork['style'][0].encode('ascii', 'ignore').encode('ascii') for artwork in json_data]

            # insure image labels accepted as numpy string array
            self.y = np.asarray(self.y, dtype="|S")

    def train_svm(self):

        # fit svm with training data
        self.classifier.fit(self.X, self.y)

    @staticmethod
    def load_image(image_path):

        # loads image from file
        image = Image.open(image_path)

        # set image to floats
        float_image = img_as_float(image)

        return float_image

    def predict(self, image_path):

        # load image object
        image = self.load_image(image_path)

        # get descriptor from image
        descriptor = get_descriptor(image)

        # return classifier prediction for given descriptor
        return self.classifier.predict([descriptor])[0]



