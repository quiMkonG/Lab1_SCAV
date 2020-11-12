import numpy as np
import sys

type = sys.argv[1]
p1 = float(sys.argv[2])
p2 = float(sys.argv[3])
p3 = float(sys.argv[4])

v = [p1,p2,p3]

def rgb2yuv(rgb):
    convert_matrix =[[0.299, 0.587, 0.114],
                    [-0.147, -0.289, 0.436],
                    [0.615, -0.515, -0.1]]
    return np.matmul(convert_matrix,np.transpose(rgb))


def yuv2rgb(yuv):
    convert_matrix =[[1, 0, 1.14],
                    [1, -0.394, -0.581],
                    [1, 2.032, 0]]
    return np.matmul(convert_matrix,np.transpose(rgb))

def normalizergb(rgb):
    return np.asarray(rgb)/255


if (type == 'rgb'):
    if (all((0<=i<=1)for i in v)):
        result = rgb2yuv(v)
        print(result)
    elif (all((0<=i<=255))for i in v):
        result = rgb2yuv(normalizergb(v))
        print(result)

elif (type == 'yuv') and ():
    result = yuv2rgb(v)
    print(result)
else:
    print('Error: Specified data type is not rgb neither yuv OR values are out of range for the specified format')
