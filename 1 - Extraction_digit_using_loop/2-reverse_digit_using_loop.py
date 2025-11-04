def extraction_digit_using_loop():
    num = int(input("Enter a number: "))
    original_num = num
    # total = 0
    reverse = 0

    print("Extracted digits:")
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        # total += last_digit
        reverse = reverse * 10 + last_digit
        num = num // 10

    # print("Sum of digits:", total)
    print("Original number:" , original_num)
    print("Reversed number:", reverse)

extraction_digit_using_loop()
