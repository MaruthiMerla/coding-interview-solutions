# Bitwise Matching Pattern


```python
from solution import next_number_with_same_bits, next_number_with_same_bits_bitwise

n = 6  # binary 110
next_num = next_number_with_same_bits(n)
print(next_num)  # 9 (binary 1001)

# More efficient bitwise version
next_num = next_number_with_same_bits_bitwise(n)
print(next_num)  # 9