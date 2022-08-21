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


