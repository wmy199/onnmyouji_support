import cv2
import os
import settings
import check
import time
import re


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
<<<<<<< HEAD
already = settings.already
=======
>>>>>>> ae1fb69f2376cc3155dbaa3f3afa054134204b97

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
		rx, ry = check.get_randomxy(x_victory, y_victory) 
		check.click(rx,ry)
		check.get_randomtime(0.5,1)

	if res_max_defeat > 0.9:
		print('\n战斗失败,结算中',end='--',flush=True)
		vote[2]=1
		end_time = time.time()		
		#rx,ry = check.get_randomxy([900*settings.resize_Magnification,350*settings.resize_Magnification],[1000*settings.resize_Magnification,400*settings.resize_Magnification])
		rx, ry = check.get_randomxy(x_defeat, y_defeat) 
		check.click(rx,ry)
		check.get_randomtime(0.5,1)

<<<<<<< HEAD

story_skip =settings.story_skip
story_battle = settings.story_battle
story_conversation = settings.story_conversation
story_conversation_1 = settings.story_conversation_1
story_eye = settings.story_eye

def check_and_click(img,template):
	x,y,res = check.match(img,template)
	if res >0.9:
		x,y = check.get_randomxy(x,y)
		check.get_randomtime(0.5,1)
		check.click(x,y)
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
	


def get_choice():
	choice = input('请输入数字来选择:\n1 御魂,御灵,业原火;\n2 剧情;\n3 还在做，先等一下;\n')
=======
	

def get_choice():
	choice = input('请输入数字来选择:\n1 御魂,御灵,业原火;\n2 还在做，先等一下;\n')
>>>>>>> ae1fb69f2376cc3155dbaa3f3afa054134204b97
	if not choice.isdigit() is True:
		print('只能输入数字')
		get_choice(choice)
	else:
<<<<<<< HEAD
		print('任务开始')
=======
>>>>>>> ae1fb69f2376cc3155dbaa3f3afa054134204b97
		return choice
		
state = ''
choice = get_choice()
if choice == '1':
	state = 'yuhun'	
<<<<<<< HEAD
if choice == '2':
	state = 'story'
while True:
	if state == 'yuhun':
		yuhun()
	if state == 'story':
		story()
=======
while True:
	if state == 'yuhun':
		yuhun()
>>>>>>> ae1fb69f2376cc3155dbaa3f3afa054134204b97

print('刷完了')


