from imageio import imread, imwrite
import numpy as np
from skimage import color
import matplotlib.pyplot as plt



class imTile :
    def __init__(self, tile, center):
        self.data = tile
        self.center = center
        self.shape = tile.shape

    def mse(self, block):
        return (np.square(self.data-block)).mean(axis=None)


def mse(a,b):
    return (np.square(a - b)).mean(axis=None)


def open_grayscale(filename) :
    img = imread(filename)
    return np.array(color.rgb2gray(color.rgba2rgb(img)))

def save(image, filename) :
    imwrite(filename, image)

def show_grayscale(image) :
    plt.imshow(image,cmap="Greys_r")
    plt.show()

def show(image) :
    plt.imshow(image)
    plt.show()

def clamp(val,a,b):
    return a if val < a else b if val > b else val

def tilification(im,blockDim) :
    return np.array([imTile(im[x:x + blockDim, y:y + blockDim], (x+blockDim//2,y+blockDim//2)) for x in range(0, im.shape[0], blockDim) for y in range(0, im.shape[1], blockDim)])

def deTilification(tiledIm, blockDim, imX, imY):
    sideX = imX//blockDim
    sideY = imY//blockDim

    im = np.zeros((imX,imY))
    for i,tile in enumerate(tiledIm):
        u = i//sideY
        v = i%sideY
        for x in range(blockDim):
            for y in range(blockDim):
                im[x+u*blockDim,y+v*blockDim] = tile.data[x,y]

    return im