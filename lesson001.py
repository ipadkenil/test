'''
第一次使用 Python
'''
print('Python 第一次練習\n')
name = input('請輸入您的名字：')
print(name , '觀迎您來到 Python 的世界')


'''
比較符號之結果會變成布林值
'''
x = 5
print(x == 5)	# 因 x = 5 ，所以這行的執行結果會等於 True  ， == 為等於符號
print(x != 5)	# 因 x = 5 ，所以這行的執行結果會等於 False ， != 為不等於符號
print(x < 5)	# False
print(x <= 5)	# True
print(x > 5)	# False
print(x >= 5)	# True

'''
if 架構，在Python裡，縮排的觀念要先建立起來
'''
anser = input('今天有下雨嗎？')
if anser == '有' :
	print('出門前記得帶傘！')
elif anser == '沒有' :
	print('出門不必帶傘！')
elif anser == '不知道' or anser == '不確定' :
	print('出門前先確認有沒有下雨')
else :
	print('請認真回答問題！！')
	