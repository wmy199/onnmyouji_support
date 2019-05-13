import os,re,cv2

def imgload(path,resize_Magnification):
   img = cv2.imread(path)
   h,w =img.shape[0:2]
   img = cv2.resize(img,(int(w*resize_Magnification),int(h*resize_Magnification)))
   img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   return img



adb_connect = 'adb connect 127.0.0.1:5555'
os.system(adb_connect)

os.system('adb devices > devices.txt')
with open('devices.txt','r') as f:
   devices = f.read()
container = []
numitem = re.findall(r'[a-z]*-\d*',devices)
stritem = re.findall(r'\d*\.\d*\.\d*\.\d*:\d*',devices)
devices = numitem+stritem
dct = 1
s= ''
for each in devices:
   s+=('\n'+str(dct)+' '+each)
   dct+=1

print('请选择设备：')
device = input('%s\n' % s)
if device.isdigit():
   device = int(device)
device = devices[device-1]
print('已连接%s' % device)
start = 'img/start.png'
end_victory = 'img/end_victory.png'
end = 'img/end.png'
end_defeat = 'img/end_defeat.png'
already = 'img/already.png'
#剧情图片模板

story_skip = 'img/skip.png'
story_battle = 'img/battle.png'
story_conversation = 'img/conversation.png'
story_conversation_1 = 'img/conversation_1.png'
story_eye = 'img/eye.png'
story_animation_skip = 'img/animation_skip.png'
story_animation_close = 'img/animation_close.png'

#离岛活动
wakajimachousen = 'img/wakajimaibendo/wakajimachousen.png'



origin =[1440,810]
os.system('adb -s %s shell wm size > 1.txt' % device)
with open('1.txt','r') as f:
   window_info_str = f.read()
wis = re.findall(r'\d*x\d*',window_info_str)
print(wis)
window_info = re.findall(r'\d+',wis[0])
window_width = int(window_info[0])
window_height = int(window_info[1])
resize_Magnification = window_width/origin[0]
print('当前设备分辨率:')
print(window_width,window_height)

start = imgload(start,resize_Magnification)
end_victory = imgload(end_victory,resize_Magnification)
end_defeat = imgload(end_defeat,resize_Magnification)
end = imgload(end,resize_Magnification)
yes = imgload('img/yes.png',resize_Magnification)

already = imgload(already,resize_Magnification)
story_battle = imgload(story_battle,resize_Magnification)
story_conversation = imgload(story_conversation,resize_Magnification)
story_conversation_1 = imgload(story_conversation_1,resize_Magnification)
story_skip = imgload(story_skip,resize_Magnification)
story_eye = imgload(story_eye,resize_Magnification)
story_animation_skip = imgload(story_animation_skip,resize_Magnification)
story_animation_close = imgload(story_animation_close,resize_Magnification)

#team
wakajimachousen = imgload(wakajimachousen,resize_Magnification)
team_start = imgload('img/team_start.png',resize_Magnification)
team_two = imgload('img/team_two.png',resize_Magnification)
team_three = imgload('img/team_three.png',resize_Magnification)

#pvp
pvp = imgload('img/pvp.png',resize_Magnification)
auto = imgload('img/auto.png',resize_Magnification)
event_wsjl = imgload('eventimg/wsjl.png',resize_Magnification)

#kekkai
kekkai_flush = imgload('img/flush.png',resize_Magnification)
kekkai_target = imgload('img/kekkai-target.png',resize_Magnification)
kekkai_click = imgload('img/kekkai-click.png',resize_Magnification)
kekkai_0_6 = imgload('img/kekkai-0-6.png',resize_Magnification)
kekkai_0_30 = imgload('img/kekkai-0-30.png',resize_Magnification)