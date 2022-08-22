import time
from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]
print(f'Device: {device}')

with open("screenshot.png", "wb") as f:
    f.write(device.screencap())
    time.sleep(0.3)
    print("Screenshot saved")