num = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]

frequency = {}

for n in num:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

print("Frequency Dictionary:", frequency)


