from json import loads
from sklearn import svm
import numpy as np


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

            # extract image labels
            self.y = [artwork['style'][0] for artwork in json_data]

            # insure image labels accepted as numpy string array
            self.y = np.asarray(self.y, dtype="|S")

    def train_svm(self):

        # fit svm with training data
        self.classifier.fit(self.X, self.y)

    def predict(self, descriptor):

        # return classifier prediction for given descriptor
        return self.classifier.predict([descriptor])[0]

