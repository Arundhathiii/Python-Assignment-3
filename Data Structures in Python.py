# #Topic: List
# #Q:1) Create a list of 5 random numbers and print the list
# import random
# random_numbers = []
# for i in range(5):
#     random_numbers.append(random.randint(1,100))
# print(random_numbers)
#
# #Q:2) Insert 3 new values to the list and print the updated list
# random_numbers.insert(0,10)
# random_numbers.insert(2,20)
# random_numbers.insert(4,5)
# print("Updated list:",random_numbers)
#
# #Q:3) Try to use a for loop to print each element in the list
# for number in random_numbers:
#     print(number)
#
##Topic: Dictionary
# #Q:1) Create  a Dictionary with keys 'name','age', and 'address' and values 'John','25',and 'New York' respectively
# person={'name':'John','age':25,'address':'New york'}
# print(person)
#
# #Q:2) Add a new key-value  pair to the dictionary created in Q1 with key 'phone' and value '1234567890'
# person['phone'] = '1234567890'
# print(person)
#
##Topic: Set
# #Q:1) Create a set with values 1,2,3,4 and 5
# s1={1,2,3,4,5}
# print(s1)
#
# #Q:2) Add the value 6 to the set created in Q1
# s1.add(6)
# print(s1)
#
# #Q:3) Remove the value 3 from the set created in Q1
# s1.remove(3)
# print(s1)
#
##Topic: Tuple
# #Q:1) Create a tuple with values 1,2,3 and 4
# t1=(1,2,3,4)
# print(t1)
# #Q:2) Print the length of the tuple created in Q1
# print(len(t1))