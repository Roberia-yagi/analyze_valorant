import cv2 as cv
import numpy as np
import sys
from time import sleep

file_path = './test.mp4'
delay = 1
window_name = 'frame'

cap_file = cv.VideoCapture(file_path)

if not cap_file.isOpened():
    sys.exit()

while True:
    # Sleep to show at normal speed
    sleeptime = 1/30
    sleep(sleeptime)

    # Read frame
    ret, frame = cap_file.read()
    if not ret:
        sys.exit()

    # Convert image to gray and blur it
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.blur(gray, (3, 3))

    # Detect edges using Canny
    threshold = 100
    canny_output = cv.Canny(blur, threshold, threshold * 2)
    # Find contours
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Draw contours
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (0, 0, 255)
        cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
    # Show in a window
    cv.imshow(window_name, drawing)

    # Push q to quit
    if cv.waitKey(delay) & 0xFF == ord('q'):
        break
cv.destroyWindow(window_name)
