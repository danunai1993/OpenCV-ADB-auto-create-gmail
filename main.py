import cv2,time,numpy
from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.device()
device = devices[0]
print('device:',device)