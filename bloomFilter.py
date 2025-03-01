import hashlib  # For hashing functions
import math 
from bitarray import bitarray   # To use a bit array and not an int array

def hash_function(data, seed, size):
    hash_value = int(hashlib.sha256((str(seed) + data).encode()).hexdigest(), 16)

    # % size to get a number <= the size of the bit array
    return hash_value % size

class BloomFilter:
    def __init__(self, size, hash_nums):
        self.size = size
        self.hash_nums = hash_nums
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
        self.inserted_count = 0

    # To print a array in a beautiful manner
    def __str__(self):
        return f"[ {" ".join([str(i) for i in self.bit_array])} ]"

    def insert(self, value):

        # adding multiple hashes to the bitarray with i as a seed
        for i in range(self.hash_nums):
            index = hash_function(value, i, self.size)
            self.bit_array[index] = 1
        self.inserted_count += 1

    def lookup(self, value):
        for i in range(self.hash_nums):
            index = hash_function(value, i, self.size)
            if self.bit_array[index] == 0:
                return False
        return True

    # Calculating the rate of false positives
    # A rate of less than or equal to 1 percent is acceptable
    def false_positive_rate(self):
        n = self.inserted_count
        m = self.size
        k = self.hash_nums
        if n == 0:
            return 0
        return (1 - math.exp(-k*n/m))**k

def main():
    bf = BloomFilter(10, 3)
    print(bf)
    bf.insert("apple")
    print(bf)

if __name__ == "__main__":
    main()
