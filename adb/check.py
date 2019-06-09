import os
import cv2
import random
import time
import settings
import threading
# def sendandpull(imgpath):
# 	cmd_send = 'adb -s %s shell screencap -p sdcard/screen.png' % settings.device
# 	cmd_pull = 'adb -s %s pull sdcard/screen.png %s' % (settings.device,imgpath)
# 	os.system(cmd_send)
# 	os.system(cmd_pull)
# 	print('done')

def get_screen():
	# cmd_get = 'adb shell screencap -p /sdcard/screen_img.png'
	# cmd_send = 'adb pull sdcard/screen_img.png img/test.png'
	imgpath = 'img/'+settings.device+'/screen.png'
	path = 'img/'+settings.device
	if not os.path.exists(path):
		os.makedirs(path)
	cmd_send = "adb -s %s shell screencap -p > %s " % (settings.device,imgpath)
	#cmd_send = 'adb -s %s shell screencap -p sdcard/screen.png' % settings.device
	#cmd_pull = 'adb -s %s pull sdcard/screen.png %s' % (settings.device,imgpath)
	#os.system(cmd_get)
	os.system(cmd_send)
	#a = os.system(cmd_pull)
	# t = threading.Thread(target=sendandpull,args=(imgpath,))
	# t.start()
	# t.join()
	with open(imgpath,'ab+') as f:
		f.seek(0)
		img = f.read()
		img = img.replace(b'\r\r\n',b'\n')
		f.truncate(0)
		f.write(img)

	
	#time.sleep(1)
	# try:
	# 	with open(imgpath,'wb+') as f:
	# 		f.write(img)
	# except OSError as e:
	# 	with open(imgpath,'wb+') as f:
	# 		f.write(img)
	img = cv2.imread(imgpath,0)
	#os.system('del %s' % imgpath.replace('/','\\'))
	return img


def match(img, template):
	res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
	h,w =template.shape[:2]
	min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
	left_top = max_loc
	right_bottom = (max_loc[0]+w,max_loc[1]+h)
	
	return left_top,right_bottom,res.max()


def get_randomxy(x, y):
	
	xc = random.randint(int(x[0]), int(y[0]))
	yc = random.randint(int(x[1]), int(y[1]))
	return xc,yc

def get_randomtime(a, b):
    """产生a,b间的随机时间延迟"""
    time.sleep(random.uniform(a, b))


def click(x, y):
    """输入两个二维列表，表示要点击的位置的x坐标，y坐标"""
    cmd_click = 'adb -s %s shell input tap {} {}'.format(x, y) % settings.device
    #print('%s,%s' % (x,y))
    os.system(cmd_click)
