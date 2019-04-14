import math

array = [0,155,155,155,155,155,155,155,155,155,155,155,155,155,155,155]
mul = [0,1,4,9,19,30,41,47,50,47,41,30,19,9,4,1]

outter_count = 15
while outter_count >= 0:

	count = 15
	result = 0
	mul_sum = 0
	while count >= 0:
		result += array[count]*mul[count]
		mul_sum += mul[count]
		count -= 1
	result //= mul_sum
	print(result)
	outter_count -= 1
	
	#if outter_count >= 10:
		#array[outter_count+1] = 140
	#else:
	#	array[outter_count+1] = 140
	#	array[outter_count+6] = 155
	
	array[outter_count+1] = 140
	
	#print(array)
	
