while True:
	print ("""
	1. addition
	2. subtraction
	3. multiplication
	4. division
	5. modulo
	6. square root
	7. close calculator 
	""")
	
	a = int(input("please choose from the menu : ")) 
	if a >= 1 and a <= 5:
		b = int(input ("enter first number : " ))
		c = int(input ("enter second number : " ))
		if a == 1:
			ans = b + c
			print (b, '+', c, '=', ans)
		elif a == 2:
			ans = b - c
			print (b, '-', c, '=', ans)
		elif a == 3:
				ans = b * c
				print (b, '*', c, '=', ans)
		elif a == 4:
				ans = b / c
				print (b, '/', c, '=', ans)
		elif a == 5:
				ans = b % c
				print (b, '%', c, '=', ans)
	elif a == 6:
		from math import sqrt
		d = int (input  ("choose a number : "))
		ans = sqrt (d)
		print ('square root of', d, '=', ans)
	elif a == 7:
		break
	else:
		print ("please make a selection from the menu")
