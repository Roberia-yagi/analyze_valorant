import cv2 as cv
import sys

file_path = './test.mp4'
delay = 1
window_name = 'frame'

cap_file = cv.VideoCapture(file_path)


if not cap_file.isOpened():
    sys.exit()

while True:
    ret, frame = cap_file.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (0, 0), 5)
    cv.imshow(window_name, blur)
    if cv.waitKey(delay) & 0xFF == ord('q'):
        break
cv.destroyWindow(window_name)
