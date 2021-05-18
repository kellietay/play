from collections import Counter

def make_anagram(s1,s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    s1_count = Counter(s1)
    s2_count = Counter(s2)

    if s1_count == s2_count:
        return 0

    steps = 0

    all_keys = set(s1_count.keys()).union(set(s2_count.keys()))

    for key in all_keys:
        steps += abs(s1_count.get(key,0)-s2_count.get(key,0))
    
    return int(steps/2)

s1 = "bond"
s2 = "down"
print(make_anagram(s1,s2))

s3 = "xxxx"
s4 = "yyyy"
print(make_anagram(s3,s4))