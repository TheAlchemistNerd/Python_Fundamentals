class CompressionGene:
    def __init__(self, gene):
        self._compress(gene)
    def _compress(self, gene):
        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2         # shift left two bits
            if nucleotide == "A":         # change the last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C":       # change the last  two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":       # change the last two bits to 10
                self.bit_string |= 0b01
            elif nucleotide == "T":        # change the last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self):
        gene = ""
        for i in range(0, self.bit_string.bit_length() -1, 2):   # -1 to exclude sentinel
            bits = self.bit_string >> i & 0b11   # get just 2 relevant bits
            if bits == 0b00:    # A
                gene += "A"
            elif bits == 0b01:    # C
                gene += "C"
            elif bits == 0b10:    # G
                gene += "G"
            elif bits == 0b11:    # T
                gene += "T"
            else:
                raise ValueError("Invalid bits: {}". format(bits))
            return gene[::-1]    # [::-1] reverses string by slicing backward
    def __str__(self):    # string representation for pretty printing
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof
    original = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed = CompressionGene(original)    # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print ("original and decompressed are the same: {}". format(original == compressed.decompress()))