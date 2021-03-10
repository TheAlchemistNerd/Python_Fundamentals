from enum import IntEnum

Nucleotide = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

codon = Nucleotide, Nucleotide, Nucleotide    # tuple
Gene = list(codon)

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def string_to_gene(s):
	gene = []
	for i in range(0, len(s), 3):
		if (i + 2) >= len(s):	# don't run off end!
			return gene

		# Initialize codon out of three nucleotides
		codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
		gene.append(codon)	# add codon to gene
	return gene

my_gene = string_to_gene(gene_str)


# linear search
def linear_contains(gene, key_codon):
	for codon in gene:
		if codon == key_codon:
			return True
	return False

acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))


# binary search
def binary_contains(gene, key_codon):
	low = 0
	high = len(gene) - 1
	while low <= high:	# while there is still some search space
		mid = (low + high) // 2
		if gene[mid] < key_codon:
			high = mid + 1
		elif gene[mid] > key_codon:
			high = mid - 1
		else:
			return True
	return False

my_sorted_gene = sorted(my_gene)
print(binary_contains(my_gene, acg))
print(binary_contains(my_gene, gat))
