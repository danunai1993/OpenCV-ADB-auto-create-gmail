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



images = ["listbar.png","addaccount.png","google2.png","makeaccbtn.png","makeacc.png",
            "dateacc.png","makeuser.png","makepass.png","phonenum.png","checkconfirm.png",
            "checkprivate.png"]

def checklistbar(images):
        img = cv2.resize(cv2.imread("screenshotphone.png",0), (0, 0), fx=0.4, fy=0.4)
        template = cv2.resize(cv2.imread(images,0), (0, 0), fx=0.8, fy=0.8)
        h,w = template.shape
        img2 = img.copy()
        
        #if images == "makeacc.png" or images == "dateacc.png" or images == "makeuser.png": 
        if images in ["makeacc.png","dateacc.png","makeuser.png","makepass.png","phonenum.png","checkconfirm.png","checkprivate.png"]:
            print(colored("[/] cv2.TM_CCOEFF!!",'green'))
            result = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            loc_xy = (max_loc[0]+ w, max_loc[1]+h)
            #print(loc_xy)
        else:
            print(colored("[/] cv2.TM_SQDIFF_NORMED!!",'green'))
            result = cv2.matchTemplate(img2, template, cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            loc_xy = (min_loc[0]+ w, min_loc[1]+h)
            #print(loc_xy)
        # print(cv2.rectangle(img2, min_loc, loc_xy, (0,0,255), 3))
        # cv2.rectangle(img2, min_loc, loc_xy, (0,0,255), 3)
        # cv2.imshow('Match', img2)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        if images == "listbar.png":
            print(colored("[/] Running listbar.png!!",'green'))
            if loc_xy == (63, 71):
                print(colored("[/] working listbar.png!!",'green'))
                time.sleep(.5)
                device.shell(f"input tap 950 163")
                time.sleep(.5)
                device.shell(f"input swipe 376 1950 376 336 1500")
                time.sleep(2.5)
            else:
                print(colored("[X] check listbar.png!!",'red'))
                return

        elif images == "addaccount.png":
            print(colored("[/] Running addaccount.png!!",'green'))
            if loc_xy == (76, 730):
                print(colored("[/] working addaccount.png!!",'green'))
                device.shell(f"input tap 350 1726")
                time.sleep(1.5)
            else:
                print(colored("[X] no check addaccount.png!!",'red'))
                return
        elif images == "google2.png":
            print(colored("[/] Running google2.png!!",'green'))
            if loc_xy == (58, 282):
                print(colored("[/] working google2.png!!",'green'))
                device.shell(f"input tap 267 662")
                time.sleep(4)
                device.shell(f"input text '272003'")
                time.sleep(9.5)
            else:
                print(colored("[X] no check google2.png!!",'red'))
                return
        elif images == "makeaccbtn.png":
            print(colored("[/] Running makeaccbtn.png!!",'green'))
            if loc_xy == (411, 838):
                print(colored("[/] working makeaccbtn.png!!",'green'))
                device.shell(f"input tap 150 2026")
                time.sleep(1.5)
                device.shell(f"input tap 198 1728")
                time.sleep(1.5)
            else:
                print(colored("[X] no check makeaccbtn.png!!",'red'))
                return
        elif images == "makeacc.png":
            print(colored("[/] Running makeacc.png!!",'green'))
            if loc_xy == (331, 225):
                print(colored("[/] working makeacc.png!!",'green'))
                device.shell(f"input tap 210 736")#กดชื่อ
                time.sleep(1.5)
                device.shell(f"input text {getname}")
                time.sleep(1.5)
                device.shell(f"input tap 168 971")#กดนามสกุล
                time.sleep(1.5)
                device.shell(f"input text {getlast}") 
                time.sleep(1.5)
                device.shell(f"input tap 350 1131")#กดที่วางในจอ
                time.sleep(1.5)
                device.shell(f"input tap 872 2019")#กดปุ่มถัดไป
                time.sleep(2.5)
            else:
                print(colored("[X] no check makeacc.png!!",'red'))
                return        
        elif images == "dateacc.png":
            print(colored("[/] Running dateacc.png!!",'green'))
            if loc_xy == (344, 227):
                print(colored("[/] working dateacc.png!!",'green'))
                device.shell(f"input tap 161 721")#กดปุ่มกรอกวันที่
                time.sleep(1.5)       
                device.shell(f"input text {day}")
                time.sleep(1.5)
                device.shell(f"input tap 514 729")#กดปุ่มเดือน
                time.sleep(1.5)
                device.shell(f"input tap 226 708")#เลือกเดือน
                time.sleep(1.5)
                device.shell(f"input tap 803 726")#กดปุ่มกรอกปี
                time.sleep(1.5)
                device.shell(f"input text {year}")
                time.sleep(1.5)
                device.shell(f"input tap 302 941")#กดปุ่มเพศ
                time.sleep(1.5)
                device.shell(f"input tap 267 1193")#เลือกเพศ
                time.sleep(1.5)
                device.shell(f"input tap 879 2021")#กดปุ่มถัดไป
                time.sleep(1.5)
            else:
                print(colored("[X] no check dateacc.png!!",'red'))
                return 
        elif images == "makeuser.png":
            print(colored("[/] Running makeuser.png!!",'green'))
            if loc_xy == (365, 187):
                print(colored("[/] working makeuser.png!!",'green'))
                device.shell(f"input tap 256 1036")#คลิกสร้างที่อยู่ gmail เอง
                time.sleep(1.5)
                device.shell(f"input tap 184 1266")#กดที่กรอก
                time.sleep(1.5)
                format = getname+word+str(day)
                device.shell(f"input text {format}")#กรอกgmail
                print(format)
                time.sleep(1.5)
                device.shell(f"input tap 865 1126")  #กดถัดไป
                time.sleep(1.5)
            else:
                print(colored("[X] no check makeuser.png!!",'red'))
                return
        elif images == "makepass.png":
            print(colored("[/] Running makepass.png!!",'green'))
            if loc_xy == (405, 247):
                print(colored("[/] working makepass.png!!",'green'))
                device.shell(f"input text {password}")#กรอก pass
                print(password)
                time.sleep(1.5)
                device.shell(f"input tap 235 1119")#กดที่ว่าง
                time.sleep(1.5)
                device.shell(f"input tap 872 2026") #กดถัดไป 
                time.sleep(1.5)
            else:
                print(colored("[X] no check makeuser.png!!",'red'))
                return          
        elif images == "phonenum.png":
            print(colored("[/] Running phonenum.png!!",'green'))
            if loc_xy == (375, 188):
                print(colored("[/] working phonenum.png!!",'green'))
                device.shell(f"input swipe 376 1950 376 336 1500")
                time.sleep(.5)
                device.shell(f"input tap 101 2030") #กดข้าม 
                time.sleep(1.5)
            else:
                print(colored("[X] no check phonenum.png!!",'red'))
                return 
        elif images == "checkconfirm.png":
            print(colored("[/] Running checkconfirm.png!!",'green'))
            if loc_xy == (412, 184):
                print(colored("[/] working checkconfirm.png!!",'green'))
                device.shell(f"input tap 856 2026") #กดถัดไป
                time.sleep(1.5)
            else:
                print(colored("[X] no check checkconfirm.png!!",'red'))
                return
        elif images == "checkprivate.png":
            print(colored("[/] Running checkprivate.png!!",'green'))
            if loc_xy == (378, 187):
                print(colored("[/] working checkprivate.png!!",'green'))
                device.shell(f"input swipe 376 1950 376 336 1500")
                time.sleep(.5)
                device.shell(f"input swipe 376 2000 376 336 1500")
                time.sleep(.5)
                device.shell(f"input tap 816 2021") #กดฉันยอมรับ 
                time.sleep(1.5)
                #หลังกด รอ 1นาที40วิ
            else:
                print(colored("[X] no check checkprivate.png!!",'red'))
                return 
save()
checklistbar(images[0]) 
save() 
checklistbar(images[1])  
save() 
checklistbar(images[2]) 
save() 
checklistbar(images[3]) 
save() 
checklistbar(images[4]) 
save() 
checklistbar(images[5]) 
save() 
checklistbar(images[6]) 
save() 
checklistbar(images[7])
save() 
checklistbar(images[8])
save() 
checklistbar(images[9])
save() 
checklistbar(images[10])
  

     
    

