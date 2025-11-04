num = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
hash_map = {}

n = len(num)

for i in range(0, n):
    hash_map[num[i]] = hash_map.get(num[i], 0) + 1

print("Frequency Map:", hash_map)
