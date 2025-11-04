num = [5, 6, 7, 7, 111, 1, 1, 5, 1, 1]
freq_map = dict()  # or simply {}

for i in range(0, len(num)):
    if num[i] in freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1

print("Frequency Map:", freq_map)
