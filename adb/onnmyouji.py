import cv2
import os
import settings
import check
import time
import re
from functools import wraps

# tiaozhan = cv2.imread(settings.tiaozhan)
# h,w =tiaozhan.shape[0:2]
# tiaozhan = cv2.resize(tiaozhan,(int(w*settings.resize_Magnification),int(h*settings.resize_Magnification)))
# tiaozhan = cv2.cvtColor(tiaozhan,cv2.COLOR_BGR2GRAY)

# _end = cv2.imread(settings.end)
# he,we = _end.shape[0:2]
# _end = cv2.resize(_end,(int(we*settings.resize_Magnification),int(he*settings.resize_Magnification)))
# _end = cv2.cvtColor(_end,cv2.COLOR_BGR2GRAY)
start = settings.start
end_victory = settings.end_victory
end_defeat = settings.end_defeat
already = settings.already

mx,my = 0,0
start_time = time.time()
end_time = time.time()
count=0
vote=[1,1,1]
def yuhun():
	global start_time,end_time,count,vote

		
	img = check.get_screen()

	x, y,res_max = check.match(img, start)
	if res_max>0.9:
		if sum(vote) == 3:
			if count != 0:
				print('\n用时'+str(end_time-start_time),end='秒\n',flush=True)
			count+=1
			vote=[0,0,0]
			print('\n第%d场' % count)
			print('\n开始界面,准备点击',flush=True)
		vote=[1,0,0]
		start_time = time.time()
		rx, ry = check.get_randomxy(x, y)
		check.get_randomtime(0.5, 1)
		check.click(rx, ry)
		
		return

	
	# res = cv2.matchTemplate(img,_end, cv2.TM_CCOEFF_NORMED)
	x_victory, y_victory,res_max_victory = check.match(img, end_victory)
	x_defeat, y_defeat,res_max_defeat = check.match(img, end_defeat)
	x_end,y_end,res_end = check.match(img,settings.end)
	# print(res_max_victory)
	# print(res_max_defeat)
	if res_max_defeat < 0.9 and res_max_victory < 0.9:
		if sum(vote) != 3:
			print('战斗中',end='--',flush=True)
		vote[1]=1
		time.sleep(3)
		return
		
	if res_max_victory > 0.9:
		print('\n战斗胜利,结算中',end='--',flush=True)
		vote[2]=1
		end_time = time.time()		
		#rx,ry = check.get_randomxy([900*settings.resize_Magnification,350*settings.resize_Magnification],[1000*settings.resize_Magnification,400*settings.resize_Magnification])
		rx, ry = check.get_randomxy(x_end, y_end) 
		check.click(rx,ry)
		check.get_randomtime(0.5,1)

	if res_max_defeat > 0.9:
		print('\n战斗失败,结算中',end='--',flush=True)
		vote[2]=1
		end_time = time.time()		
		#rx,ry = check.get_randomxy([900*settings.resize_Magnification,350*settings.resize_Magnification],[1000*settings.resize_Magnification,400*settings.resize_Magnification])
		rx, ry = check.get_randomxy(x_end, y_end) 
		check.click(rx,ry)
		check.get_randomtime(0.5,1)


story_skip =settings.story_skip
story_battle = settings.story_battle
story_conversation = settings.story_conversation
story_conversation_1 = settings.story_conversation_1
story_eye = settings.story_eye
story_animation_skip = settings.story_animation_skip
story_animation_close = settings.story_animation_close

scale = 0.9
def check_and_click(img,template):
	x,y,res = check.match(img,template)
	if res > scale:
		x,y = check.get_randomxy(x,y)
		check.click(x,y)
		check.get_randomtime(0.5,1)
		return True
	return False


def story():
	img = check.get_screen()
	res =  check_and_click(img,story_conversation)
	if res:
		return
	check_and_click(img,story_skip)
	if res:
		return
	res = check_and_click(img,already)
	if res:
		return
	res = check_and_click(img,story_battle)
	if res:
		return
	res = check_and_click(img,end_victory)
	if res:
		return
	res = check_and_click(img,story_conversation_1)
	if res:
		return
	res = check_and_click(img,story_eye)
	if res:
		return
	res = check_and_click(img,story_animation_skip)
	if res:
		return
	res = check_and_click(img,story_animation_close)
	if res:
		return

inround = False
members = 0;
def teamwork():
	global inround,start_time,end_time,count,members
	img = check.get_screen()

	if members == 2:
		if check.match(img,settings.team_two)[2] > 0.9:
			res = check_and_click(img,settings.team_start)
			if res:
				if not inround:
					inround = True
					count+=1
					print('\n\n战斗开始,第%d场' % count)
					start_time = time.time()
				return
	else:
		if check.match(img,settings.team_three)[2] > 0.9:
			res = check_and_click(img,settings.team_start)
			if res:
				if not inround:
					inround = True
					count+=1
					print('\n\n战斗开始,第%d场' % count)
					start_time = time.time()
				return



	res = check_and_click(img,settings.end)
	if res:
		if inround:
			end_time = time.time()
			print('\n战斗胜利,用时%d秒' % int(end_time-start_time))
			inround = False
		return

	if inround:
		print('战斗中',end = '--',flush=True)
		
