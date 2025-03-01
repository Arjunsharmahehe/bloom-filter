# Bloom Filter Implementation

## Overview
This is a simple implementation of a **Bloom Filter**, a probabilistic data structure that efficiently checks whether an element is present in a set. It provides fast insertions and lookups with a trade-off: **false positives are possible, but false negatives are not**.

## Features
- Uses multiple hash functions to map elements into a **bit array**.
- Supports **insertions** and **lookups**.
- Implements a function to compute the **false positive rate**.

## Dependencies
This implementation requires the `bitarray` library. You can install it using:
```sh
pip install bitarray
```

## How It Works
1. **Insertion**: Each item is hashed using multiple hash functions, and the corresponding bits in the bit array are set to `1`.
2. **Lookup**: The item is hashed again, and if all the corresponding bits are `1`, the item may be in the set (with some probability of false positives).
3. **False Positive Rate**: The probability of false positives is estimated using the formula:
   
   $(1 - e^{-kn/m})^k$

   where:
   - `n` = number of inserted elements
   - `m` = size of the bit array
   - `k` = number of hash functions

## Usage
### Example
```python
from bloom_filter import BloomFilter

# Initialize Bloom Filter with size 1000 and 5 hash functions
bf = BloomFilter(1000, 5)

# Insert values
bf.insert("apple")
bf.insert("banana")

# Lookup values
print(bf.lookup("apple"))  # True
print(bf.lookup("grape"))   # False (most likely)

# Check estimated false positive rate
print(f"False Positive Rate: {bf.false_positive_rate() * 100:.2f}%")
```

## Notes
- This implementation uses **SHA-256** for hashing.
- A **larger bit array and more hash functions reduce false positives**, but at the cost of increased space and computation.
- The number of hash functions should be chosen optimally using:
  
  
  $k = \frac{m}{n} \ln 2$

## License
This project is open-source and free to use under the MIT License.


