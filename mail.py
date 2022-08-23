import cv2, time, numpy as np
import names, random, string
from ppadb.client import Client as AdbClient
from termcolor import colored

try:
    client = AdbClient(host="127.0.0.1",port=5037)
    devices = client.devices()
    device = devices[0]
    print(colored('[/] Connecting Driver Successfuly', 'green'))
except:
    print(colored('[X] No connection!! pls Connect your device', 'red'))

words = [
            "manste","noxze","ssad","medsw","lovex","loxsz","meyous","amsazte","sdrsd","opesee",
            "gorsd","messer","lnwst","tomsa","goodstr","saddss","eieisa","kuyria","noiza","newop",
            "suppua","appeal","apply","argument","artist","assistant","attempt","beat","beach","behavior",
            "capability","career","ceiling","chance","characterize","chief","chapter","clinic","colleague",
            "concentrate","course","darkness","desert","devote","device"
        ]
passwords = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(14))
        
word = random.choice(words)         #สุ่มคำ
getname = names.get_first_name()    #สร้างชื่อ
getlast = names.get_last_name()
day = random.randint(0,28)          #สุ่มวันเกิด
year = random.randint(1990,2000)    #สุ่มปีเกิด
password = passwords                #สุ่มรหัส

def save():
    with open("screenshotphone.png","wb")as f:
        f.write(device.screencap())
        time.sleep(0.3)
        print(colored("[/] Screenshot saved!!",'green'))



images = ["listbar.png","addaccount.png"]
def check(images):
        img = cv2.imread("screenshotphone.png",0)
        template = cv2.imread(images,0)
        h,w = template.shape
        img2 = img.copy()
        result = cv2.matchTemplate(img2, template, cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
        listbar = (min_loc[0]+ w, min_loc[1]+h)
        print(listbar)
        
        device.shell(f"input tap 950 163")
        time.sleep(.5)
        device.shell(f"input swipe 376 1950 376 336 1500")
        time.sleep(.5)
        device.shell(f"input tap 350 1726")
        time.sleep(.5)
        device.shell(f"input tap 267 662")
        time.sleep(3.5)
        device.shell(f"input text '272003'")
        time.sleep(6)
        device.shell(f"input tap 150 2026")
        time.sleep(1.5)
        device.shell(f"input tap 198 1728")
        time.sleep(1.5)
        device.shell(f"input tap 210 736")#กดชื่อ
        time.sleep(1.5)
        device.shell(f"input text {getname}")
        time.sleep(1.5)
        device.shell(f"input tap 168 971")#กดนามสกุล
        time.sleep(1.5)
        device.shell(f"input text {getlast}") 
        time.sleep(1.5)
        device.shell(f"input tap 350 1131")
        time.sleep(1.5)
        device.shell(f"input tap 872 2019")
        time.sleep(1.5)
        device.shell(f"input tap 161 721")
        time.sleep(1.5)       
        device.shell(f"input text {day}")
        time.sleep(1.5)
        device.shell(f"input tap 514 729")
        time.sleep(1.5)
        device.shell(f"input tap 226 708")
        time.sleep(1.5)
        device.shell(f"input tap 803 726")
        time.sleep(1.5)
        device.shell(f"input text {year}")
        time.sleep(1.5)
        device.shell(f"input tap 302 941")
        time.sleep(1.5)
        device.shell(f"input tap 267 1193")
        time.sleep(1.5)
        device.shell(f"input tap 879 2021")
        time.sleep(1.5)
        device.shell(f"input tap 256 1036")
        time.sleep(1.5)       
        device.shell(f"input tap 184 1266")
        time.sleep(1.5)
        device.shell(f"input text {getname}{word}{day}")
        print(getname,word,day)
        time.sleep(1.5)
        device.shell(f"input tap 865 1126")  
        time.sleep(1.5)
        device.shell(f"input text {password}")
        print(password)
        time.sleep(1.5)
        device.shell(f"input tap 872 2026")  
        

        txt = open("gmail.txt","a")
        user = getname + word + '{day}' + "@gmail.com || " + password + "\n"
        txt.write(user)
        print(user)
        txt.close()

save()
check(images[0])   
     
    

