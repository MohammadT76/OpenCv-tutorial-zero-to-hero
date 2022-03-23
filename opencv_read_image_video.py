# in my system for commentting and uncommenting multiple line : Ctrl + / 
# for more information go to : vscode -> File -> Preferences -> keyboard Shortcuts

import cv2

# reading images
# img = cv2.imread('image/cat_2.jpg')
# cv2.imshow('Cat Image' , img)

# cv2.waitKey(0)



# reading videos
capture = cv2.VideoCapture('video/video2.mp4')

while True:
    is_frame , frame = capture.read()
    cv2.imshow('Frame' , frame)
    print(f"is frame : {is_frame}")

    key = cv2.waitKey(50)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()