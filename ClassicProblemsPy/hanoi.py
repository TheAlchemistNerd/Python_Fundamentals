class Stack():
	""" a stack class to implement the towers of hanoi
	    with push method to add discs and pop methods to remove
	    a disc and return the disc
	"""

	def __init__(self):
		self._container = []

	def push(self, item):
		self._container.append(item)

	def pop(self):
		return self._container.pop()

	def __repr__(self):
		return repr(self._container)

num_discs = int(input("Enter the number of discs in the first tower: "))
tower_a = Stack()
tower_b = Stack()
tower_c = Stack()

for i in range(1, num_discs + 1):
	tower_a.push(1)

def hanoi(begin, end, temp, n):
	""" a recursive function to move the discs
		through the towers of hanoi
	"""
	if n == 1:     # base case
		end.push(begin.pop())
	else:
		hanoi(begin, temp, end,  n-1)
		hanoi(begin, end, temp, 1)
		hanoi(temp, end, begin, n -1)

if __name__ == '__main__':
	hanoi(tower_a, tower_b, tower_c, num_discs)
	print(tower_a)
	print(tower_b)
	print(tower_c)