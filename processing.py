import cv2 as cv
import numpy as np
import sys

def binarization(frame):
    if len(sys.argv) > 2:
        threshold = int(sys.argv[2])
    else:
        threshold = 120

    # Convert image to gray and blur it
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.blur(gray, (3, 3))

    # Detect edges using Canny
    canny_output = cv.Canny(blur, threshold, threshold * 2)
    # Find contours
    contours, hierarchy = cv.findContours(
        canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Draw contours
    drawing = np.zeros(
        (canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (255, 255, 255)
        cv.drawContours(drawing, contours, i, color,
                        2, cv.LINE_8, hierarchy, 0)

    return drawing