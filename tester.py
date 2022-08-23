import numpy as np
import cv2 

img = cv2.resize(cv2.imread("screenshotphone.png",0), (0, 0), fx=0.4, fy=0.4)
template = cv2.resize(cv2.imread("addaccount.png",0), (0, 0), fx=0.8, fy=0.8)

""" method ที่ตรวจจับเจอรูปภาพ
xy
950 163
gmail.png       TM_CCOEFF,TM_CCOEFF_NORMED,TM_CCORR_NORMED,TM_SQDIFF,TM_SQDIFF_NORMED
listgmail.png   TM_CCOEFF_NORMED,TM_CCORR_NORMED,TM_SQDIFF,TM_SQDIFF_NORMED
addaccount.png  TM_CCOEFF,TM_CCOEFF_NORMED,TM_CCORR_NORMED,TM_SQDIFF,TM_SQDIFF_NORMED
google2.png     TM_CCOEFF_NORMED,TM_SQDIFF,TM_SQDIFF_NORMED

"""

h, w = template.shape
methods = [ cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w , location[1] + h)
    color = (255, 0, 0)
    cv2.rectangle(img2, location, bottom_right, (0,0,255), 3)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()