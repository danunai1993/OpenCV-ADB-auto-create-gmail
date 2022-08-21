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
        time.sleep(0.3)
        print(colored("[/] Screenshot saved!!",'green'))

def check(imagecheck):
    item = cv2.imread(imagecheck)
    screen = cv2.imread("screenshot.png")
    # cv2.imshow('',item)
    # cv2.waitKey()
    result = cv2.matchTemplate(item,screen,cv2.TM_SQDIFF_NORMED)
    print(result)
    loc_cut = np.where(result<=0.03)
    loc_xy = list(zip(*loc_cut[::-1]))
    print(loc_xy)
    print(colored(f'[INFO] Found {len(loc_xy)}', 'green'))
    for i in loc_xy:
        device.shell(f'input tap {i[0]} {i[1]}')
        print(colored(f'[INFO] Tap {i[0]} {i[1]}', 'green'))
        return

save()
check('gmail.png')