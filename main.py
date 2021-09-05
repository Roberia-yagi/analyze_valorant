import cv2 as cv
import numpy as np
import sys
import processing as process

file_path = './test.mp4'
delay = 33
window_name = 'frame'
window_name2 = 'window'
trackbar_name = 'Position'
g_slider_position = 0
g_run = 1
g_dontset = 0
cap_file = cv.VideoCapture()


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
    global delay
    global cap_file
    global g_slider_position

    # 引数が少なかったらだめ
    if len(sys.argv) == 3:
        filename = sys.argv[1]
    else:
        print('Usage: [filename], [threshold]')
        sys.exit()

    #ファイルの読み込み
    cap_file.open(filename)
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
            #smoothed_frame = process.smoothing(frame)
            #trimmed_frame = process.ammo_area(binarized_frame, cap_file)

            current_pos = int(cap_file.get(cv.CAP_PROP_POS_FRAMES))
            g_dontset = 1

            cv.setTrackbarPos(trackbar_name, window_name, current_pos)

            # Show in a window
            cv.imshow(window_name, binarized_frame)
            #cv.imshow(window_name2, trimmed_frame)

            g_run = g_run - 1

        # Escを押すと終わり
        c = cv.waitKey(delay)
        if c == ord('s'):
            g_run = 1
        if c == ord('r'):
            g_run = -1
        #ESC key
        if c == 27:
            break


    cv.destroyWindow(window_name)

if __name__ == '__main__':
    main()