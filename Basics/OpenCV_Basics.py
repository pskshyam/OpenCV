
# coding: utf-8

# ** Reference **
# 
# https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/

# In[1]:

#Import necessary libraries
import cv2
import imutils


# In[2]:

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("img/jp.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))


# In[3]:

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)


# In[4]:

# access the RGB pixel located at x=50, y=100, keep in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))


# In[7]:

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 and ending at x=420,y=160
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)


# In[6]:

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)


# In[8]:

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)


# In[9]:

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)


# In[10]:

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0) # Rotate image 45 degrees clockwise, scale factor by default 1.0 
                                              #positive angles are counterclockwise and negative angles are clockwise.
rotated = cv2.warpAffine(image, M, (w, h)) # Rotate the matrix using rotation matrix M
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)


# In[11]:

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)


# In[12]:

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help us out
#The rotate_bound function of imutils will prevent OpenCV from clipping the image during a rotation.
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)


# In[13]:

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


# In[14]:

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)


# In[15]:

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)


# In[16]:

#Similar to drawing rectangles and circles, drawing a line in OpenCV using cv2.line 
#only requires a starting point, ending point, color, and thickness.
# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)


# In[17]:

#Using the cv2.putText code, you can practice overlaying text on an image 
#with different colors, fonts, sizes, and/or locations.
# draw green text on the image
#cv2.putText(img, text, starting point, font, scale, color, thickness)
output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park!!!", (10, 25), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)


# In[ ]:



