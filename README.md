# Lab1_SCAV

#Exercise 1)

Corresponding files: rgbyuv.py

The file is aimed to be run from terminal with the following sequence:

python3 rgbyuv.py xxx A B C

Where xxx specifies the "rgb" or "yuv" color space and values A,B,C correspond to each value (R,G,B or Y,U,V) respectively. Values for RGB can be either normalized or not, but YUV values must be. It prints in the terminal the transformed values.

#Exercise 2)

Corresponding files: ex:0x.png, lenna_0x.png/gif/jpg

Different compression methods:

Case 1: Changing file format from .png to .jpg. Compression from 88.2kB to 13.2kB.

Case 2: Resizing the image from 220x220 pixels to 110x110. This is not the most suitable/optimal option in my opinion because it changes the image size. Compression from 88.2kB to 34.4kB.

Case 3: Changing file format from .png to .gif. Compression from 88.2kB to 27.1kB.

In my opinion the best compression is performed by changing image format from .png to .jpg, as it is the hardest compression and it does not change the image size. To be honest, I was not able to change image quality in order to compress it without changing its size or format.

#Exercise 3) 

Corresponding files: ex3_bw.png, lennabw.png, ex3_bw02.png, lenna_bw.png. lenna_bw.jpg

At first I just used conversion to grayscale by changing the hue angle (in degrees) to 0 and then compressing it by changing the format to .jpg. (result: lennabw.jpg)

However, after looking for a black and white conversion on the internet, I found an optimal solution by using the threshold filter. I still had to apply some changes in terms of size to this proposed solution and fit them to the size of lenna image (220x220 pixels). After obtaining the black and white image I compressed it to .jpg using the same method as in Exercise 2. (result: lenna_bw.jpg)


(source: https://video.stackexchange.com/questions/28758/ffmpeg-convert-video-to-black-white-with-threshold/28759#28759) 

#Exercise 4)

Corresponding files: runlen.py

This file is aimed to be run from the terminal with the following line:

python3 runlen.py X

Where X can be any consecution of bits. The function prints in the terminal the run-length encoded solution. The code is commented so a deeper explanation can be found in the .py file.

#Exercise 5)

Corresponding files: dct.py

This file is aimed to be run from terminal with the following command

python3 dct.py X

Where X is either an image file or the path to this image file. It computes the dct taking advantage of the fft package in the scipy library.

#END 




