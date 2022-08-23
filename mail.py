import cv2, time, numpy as np
import names, random
from ppadb.client import Client as AdbClient


try:
    client = AdbClient(host="127.0.0.1",port=5037)
    devices = client.devices()
    device = devices[0]

except:
    print("Not connect")

def save():
    with open("screenshotphone.png","wb")as f:
        f.write(device.screencap())
        time.sleep(0.3)
        print("Screenshot saved")
        device.shell(f"input tap 950 163")
        time.sleep(.5)
        device.shell(f"input swipe 376 1950 376 336 1500")
        time.sleep(.5)
        device.shell(f"input tap 350 1726")
        time.sleep(.5)
        device.shell(f"input tap 267 662")
        time.sleep(3.5)
        device.shell(f"input text '272003'")
        time.sleep(4.5)
        device.shell(f"input tap 150 2026")
        time.sleep(.5)
        device.shell(f"input tap 198 1728")
        time.sleep(1.5)
        device.shell(f"input tap 210 736")
        time.sleep(1.5)
        getname = names.get_first_name()
        device.shell(f"input text {getname}xxt")
        time.sleep(1.5)
        device.shell(f"input tap 350 1131")
        time.sleep(1.5)
        device.shell(f"input tap 872 2019")
        time.sleep(1.5)
        device.shell(f"input tap 161 721")
        time.sleep(1.5)
        day = random.randint(0,28)
        device.shell(f"input text {day}")
        time.sleep(1.5)
        device.shell(f"input tap 514 729")
        time.sleep(1.5)
        device.shell(f"input tap 226 708")
        time.sleep(1.5)
        device.shell(f"input tap 803 726")
        time.sleep(1.5)
        year = random.randint(1990,2000)
        device.shell(f"input text {year}")
        time.sleep(1.5)
        device.shell(f"input tap 302 941")
        time.sleep(1.5)
        device.shell(f"input tap 267 1193")
        time.sleep(1.5)
        device.shell(f"input tap 879 2021")
        time.sleep(1.5)
        """
        #แบบไม่มีตัวเลือกให้กรอกยอย่างเดียว
        device.shell(f"input text {getname}")
        time.sleep(1.5)
        device.shell(f"input tap 867 1133")       
        """
        device.shell(f"input tap 256 1036")
        time.sleep(1.5)       
        device.shell(f"input tap 184 1266")
        time.sleep(1.5)
        device.shell(f"input text {getname}xxt")
        time.sleep(1.5)
        device.shell(f"input tap 865 1126")  



        
save()

def check():
    img = cv2.imread("screenshotphone.png",0)
    template = cv2.imread("gmail.png",0)
    h,w = template.shape

    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc

    bottom_right = (max_loc[0]+ w, max_loc[1] + h)
    cv2.rectangle(img2, max_loc, bottom_right, (0,0,255), 3)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

