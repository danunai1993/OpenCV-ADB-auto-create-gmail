from ctypes import resize
from re import template
import cv2,time
from ppadb.client import Client as AdbClient

try:
    client = AdbClient(host="localhost", port=5037)
    devices = client.devices()
    device = devices[0]
    print(f'Device: {device}')
except:
    print("no connection")


def save():
    with open("screenshot.png", "wb") as f:
        f.write(device.screencap())
        time.sleep(0.3)
        print("Screenshot saved")

def check():
    print("[INFO] Checking Screenshot",'green')
    img = cv2.imread("screenshot.png")
    #img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    templatex = cv2.imread("google.jpg")
    #templatex_gray = cv2.cvtColor(templatex, cv2.COLOR_RGB2GRAY)
    h, w, _ = templatex.shape

    res = cv2.matchTemplate(img,templatex,cv2.TM_CCOEFF)
    print(res)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 4)
    resize = cv2.resize(img, (540, 960), fx=0.5, fy=0.5)
    cv2.imshow("", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

save()
check()