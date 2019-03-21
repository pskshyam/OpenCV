# Document Scanner

[//]: # (Image References)

[image1]: ./images/receipt-input.JPG "Input Receipt"
[image2]: ./images/receipt-edge-detected.JPG "Edge detection of the receipt"
[image3]: ./images/receipt-outlined.JPG "Outline of the receipt"
[image4]: ./images/receipt-scanned.JPG "Perspective transformed receipt"

In this project, I showed how to build a document scanner using OpenCV. We will work on the below image of a scanned receipt.

![alt_text][image1]

Document scanning can be broken down into three distinct and simple steps.

Step 1: Apply edge detection.

![alt_text][image2]

Step 2: Find the contours in the image that represent the document we want to scan. We assume that the largest contour in the image with exactly four points is our piece of paper to be scanned.

![alt_text][image3]

Step 3: Take the four points representing the outline of the document and apply a perspective transform to obtain a top-down, “birds eye view” of the image.

![alt_text][image4]

Optionally, you can also apply thresholding to obtain a nice, clean black and white feel to the piece of paper using `threshold_local`  function from scikit-image. This function will help us obtain the “black and white” feel to our scanned image.

Source:
https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
