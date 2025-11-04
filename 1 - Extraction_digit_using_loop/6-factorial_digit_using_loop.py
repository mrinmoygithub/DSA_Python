# ✅ What is a Factorial Number?
# The factorial of a non-negative integer n, written as n!, is the product of all positive integers less than or equal to n.

def print_factors():
    num = int(input("Enter a number: "))
    print(f"Factors of {num} are:")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

print_factors()
