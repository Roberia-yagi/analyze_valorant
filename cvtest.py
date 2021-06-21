import cv2 as cv
import numpy as np
import sys
from time import sleep

file_path = './test.mp4'
delay = 1
window_name = 'frame'
window_name2 = 'window'


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


def ammo_area(frame, cap_file):
    width = cap_file.get(3)
    height = cap_file.get(4)
    xmin, xmax = int(width * (2 / 3)), int(width * (2 / 3) + 35)
    ymin, ymax = int(height - 60), int(height - 20)
    trimmed_frame = frame[ymin:ymax, xmin:xmax]

    return trimmed_frame


def main():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
    else:
        print('Usage: [filename], [threshold]')
        sys.exit()

    cap_file = cv.VideoCapture(filename)

    if not cap_file.isOpened():
        sys.exit()

    while True:
        # Sleep to show at normal speed
        sleeptime = 1/10
        sleep(sleeptime)

        # Read frame
        ret, frame = cap_file.read()
        if not ret:
            sys.exit()

        binarized_frame = binarization(frame)
        trimmed_frame = ammo_area(binarized_frame, cap_file)

        # Show in a window
        cv.imshow(window_name, binarized_frame)
        cv.imshow(window_name2, trimmed_frame)

        # Push q to quit
        if cv.waitKey(delay) & 0xFF == ord('q'):
            break
    cv.destroyWindow(window_name)


main()
