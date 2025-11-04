def is_count_number():
    num = int(input("Enter your number: "))
    original_num = num
    count = 0

    while num > 0:
        num //= 10
        count += 1
        
    print("Number of digits:", count)
    return count

is_count_number()