#wakajimaibendou
wakajimachousen = settings.wakajimachousen
def wakajimaibendo():
	img = check.get_screen()
	res = check_and_click(img,wakajimachousen)
	if res:
		return
	res = check_and_click(img,already)
	if res:
		return
	res = check_and_click(img,end_victory)
	if res:
		return
	res = check_and_click(img,end_defeat)
	if res:
		return
is_out = False
def quick_create(*imgs):
	def reg(fun):
		@wraps(fun)
		def myfun():
			img = check.get_screen()
			res = fun(img)
			if res:
				return		
			for each in imgs:
				if check_and_click(img,each):
					return	
				
		return myfun
	return reg

@quick_create(settings.pvp,settings.already,settings.end,settings.auto)
def pvp(img):
	return

@quick_create(settings.imgload('eventimg/tj.png',settings.resize_Magnification)
	,settings.imgload('eventimg/ji.png',settings.resize_Magnification)
	,settings.team_start
	,settings.already
	,settings.end
	)
def test(img):
	return

@quick_create(settings.end_victory,settings.end_defeat,settings.yes,settings.kekkai_flush)
def kekkai(img):
	arr = (settings.kekkai_0_6,settings.kekkai_0_30)
	for each in arr:
		x,y,res = check.match(img, each)
		print(res)
		if res >0.98:
			return True
	for each in (settings.kekkai_click,settings.kekkai_target):
		x,y,res = check.match(img, each)
		print(res)
		if res >0.94:
			x,y=check.get_randomxy(x,y)
			check.click(x,y)
			check.get_randomtime(0.5,1)		
			return True
	return	False
class GameSupport(object):
	"""docstring for GameSupport"""
	def __init__(self, *relavtice_img,**absolute_img):
		self.relavtice_img = []
		self.absolute_img = []
		for each in relavtice_img:
			self.relavtice_img.append(cv2.imread(each,0))
		for name,v in absolute_img:
			self.absolute_img.append(cv2.imread(v,0))

	def get_screen():
		imgpath = 'img/'+settings.device+'/screen.png'
		path = 'img/'+settings.device
		if not os.path.exists(path):
			os.makedirs(path)
		cmd_send = "adb -s %s shell screencap -p > %s " % (settings.device,imgpath)
		os.system(cmd_send)
		with open(imgpath,'ab+') as f:
			f.seek(0)
			img = f.read()
			img = img.replace(b'\r\r\n',b'\n')
			f.truncate(0)
			f.write(img)
		img = cv2.imread(imgpath,0)
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

	scale = 0.9
	def check_and_click(img,template):
		x,y,res = match(img,template)
		if res > self.scale:
			x,y = get_randomxy(x,y)
			click(x,y)
			get_randomtime(0.5,1)
			return True
		return False

	def update(self):
		img = get_screen()
		pos = []
		count = 0
		for name,val in self.absolute_img.items():
			lt,rb,res = match(img, val)
			if res>0.9:
				count+=1
			x = lt[0]+rb[0]
			y = lt[1]+rb[1]
			pos.append((x/2,y/2))
		position = [0,0]
		for each in pos:
			position[0]+=each[0]
			position[1]+=each[1]
		position[0] = position[0]/position.count
		position[1] = position[1]/position.count
		if count==absolute_img.items.count():
			click(position[0], position[1])
		
		for each in self.relavtice_img:
			res = check_and_click(img, each)
			if res:
				return


def get_choice():
	choice = input('请输入数字来选择:\n1 御魂,御灵,业原火;\n2 剧情;\n3 离岛活动;\n4组队;\n5斗技;\n6结界突破;\n7还在做，先等一下;\n999测试\n')
	if not choice.isdigit() is True:
		print('只能输入数字')
		get_choice(choice)
	else:
		print('任务开始')
		return choice
state = ''
choice = get_choice()
if choice == '1':
	state = 'yuhun'	
elif choice == '2':
	state = 'story'
elif choice == '3':
	state = 'ibendo'
elif choice == '4':
	members = int(input('请输入人数(2 or 3)\n'))
	state ='team'
elif choice == '5':
	state = 'pvp'
elif choice == '6':
	scale = 0.8
	state = 'kekkai'
elif choice == '999':
	state = 'test'
elif choice == '0':
	check.get_screen()
else:
	print('不存在的')
while True:
	try:
		if state == 'yuhun':
			yuhun()
		elif state == 'story':
			story()
		elif state == 'ibendo':
			wakajimaibendo()
		elif state == 'team':
			teamwork()
		elif state == 'pvp':
			pvp()
			print(pvp.__name__)
		elif state == 'kekkai':
			kekkai()
		elif state == 'test':
			test()
	except Exception as exc:
		pass

print('done')


