import cv2,time,numpy
from ppadb.client import Client as AdbClient

client = AdbClient(host="localhost", port=5037)
devices = client.devices()
device = devices[0]
print(f'Device: {device}')

def save():
    with open("screenshot.png", "wb") as f:
        f.write(device.screencap())
        time.sleep(0.3)
        print("Screenshot saved")

data = ['gmail.png']

def check(images):
    item = cv2.imread(images)
    screen = cv2.imread("screenshot.png")
    result = cv2.matchTemplate(screen, item, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(result <= 0.2)
    loc_xy = list(zip(*loc[::-1]))
    print(loc_xy)

    for i in loc_xy:
        device.shell(f"input tap {i[0]} {i[1]}")
        #device.touch(i[0]+10, i[1]+10, "DOWN_AND_UP")
        #cv2.rectangle(screen, i, (i[0] + item.shape[1], i[1] + item.shape[0]), (0, 255, 0), 2)
        print(i[0]+10,i[1]+10)
        save()
        return

save()
check(data[0])
