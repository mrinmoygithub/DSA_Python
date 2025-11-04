# 🔢 What is an Armstrong number?
# A number is an Armstrong number if the sum of its digits raised to the power of the number of digits equals the original number.

# For example:

# 153 is an Armstrong number because:
# 1^3 + 5^3 + 3^3 = 153

def is_armstrong_number():
    num = int(input("Enter a number: "))
    original_num = num
    digits = [int(d) for d in str(num)]
    print("digits : ", digits)
    power = len(digits)

    armstrong_sum = sum(d ** power for d in digits)

    if original_num == armstrong_sum:
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")

is_armstrong_number()

