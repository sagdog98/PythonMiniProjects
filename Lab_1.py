# A list of numbers that will be used for testing our programs
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Question 1: Create a function called even, which takes in an integer as input and returns true if the input is even, and false otherwise
def even(num):
    # Provide your code here
    return True if num % 2 == 0 else False

print("even(1):\t\t\t\t", even(1)) # should return False
print( "even(2):\t\t\t\t", even(2)) # shourd return True
print()

# Question 2: Create a function called odd, which takes in an integer as input and returns true if the input is odd, and false otherwise
def odd(num):
    # Provide your code here
    return False if num % 2 == 0 else True

print("odd(1):\t\t\t\t\t", odd(1)) # should return True
print("odd(2):\t\t\t\t\t", odd(2)) # shourd return False
print()

# Question 3: Given a list of integers, create a function called count_odd, which takes in a list and counts the number of odd. Your function should employ a divide and conquer approach. Select an appropriate base case and implement a recursive step.
def count_odd(list):
    # Provide your code here
    return 0 if len(list) == 0 else (list[0] % 2 + count_odd(list[1:]))

print("count_odd([1, 2, 3, 4, 5, 6, 7, 8]):\t", count_odd(numbers)) # should return 4
print()

# Question 4: Given a list of integers, use a divide and conquer approach to create a function named reverse, which takes in a list and returns the list in reverse order.
def reverse(list):
    # Provide your code here
    if len(list) == 0:
        return []
    else:
        return reverse(list[1:]) + list[:1] if list else []

print("reverse([1, 2, 3, 4, 5, 6, 7, 8]):\t", reverse(numbers)) # should return [8, 7, 6, 5, 4, 3, 2, 1]
print()

# Question 5: Given two sorted lists, it is possible to merge them into one sorted lists in an efficient way. Design and implement a divide and conquer algorithm to merge two sorted lists.
def merge(list1, list2):
    # Provide your code here
    if list1 and list2:
        if list1[0] > list2[0]:
            list1, list2 = list2, list1
        return [list1[0]] + merge(list1[1:], list2)
    return list1 + list2

print("merge([1, 3, 5, 7], [2, 4, 6, 8]):\t", merge([1, 3, 5, 7], [2, 4, 6, 8])) # should return [1, 2, 3, 4, 5, 6, 7, 8]
