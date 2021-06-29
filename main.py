import cv2 as cv
import numpy as np
import sys
import processing as process

file_path = './test.mp4'
#delay = 33
window_name = 'frame'
window_name2 = 'window'
trackbar_name = 'Position'
g_slider_position = 0
g_run = 1
g_dontset = 0
cap_file = None


def ammo_area(frame, cap_file):
    width = cap_file.get(3)
    height = cap_file.get(4)
    xmin, xmax = int(width * (2 / 3)), int(width * (2 / 3) + 35)
    ymin, ymax = int(height - 60), int(height - 20)
    trimmed_frame = frame[ymin:ymax, xmin:xmax]

    return trimmed_frame


def onTrackbarSlide(pos):
    global g_dontset
    global g_run
    global cap_file
    cap_file.set(cv.CAP_PROP_POS_FRAMES, pos)

    if g_dontset != 1:
        g_run = 1
    g_dontset = 0


def main():
    global g_dontset
    global g_run
    global cap_file
    global g_slider_position

    # 引数が少なかったらだめ
    if len(sys.argv) == 3:
        filename = sys.argv[1]
    else:
        print('Usage: [filename], [threshold]')
        sys.exit()

    #ファイルの読み込み
    cap_file = cv.VideoCapture(filename)
    if not cap_file.isOpened():
        sys.exit()
    frames = cap_file.get(cv.CAP_PROP_FRAME_COUNT)

    #ウィンドウの作成
    cv.namedWindow(window_name)
    cv.createTrackbar(trackbar_name, window_name,
                      g_slider_position, int(frames), onTrackbarSlide)

    while True:
        if g_run != 0:
            # フレームの読み込み
            ret, frame = cap_file.read()
            if not ret:
                sys.exit()

            # 画像の加工
            binarized_frame = process.binarization(frame)
            trimmed_frame = ammo_area(binarized_frame, cap_file)

            current_pos = int(cap_file.get(cv.CAP_PROP_POS_FRAMES))
            g_dontset = 1

            cv.setTrackbarPos(trackbar_name, window_name, current_pos)

            # Show in a window
            cv.imshow(window_name, frame)
            #cv.imshow(window_name2, trimmed_frame)

            g_run = g_run - 1

        # Push q to quit
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
