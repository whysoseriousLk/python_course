

#დავალება 1

test = input("please enter true or false (true/false) :").lower()
if test == "true":
    print("whoala")

#დავალება 2

a = int(input("A : "))
b = int(input("B : "))
if a % b == 0:
    print(a, "არის", b,"-ს ჯერადი")


#დავალება 3

num = int(input("enter number from the range: 1-10 :"))
if 1 <= num <= 10:
    if num % 2 == 0 and num % 3 == 0:
        print (2,3)
    elif num % 2 == 0 and num % 5 == 0:
        print (2,5)    
    elif num % 2 == 0:
        print(2)
    elif num % 3 == 0:
        print(3)
    elif num % 5 == 0:
        print(5)
    elif num % 7 == 0:
        print(7)    
else:
    print("enter number from the range: 1-10 !!!")
if num == 1:
    print ("No divisors for 1")




#დავალება 4

speed = int(input("Enter Car's speed : "))
s = "SLOW"
m = "MODERATE"
f = "FAST"
vf = "VERY FAST"

if speed > 120:
    print(vf)
elif speed <= 30:
    print(s)
elif 60 < speed <= 120:
    print(f) 
elif 30 < speed <= 60:
    print(m)
