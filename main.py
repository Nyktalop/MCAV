from utils import *
from search import *
from results import *
import numpy as np
import matplotlib.pyplot as plt


im1 = open_grayscale("I2-1.PNG")
im2 = open_grayscale("I2-2.PNG")

show_grayscale(recomp_unalafois(im1,im2,16))