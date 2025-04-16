



# დავალება 1

# def is_palindrome(text):
#     cleaned_text = ''
#     for char in text:
#         if char.isalpha():
#             cleaned_text += char.lower()
    
#     reversed_text = cleaned_text[::-1]
#     if cleaned_text == reversed_text:
#         return True
#     else:
#         return False

# text = input("Enter Text: ")

# if is_palindrome(text):
#     print("Is palindrome")
# else:
#     print("Is not palindrome")



# დავალება 2

# def can_construct(text1, text2):
#     text1 = text1.lower().replace(" ", "")
#     text2 = text2.lower().replace(" ", "")
    
#     sorted_text1 = sorted(text1)
#     sorted_text2 = sorted(text2)
    
#     if sorted_text1 == sorted_text2:
#         return True
#     else:
#         return False

# text1 = input("Enter Text: ")
# text2 = input("Enter Text: ")

# if can_construct(text1, text2):
#     print("YES")
# else:
#     print("NO")




# დავალება 3

# date = "2024-03-04T11:17:42.000123+04:00"
# parts = date.split('T')

# year = parts[0][0:4]
# month = parts [0][5:7]
# day = parts[0][8:10]

# hours = parts[1][0:2]
# if "0" in hours:
#     hours = hours.replace("0", "")   

# minutes = parts[1][3:5]
# seconds = parts[1][6:8]

# timezone = parts[1][15:].replace("0", "").replace(":", "")

# print(f"{day}-{month}-{year} {hours}:{minutes}:{seconds} {timezone}")
