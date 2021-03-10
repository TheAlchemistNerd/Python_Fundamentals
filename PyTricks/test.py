def fn1():
	print('Hello:  ', end = '')
	return (1)

def fn2():
	print('Goodbye', end = '')
	return(2)

def test(func):
	print('testing', func.__name__, 'Output =', func())

def main():
	print('In program', __file__)

	test(fn1)

	test(fn2)
