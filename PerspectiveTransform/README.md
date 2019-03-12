# OpenCV

[//]: # (Image References)

[image1]: ./output/example_1.jpg "Example1 Output"
[image2]: ./output/example_2.jpg "Example2 Output"
[image3]: ./output/example_3.jpg "Example3 Output"

This project covers how to use a perspective transform to obtain a top-down, “birds eye view” of an image given the reference points. The repository contains below two files:

* transform.py - this python file contains two functions - 
  * order_points - to order a list of coordinates of the image that will be ordered such that the first entry in the list is the top-left, the second entry is the top-right, the third is the bottom-right, and the fourth is the bottom-left.
  * four_point_transform - obtain a consistent order of the points by calling above function, compute the width and height of the image, construct the set of destination points to obtain a "birds eye view", (i.e. top-down view) of the image
* transform_example.py - to read input image and coordinates, call four_point_transform function and output the warped image.

Input folder contains images used for testing and output folder contains corresponding warped images.

To execute the transform_example.py script, open a terminal or command window and navigate to this file and from there enter the following command:

`python transform_example.py --image images/example_01.png --coords "[(73, 239), (356, 117), (475, 265), (187, 443)]"`

Two image windows are opened showing original image and warped image. 

Below are the output images of the images present in ./input folder.

![alt_text][image1]
![alt_text][image2]
![alt_text][image3]

These basics are from pyimagesearch blog article:
https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
