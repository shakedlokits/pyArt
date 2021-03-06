from skimage.color import rgb2gray
from skimage.feature import hog, local_binary_pattern
import numpy as np

# constant descriptor parameters
RGB_HIST_BINS = 8
HOG_WINDOW_SIZE = (16, 16)
HOG_ORIENTATIONS = 9
LBP_RADIUS = 3
LBP_POINTS = 8 * LBP_RADIUS
LBP_HIST_BIN = 2 ** 6


def get_descriptor(image):

    # get the color channel histograms (duplicates if b/w)
    hist_vec = get_histogram_vector(image)

    # get the HoG histogram
    averaged_hog = get_hog_vector(image)

    # get the lbp image histogram
    lbp_hist = get_lbp_vector(image)

    # concatenate final descriptor
    descriptor = hist_vec + averaged_hog + lbp_hist

    return descriptor


def get_lbp_vector(image):
    # set image to grays
    gray = rgb2gray(image)

    # evaluate lbp image reshaped into vector
    lbp = local_binary_pattern(gray, P=LBP_POINTS, R=LBP_RADIUS).ravel()

    # take histogram of the lbp image
    lbp_hist = np.histogram(lbp, bins=LBP_HIST_BIN)[0]

    # normalize lbp histogram
    norm_lbp_hist = lbp_hist / float(sum(lbp_hist))

    return norm_lbp_hist.tolist()


def get_hog_vector(image):
    # set image to grays
    gray = rgb2gray(image)

    # evaluate the HoG of the image over a 16x16 window
    image_hog = hog(gray, orientations=HOG_ORIENTATIONS, pixels_per_cell=HOG_WINDOW_SIZE, cells_per_block=(1, 1))

    # take an average over the HoG cells
    divided_hog = [image_hog[i:i + HOG_ORIENTATIONS] for i in range(0, len(image_hog), HOG_ORIENTATIONS)]
    averaged_hog = np.average(divided_hog, axis=0)

    return averaged_hog.tolist()


def get_histogram_vector(image):
    # evaluate image channels histogram on 8 bins
    if len(image.shape) == 3:
        r_hist = np.histogram(image[:, :, 0], bins=RGB_HIST_BINS)[0]
        g_hist = np.histogram(image[:, :, 1], bins=RGB_HIST_BINS)[0]
        b_hist = np.histogram(image[:, :, 2], bins=RGB_HIST_BINS)[0]

    elif len(image.shape) == 2:
        r_hist = g_hist = b_hist = np.histogram(image, bins=RGB_HIST_BINS)[0]

    else:
        raise Exception("Image Dimension Error")

    # normalize histograms
    norm_r_hist = r_hist / float(sum(r_hist))
    norm_g_hist = g_hist / float(sum(g_hist))
    norm_b_hist = b_hist / float(sum(b_hist))

    # return concatenation of histograms
    return norm_r_hist.tolist() + norm_g_hist.tolist() + norm_b_hist.tolist()
