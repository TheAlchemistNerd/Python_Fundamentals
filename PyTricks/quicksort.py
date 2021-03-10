import time
from random import randint

def quickSort(array):
	if len(array) <= 1: return array
	return quickSort([x for x in array[1:] if x < array[0]]) \
	       + [array[0]]					\
		+ quickSort([x for x in array[1:] if x >= array[0]])

nums =[randint(0, 100) for x in range(5000)]
start_time = time.time()
quickSort(nums)
end_time = time.time() - start_time
print("Elapsed time for Quick sort: {}". format(end_time))
