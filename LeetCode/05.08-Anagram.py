"""
corner cases:
- one or both strings are empty
- len is different
"""
from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
