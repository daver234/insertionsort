import random
import time

start_time = time.time()

def randomlist(amount):
	list3 = []
	for i in range(0,amount):
		new = random.randint(0,10000)
		list3.append(new)
	print "here"
	insertionsort(list3)


def insertionsort(list):
	#print(list)
	
	for num in range(1,len(list)):
		print num

		ivalue = list[num]
		local = num

		while local > 0 and list[local-1] > ivalue:
			print "local is:",local,"local-1 is:", local-1, "ivalue:",ivalue
			list[local] = list[local -1]
			local = local -1

		list[local] = ivalue
	print list		 
			

#list =[3,1,5,6,9,0]
#insertionsort(list)


randomlist(5)
print "I am done"
print("--- %s seconds ---" % (time.time() - start_time))