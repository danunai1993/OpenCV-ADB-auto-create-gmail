from termcolor import colored
import numpy as np
import cv2,time
from ppadb.client import Client as AdbClient

print(colored("===========================================",'red'))
print(colored("---- Auto register Gmail ---- ",'green'))
print(colored("+ Dev : !nwgodrip",'green'))
print(colored("+ Github : github.com/danunai1993",'green'))
print(colored("+ FB : facebook.com/Danunai.Sangkachalaw",'blue'))
print(colored("===========================================",'red'))
print(colored("[INFO] Starting Automatic Mode",'green'))

try:
    client = AdbClient(host="localhost", port=5037)
    devices = client.devices()
    device = devices[0]
    print(f'Device: {device}') 
    print(colored('[/] Connecting Driver Successfuly', 'green'))
except:
    print(colored('[X] No connection!! pls Connect your device', 'red'))


def save():
    with open("screenshot.png", "wb") as f:
        f.write(device.screencap())
        time.sleep(1)
        print(colored("[/] Screenshot saved!!",'green'))

def check():   
    print(colored("[INFO] Checking Screenshot",'green'))
    screen = cv2.imread("screenshot.png")
    item = cv2.imread("gmail2.png")

    h, w, _ = item.shape

    res = cv2.matchTemplate(screen, item, cv2.TM_CCOEFF)
    loc_cut = np.where(res <= 0.03)
    loc_xy = list(zip(*loc_cut[::-1]))
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(screen, top_left, bottom_right, (0, 0, 255), 2)

    resize = cv2.resize(screen, (540, 960), fx=0.5, fy=0.5)
    cv2.imshow("img", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
save()
check()