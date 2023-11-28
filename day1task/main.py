import random
#1
def even_num():
    user_input = int(input("Enter a number"))
    print(type(user_input))
    for i in range(user_input):
        if i % 2 == 0:
            print(i)

def guess_num():
    secret_num = random.randint(0, 100)
    count = 0
    while count != 3:
        number = int(input("guess the number"))
        if secret_num == number:
            print("Guess correct")
            break
        if secret_num > number:
            print(f"The number is greater than {number}") 
        if secret_num < number:
            print(f"The number is less than {number}") 
        count +=1


def vowel_count():
    vowels = ["a", "e", "i", "o"]
    user_data = input("enter a string")
    count = 0
    for char in user_data:
        if char.lower() in vowels:
            count += 1

    return count

def calculator():
    first_num = int(input("enter a number"))
    second_num = int(input("enter a second number"))
    operation = input("operation between")
    if operation == "+":
        return (first_num + second_num)
    if operation == "-":
        return (first_num - second_num)
    elif operation == "/":
        return (first_num / second_num)
    elif operation == "*":
        return (first_num * second_num)
    

def even_odd_sum():
    user = int(input("enter a number you want to insert in the list"))
    user_list = [i for i in range(user)]
    evenSum = 0
    odd_sum = 0
    for e in user_list:
        if e % 2 == 0:
            evenSum +=e
        else:
            odd_sum += e
    print( evenSum, odd_sum)


print(calculator())