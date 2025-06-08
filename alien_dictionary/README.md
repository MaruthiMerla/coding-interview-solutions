# Alien Dictionary

This solution determines the character order of an alien language from a sorted list of words using topological sorting.



```python
from solution import alien_order

words = ["wrt", "wrf", "er", "ett", "rftt"]
order = alien_order(words)
print(order)  # "wertf"