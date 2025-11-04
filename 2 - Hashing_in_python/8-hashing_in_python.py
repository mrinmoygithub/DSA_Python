# Constraints
# 1. i <= n[i] <= 10
# 2. n can have 10^8 elements
# 3. m can have 10^8 elements

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

def is_hashing():
    for num in m:
        count = 0
        for x in n: 
            if x == num:
                count += 1
        print (f'{num}: {count}')

is_hashing()
