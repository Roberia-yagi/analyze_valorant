import cv2 as cv
import numpy as np
import sys
import processing as process

window_name = 'frame'

def main():
    cap_file = cv.VideoCapture(0)
    if not cap_file.isOpened():
        sys.exit()

    cv.namedWindow(window_name)

    while True:
        ret, frame = cap_file.read()
        if not ret:
            sys.exit()

        windowsize = (800, 600)
        frame = cv.resize(frame, windowsize)
        binarized_frame = process.cam_binarization(frame)

        cv.imshow(window_name, binarized_frame)

        c = cv.waitKey(1)
        if c == 27:
            break


    capture.release()
    cv.destroyWindow(window_name)

main()
