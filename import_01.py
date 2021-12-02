import random  #python
import os

random_01 = random.randint(1, 100) #rand + int 產生隨機整數 包含頭尾
print(random_01)

print('---------------------------猜數字遊戲開始------------------------------')
answer_01 = input('請輸入你要猜的數字(1-100)! 有五次機會喔')
answer_01 = int(answer_01)
chances = 5
while chances > 1:
	if answer_01 == random_01:
		print('好厲害喔猜對了')
		os._exit() 
	elif answer_01 > random_01:
		chances = chances - 1
		print('猜錯囉!太大了!剩餘次數: ', chances)
		answer_01 = input('請輸入你要猜的數字(1-100)!')
		answer_01 = int(answer_01)
	elif answer_01 < random_01:
		chances = chances - 1
		print('猜錯囉!太小了!剩餘次數: ', chances)
		answer_01 = input('請輸入你要猜的數字(1-100)!')
		answer_01 = int(answer_01)

print('沒機會了喔遊戲結束')
os._exit() 

