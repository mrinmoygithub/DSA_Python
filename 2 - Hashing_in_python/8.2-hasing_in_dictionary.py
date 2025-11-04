n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

def is_hashing():
    # Count occurrences of each number in n
    freq = {}
    for num in n:
        freq[num] = freq.get(num, 0) + 1

    # Check and print frequencies for numbers in m
    for num in m:
        print(f"{num}: {freq.get(num, 0)}")

# Call the function
is_hashing()
