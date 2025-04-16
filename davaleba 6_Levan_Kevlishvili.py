

# დავალება 1  


import random

computer_number = random.randint(0, 100)
max_attempts = 10

for attempt in range(1, max_attempts + 1):
    user_number = int(input(f"attempt {attempt}: please, enter the number (0-100): "))
    
    if user_number == computer_number:
        print("you are the winner!!!")
        break
    elif user_number > computer_number:
        print("high")
    else:
        print("low")    
    if attempt == max_attempts:
        print("computer is the winner")


# დავალება 2

n = int(input("enter number (0 < n < 1000): "))

while n > 0 and n < 1000:
    if n % 2 == 0:
        n = n // 2
    else: 
        n = n * 3 + 1
    print(n, end=" ")
    if n == 1:
        break


# დავალება 3

n = int(input("Enter number (0 <= n < 10000): "))

if n < 0 or n >= 10000:
    print("Invalid input. Please enter a number between 0 and 9999.")
else:
    reversed_number = 0
    sum_of_digits = 0

    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        sum_of_digits += digit
        n = n // 10

    print(f"Reversed number is: {reversed_number}")
    print(f"Sum of digits: {sum_of_digits}")


# დავალება 4

n = int(input("Enter a number (0 < n < 10): "))

if n <= 0 or n >= 10:
    print("Invalid input. Please enter a number between 1 and 9.")
else:
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(j, end="")
            j += 1
        print()
        i += 1
    
    i = n - 1
    while i >= 1:
        j = 1
        while j <= i:
            print(j, end="")
            j += 1
        print()
        i -= 1



   