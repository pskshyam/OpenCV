# Measuring size of objects in an image

[//]: # (Image References)

[image1]: ./images/size_of_objects_example.gif "Image with size of objects"
[image2]: ./images/receipt-edge-detected.jpg "Edge detection of the receipt"
[image3]: ./images/receipt-outlined.jpg "Outline of the receipt"
[image4]: ./images/receipt-scanned.jpg "Perspective transformed receipt"

In this project, we see how to measure the size of objects in an image using `Python` and `OpenCV`.

![alt_text][image1]

## Introduction
In order to do this, we need to determine our <strong>pixels per metric</strong> ratio, which describes the number of pixels that can “fit” into a given metric (inches, millimeters, meters, etc.).

To compute this ratio, we first need to perform a “calibration” (not to be confused with intrinsic/extrinsic calibration) using a reference object. We need a reference object with two important properties:

Property #1: The reference object should have known dimensions (such as width or height) in terms of a measurable unit (inches, millimeters, etc.).
Property #2: The reference object should be easy to find, either in terms of location of the object or in its appearance.

Provided that both of these properties can be met, we can utilize the reference object to calibrate pixels_per_metric variable, and from there, compute the size of other objects in an image.

In this example, we’ll be using the United States quarter as our reference object and throughout all examples, ensure it is always the left-most object in our image.

By guaranteeing the quarter is the left-most object, we can sort our object contours from left-to-right, grab the quarter (which will always be the first contour in the sorted list), and use it to define our pixels_per_metric, which we define as:

pixels_per_metric = object_width / know_width

A US quarter has a known_width of 0.955 inches. Now, suppose that our object_width (measured in pixels) is computed be 150 pixels wide (based on its associated bounding box).

The pixels_per_metric is therefore:

pixels_per_metric = 150px / 0.955in = 157px

Thus implying there are approximately 157 pixels per every 0.955 inches in our image. Using this ratio, we can compute the size of objects in an image.

## Steps involved in the project

* Preprocess the image
* perform edge detection followed by dilation and erosion
* Find contours in the edged image and sort them from left to right
* Compute the rotated bounding box of the contour and order the points in the contour such that they appear in top-left, top-right, bottom-right, and bottom-left order
* Draw the outline of the rotated bounding box and points of each corner
* Compute the midpoints adnd draw the midpoints on the image and lines between the midpoints
* Compute the Euclidean distance between the midpoints
* For the first image (reference object), compute and initialize pixels per metric as the ratio of pixels to supplied metric (in this case, inches)
* Compute the size of each object using above initialized pixelsPerMetric and draw it on the image

## Executing the project
`$ python object_size.py --image images/example_01.png --width 0.955`

Try with different example images present in the images folder and check the result.

Source: https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/
