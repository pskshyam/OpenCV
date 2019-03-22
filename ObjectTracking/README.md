# Object Tracking using OpenCV

## Introduction
In this project, we detect the presence of a colored ball using computer vision techniques, track the ball as it moves around in the video frames and draw its previous positions as it moves. We use OpenCV and Python to achieve this.

This project contains below steps:
1. Read the frames from a video file or a webcam.
2. Preprocess each frame - resizing the width, blurring and converting to HSV color space
3. Construct a mask by passing the lower and upper boundaries of the "green" ball in the HSV color space to `cv2.inRange()` function.
4. Find contours in the mask
5. Find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
6. Draw the circle and centroid on the frame, then update the list of tracked points
7. Loop over the set of tracked points and compute the thickness of the line and draw the connecting lines
8. Show the frame to the screen.

## Implementation details.

### Dequeue
We’ll be using deque, a list-like data structure with super fast appends and pops to maintain a list of the past N (x, y)-locations of the ball in our video stream. Maintaining such a queue allows us to draw the “contrail” of the ball as its being tracked.

We take an input argument named `buffer` which is the maximum size of `deque`, which maintains a list of the previous (x, y)-coordinates of the ball we are tracking. This deque  allows us to draw the “contrail” of the ball, detailing its past locations. A smaller queue will lead to a shorter tail whereas a larger queue will create a longer tail (since more points are being tracked)

### HSV Color Space boundaries
The lower and upper boundaries of the color green in the HSV color space (which are determined using the <a href="https://github.com/jrosebr1/imutils/blob/master/bin/range-detector">`range-detector`</a> script in the imutils  library). These color boundaries will allow us to detect the green ball in our video file.

## Execution of the Script
`$ python object_tracking.py --video ball_tracking_example.mp4` - using a video file

`$ python object_tracking.py` - using a webcam

Source: https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
