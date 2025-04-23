
import random




def main(): 
    # დავალება 1
    avgtemp()
    
    # დავალება 2
    random_numbers()

    # დავალება 3
    remove_duplicates()



# დავალება 1

def avgtemp():
    temperatures = [22, 25, 19, 23, 25, 26, 23]
    
    total = 0
    for temp in temperatures:
        total += temp
    
    average_temp = int(total / len(temperatures))
    print(f"Average Temperature is: {average_temp}")


# დავალება 2

def random_numbers():
    numbers = [random.randint(1, 30) for _ in range(50)]
      
    new_list = []
    for num in numbers:
        new_list.extend([num] * num)
    print(new_list)
    print(f"length of list is: {len(new_list)}")


# დავალება 3

def remove_duplicates():
    numbers = [random.randint(1, 30) for _ in range(50)]

    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    print(new_list)
    print(f"length of list is: {len(new_list)}")




if __name__ == "__main__":
    main()

