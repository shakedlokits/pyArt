import skimage.io as io

def vectorize(image_path):
    io.use_plugin('matplotlib','imshow')
    image = io.imread("./images/"+image_path[0])
    io.imshow(image)
    return "test"