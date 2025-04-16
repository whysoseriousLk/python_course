
# დავალება 1

n = int(input("enter number (0 < n < 50): "))

for i in range(1, n + 1):
        print(f"{i} -", end=" ")
        divisors = 0
        
        for j in range(1, i + 1):
            if divisors == 3:
                break
            if i % j == 0:
                print(j, end=" ")
                divisors += 1
        
        print()


# დავალება 2

for i in range(1, 10):
    for j in range(1, i + 1):
        number = j * i
        print(f"{j} * {i} = {number}", end="     ")
    print()


# დავალება 3

n = int(input("Enter number 0-20 : "))
a, b = 0, 1
count = 0

print(a, end=" ")

while count < n:
    print(b, end=" ")
    a, b = b, a + b
    count += 1



# დავალება 4

n = int(input("Enter tree height (0 < n < 50): "))

for i in range(n):   
    print(" " * (n - i - 1), end="")  
    if i == 0:
        print("*")
    else:
        print("/", end="")        
      
        print("*" * (2 * i - 1), end="")

        print("\\")

for i in range(2):
    print(" " * (n - 1) + "|")



