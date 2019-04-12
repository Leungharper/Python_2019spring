# coding:utf-8
# 【递归函数】汉诺塔 {包括输入盘子数、输出步骤、步数}


def move(n,a,b,c,x=0):	# x为默认参数
	if n == 1:
		print(a,'-->',c)
		x += 1
	else:
		x = move(n-1,a,c,b,x)
		x =move(1,  a,b,c,x)
		x =move(n-1,b,a,c,x)
	return x

flag = 'Y'
while flag != 'N' and flag != 'n':
	num = input('输入A柱的盘子数：')
	num = int(num)
	x = move(num,'A','B','C')
	print ('\n步数：',x)
	
	flag = input('\n继续？(Y/N) ')

input('\n----(输入任意键并)按回车结束----\n')
