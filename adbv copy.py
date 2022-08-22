import cv2,numpy

print("[INFO] Checking Screenshot",'green')
img = cv2.imread("screenshot.png")
templatex = cv2.imread("gmail2.png")

h, w, _ = templatex.shape

res = cv2.matchTemplate(img, templatex, cv2.TM_CCOEFF_NORMED)
print(res)
loc_cut = numpy.where(res<=0.03)
loc_xy = list(zip(*loc_cut[::-1]))


#cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

for i in loc_xy:
    shell(f'input tap {i[0]} {i[1]}')
    print({i[0]}, {i[1]})
    return
resize = cv2.resize(img, (540, 960), fx=0.5, fy=0.5)
cv2.imshow("img", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()