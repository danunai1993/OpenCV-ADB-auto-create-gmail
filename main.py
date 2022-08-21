import cv2,time,numpy
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

data = ['gmail.png','slack.png','whatsapp.png','facebook.png','twitter.png','instagram.png','linkedin.png','youtube.png']

def check(imagecheck):
    item = cv2.imread(imagecheck)
    screen = cv2.imread("screenshot.png")
    # cv2.imshow('',item)
    # cv2.waitKey()
    result = cv2.matchTemplate(item,screen,cv2.TM_SQDIFF_NORMED)
    loc_cut = numpy.where(result<=0.03)
    loc_xy = list(zip(*loc_cut[::-1]))
    print(loc_xy)
    for i in loc_xy:
        device.shell(f'input tap {i[0]} {i[1]}')
        print({i[0]}, {i[1]})
        return

save()
check('gmail.png')
