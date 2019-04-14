import os,re,cv2

def imgload(path,resize_Magnification):
   img = cv2.imread(path)
   h,w =img.shape[0:2]
   img = cv2.resize(img,(int(w*resize_Magnification),int(h*resize_Magnification)))
   img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   return img



adb_connect = 'adb connect 127.0.0.1:5555'
os.system(adb_connect)
device = ''
start = 'img/start.png'
end_victory = 'img/end_victory.png'
end_defeat = 'img/end_defeat.png'


origin =[1440,810]
os.system('adb %s shell wm size > 1.txt' % device)
with open('1.txt','r') as f:
   window_info_str = f.read()
wis = re.findall(r'\d*x\d*',window_info_str)
print(wis)
window_info = re.findall(r'\d+',wis[0])
window_width = int(window_info[0])
window_height = int(window_info[1])
resize_Magnification = window_width/origin[0]
print(window_width,window_height)

start = imgload(start,resize_Magnification)
end_victory = imgload(end_victory,resize_Magnification)
end_defeat = imgload(end_defeat,resize_Magnification)