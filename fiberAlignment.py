import cv2
import numpy as np
import math
import matplotlib

def FiberAlignment(inputImagePath):
    # load the image, convert it to grayscale, and blur it slightly
    image = cv2.imread(inputImagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # apply Canny edge detection using a wide threshold, tight
    # threshold, and automatically determined threshold
    wide = cv2.Canny(blurred, 10, 200)
    tight = cv2.Canny(blurred, 225, 250)
    # auto = auto_canny(blurred)
    
    return wide

def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))

if __name__=="__main__":
    image = cv2.imread("percent4m.tif")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    minLineLength = 0
    maxLineGap = 5

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)

    theLines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            theLines.append((x1,y1, x2, y2))
            cv2.line(image, (x1, y1), (x2, y2), (255, 255, 0), 2)

    slopes = []
    for line in theLines:
        x1, y1, x2, y2 = line
        angle = np.rad2deg(
            np.arctan2(y2 - y1, x2 - x1)
        ) + 180
        slopes.append(angle)

    av = mad(slopes)
    print(av)

    cv2.imwrite('out.png', image)
