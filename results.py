from utils import *
from search import *

def recomp_exhaustive(im1,im2,fenDim = 16) :
    imTiled = tilification(im2, 8)
    tiledRes = []
    for tile in imTiled:
        x, y = exhaustive_tile(tile, im1, fenDim)
        tiledRes.append(imTile(im1[x - 4:x + 4, y - 4:y + 4], None))

    return deTilification(tiledRes,8,im1.shape[0],im1.shape[1])

def recomp_log2D(im1,im2,fenDim = 16) :
    imTiled = tilification(im2, 8)
    tiledRes = []
    for tile in imTiled:
        x, y = log2D_tile(tile, im1, fenDim)
        tiledRes.append(imTile(im1[x - 4:x + 4, y - 4:y + 4], None))

    return deTilification(tiledRes,8,im1.shape[0],im1.shape[1])

def recomp_unalafois(im1,im2,fenDim = 16) :
    imTiled = tilification(im2, 8)
    tiledRes = []
    for tile in imTiled:
        x, y = unalafois_tile(tile, im1, fenDim)
        tiledRes.append(imTile(im1[x - 4:x + 4, y - 4:y + 4], None))

    return deTilification(tiledRes,8,im1.shape[0],im1.shape[1])