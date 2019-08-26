import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

#randrange - random number from 1-6 skipping 1 above... (1,6,1)

# numb_list = list[1,2,3,4,5,6,7,8,9,10]

print(my_randoms)

# Print a message to the console indicating whether each value of
# `number` is in the`my_randoms` list.

# numb_list = list(range(1,11))


for number in range(1,6):
    contains = False
    for x in my_randoms:
        if number == x:
            contains = True
    if contains == True:
        print(f"my_randoms list includes number {number}")
    else:
        print(f"my_randoms list does not includes number {number}")


# print("my Randoms", my_randoms)

# example of conditional below
# name = "Stebe"
# if name == "Steve":
#     print("I feel good")
# elif name == "Joe":
#     print("Joe is the King of the World")
# else:
#     print("I have a cold")




#another way to do it:

#   import random
# """
# Print a message to the console indicating whether each value of
# `number` is in the `my_randoms` list.
# """



# my_randoms = list()
# for i in range(10):
#     my_randoms.append(random.randrange(1, 6, 1))

# # Generate a list of numbers 1..10
# numbers_1_to_10 = range(1, 10)

# # Iterate from 1 to 10
# for number in numbers_1_to_10:
#     the_numbers_match = False

#     # Iterate your random number list here

#     # Do the two numbers match? Change the boolean.

#     print(f'{number} is in the random list')











