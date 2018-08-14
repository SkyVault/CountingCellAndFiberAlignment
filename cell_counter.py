import cv2
import numpy as np
import math
import matplotlib

def CellCounter():
    image = cv2.imread("cells.jpg")
    orig = image.copy()

    contrast = 400.0
    brightness = -180.0

    image = cv2.addWeighted(image, 1. + contrast / 127., image, 0, brightness - contrast)

    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 10
    params.filterByArea = True
    params.minArea = 40
    params.filterByCircularity = True
    params.minCircularity = 0.05
    params.filterByConvexity = True
    params.minConvexity = 0.60
    params.filterByInertia = True
    params.minInertiaRatio = .1

    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(image)

    image_w_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 255, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    print(len(keypoints))

    # cv2.imshow("output", np.hstack([orig, image, image_w_keypoints]))
    # cv2.waitKey(0)
    return image_w_keypoints
