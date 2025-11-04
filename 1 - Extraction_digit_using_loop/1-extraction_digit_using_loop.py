
n = int(input("Enter any number: "))
def extraction_digit_using_loop(num):
    total = 0
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        total += last_digit
        num = num // 10
    print("Sum of digits:", total)

extraction_digit_using_loop(n)
