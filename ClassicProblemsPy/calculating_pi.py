
def calculate_pi(n_terms):
	""" calculating pi using Leibniz formula:
		pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ...
	"""
	numerator = 4.0
	denominator = 1.0
	operation = 1.0
	pi = 0.0

	for _ in range(n_terms):
		pi += operation * (numerator / denominator)
		denominator += 2.0
		operation *= - 1.0
	return pi

if __name__ == '__main__':
	print(calculate_pi(1000000))