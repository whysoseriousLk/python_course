

# დავალება 1

# def count_vowels(text):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'ა', 'ე', 'ი', 'ო', 'უ']
#     count = 0

#     for char in text:
#         if char.lower() in vowels:
#             count += 1

#     return count

# print("Number of vowels:", count_vowels("Hello World"))
# print("Number of vowels:", count_vowels("თევზები რას ფიქრობენ?"))
# print("Number of vowels:", count_vowels("ლაშას მამა გარდაიცვალა"))



# დავალება 2

# def max_number(*args):
#      return max(args)   

# print("Maximum:", max_number(2, -8, 0, 15, 20))
# print("Maximum:", max_number(-10, -5, 0, -140))
# print("Maximum:", max_number(150, 1000, 1000.1))



# დავალება 3

# def factorial(n):
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print("Factorial:", factorial(10)) 
# print("Factorial:", factorial(0)) 
# print("Factorial:", factorial(5)) 


# დავალება 4

# def is_prime (num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True    
    
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")



# დავალება 5

# def reverse_text(text):
#     return text[::-1]

# print("Reversed:", reverse_text("გამარჯობა"))
# print("Reversed:", reverse_text("Hello World"))
# print("Reversed:", reverse_text("Radar"))



# დავალება 6

# def car_info (model, year = 2025, **kwargs):
#     print("Model:", model)
#     print("Year:", year)
#     for key, value in kwargs.items():
#         print(f"{key.capitalize()}: {value}")    

# car_info("BMW", color = "black", engine = "V8")
# car_info("Audi", 2023, color = "red", engine = "V6")
# car_info("Mercedes", 2024, color = "blue", engine = "V12", price = 100000)




    