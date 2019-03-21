# Bubble sheet scanner and test grader using OMR, Python, and OpenCV

[//]: # (Image References)

[image1]: ./images/example_test.png "Example bubble sheet"
[image2]: ./images/omr_edged.jpg "Edge detection of exam paper"
[image3]: ./images/omr_exam_contours.jpg "Contours of exam paper"
[image4]: ./images/omr_perspective_transform.jpg "Perspective transformed exam paper"
[image5]: ./images/omr_thresh.jpg "Binary Thresholded exam paper"
[image6]: ./images/omr_finding_bubbles.jpg "Finding Bubbles on exam paper"
[image7]: ./images/omr_bubble_rows.jpg "Rows of Bubbles on exam paper"
[image8]: ./images/omr_mask.gif "Mask for each bubble"
[image9]: ./images/omr_correct_vs_incorrect.jpg "Correct vs Incorrect bubbles"
[image10]: ./images/omr_result.jpg "Final Result"

In this project, we will see what Optical Mark Recognition (OMR) is and how to implement a bubble sheet test scanner and grader using strictly computer vision and image processing techniques, along with the OpenCV library.

## Optical Mark Recognition (OMR)
Optical Mark Recognition, or OMR for short, is the process of automatically analyzing human-marked documents and interpreting their results.

The most famous, easily recognizable form of OMR are bubble sheet multiple choice tests.

![alt_text][image1]

## Implementing a bubble sheet scanner and grader using OMR, Python, and OpenCV

The goal of this project is to build a bubble sheet scanner and test grader using Python and OpenCV.

To accomplish this, our implementation will need to satisfy the following 7 steps:

Step #1: Detect the exam paper in an image by applying edge detection and finding contours.

![alt_text][image2]

![alt_text][image3]

Step #2: Apply a perspective transform to extract the top-down, birds-eye-view of the exam paper.

![alt_text][image4]

Step #3: Grading the document starts with binarization, or the process of thresholding/segmenting the foreground from the background of the image using Otsu’s thresholding method.

![alt_text][image5]

Step #4: This binarization will allow us to once again apply contour extraction techniques to find each of the bubbles in the exam:
Extract the set of bubbles (i.e., the possible answer choices) from the perspective transformed exam.

![alt_text][image6]

Step #5: We must sort the questions/bubbles from top-to-bottom. This will ensure that rows of questions that are closer to the top of the exam will appear first in the sorted list.

![alt_text][image7]

Step #6: Determine the marked (i.e., “bubbled in”) answer for each row.
Given a row of bubbles, we have to determine which bubble is filled in by using our thresh image and counting the number of non-zero pixels (i.e., foreground pixels) in each bubble region.

![alt_text][image8]

Step #7: Lookup the correct answer in our answer key to determine if the user was correct in their choice.

![alt_text][image9]

Step #8: Scoring the exam and displaying the results

![alt_text][image10]

Step #9: Repeat for all questions in the exam.

Please refer to test_grader.py file for the actual implementation of our algorithm.

## Extending the OMR and test scanner
We can extend this code for finding unanswered questions and more than one filled-up bubbles for each question.

Source:

https://www.pyimagesearch.com/2016/10/03/bubble-sheet-multiple-choice-scanner-and-test-grader-using-omr-python-and-opencv/
