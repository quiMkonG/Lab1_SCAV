import numpy as np
import sys
import scipy.fftpack as fft
from matplotlib.image import imread
from matplotlib.pyplot import imshow, show

input = imread(sys.argv[1])
result = fft.dct(input)
