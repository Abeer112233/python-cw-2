my_name = input("what your name ?")
my_age = int(input("what is your age ?"))
print(f"my name is {my_name} and i am {my_age}years old")

first_number = int(input("enter the first number:"))
secound_number  = int(input("enter the secound number:"))

operation = input("entar the mathmatical operation:")

if operation=='+':
    print(first_number+secound_number)
elif operation=='-':
    print(first_number-secound_number)
elif operation=='*':
    print(first_number*secound_number)
elif operation=='/':
    print(first_number/secound_number)
else:
    print("the operation is not valid")

bus_capacity = 30
inside_the_bus = int(input("how many people are on the bus?"))
outside_the_bus = int(input("how many people are outside the bus?"))
empty_seats = bus_capacity - inside_the_bus

if empty_seats>outside_the_bus:
    print("there are seats on the bus")
else:
    print("the bus is full")

