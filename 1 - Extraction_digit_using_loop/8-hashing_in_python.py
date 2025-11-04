# Hashing in Python
# Pre-storing values into some data-structure like List/Dictionary/Set and the fetching it. 

# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
# m = [10, 111, 1, 9, 5, 67, 2]

# for num in m:
#     count = 0
#     for x in n:
#         if x == num:
#             count += 1
#     print (f'{num}: {count}')

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

def is_hashing():
    hash_list = [0] * 11  # index 0 to 10

    # Count occurrences in n
    for num in n:
        if 1 <= num <= 10:
            hash_list[num] += 1

    # Print frequencies for each num in m
    for num in m:
        if num < 1 or num > 10:
            print(f"{num}: 0")
        else:
            print(f"{num}: {hash_list[num]}")

# Call the function
is_hashing()

