import cv2 as cv
import numpy as np
import sys
import processing as process

file_path = './test.mp4'
#delay = 33
window_name = 'frame'
cap_file = None


def main():
    global cap_file

    #ファイルの読み込み
    cap_file = cv.VideoCapture(0)
    if not cap_file.isOpened():
        sys.exit()
    frames = cap_file.get(cv.CAP_PROP_FRAME_COUNT)

    #ウィンドウの作成
    cv.namedWindow(window_name)

    while True:
        if g_run != 0:
            # フレームの読み込み
            ret, frame = cap_file.read()
            if not ret:
                sys.exit()

            # 画像の加工
            binarized_frame = process.binarization(frame)

            cv.imshow(window_name, frame)


        c = cv.waitKey(10)
        if c == ord('s'):
            g_run = 1
            print("single step run = ", g_run, "\n")
        if c == ord('r'):
            g_run = -1
            print("run step run = ", g_run, "\n")
        #ESC key
        if c == 27:
            break


    cv.destroyWindow(window_name)


main()
