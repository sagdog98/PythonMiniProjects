

# Exercise 1. Implement the algorithm covered in lectures (and not any other algorithm) that determines if an integer n is prime. Your function should return True, if n is prime, and False otherwise. Your algorithm has to be effective for n ~ 1,000,000,000,000. A description of the algorithm covered in class appears on page 258 of the Rosen textbook.
def isPrime(n):
    # Provide a correct implementation for this function
    if x == 2:
        return True
    for i in range(2, int(ceil(sqrt(n+1)))):
        if x % i == 0:
            return False
    return True






# Exercise 2. Using the isPrime function above, implement a function that takes in an integer n, and returns the smallest prime number greater than n. Your code should computer in a reasonable time for n ~ 1,000,000,000,000.
def nextPrime(n):
    # Provide a correct implementation for this function
    if x < 2:
        return 2
    elif x == 2:
        return 3
    i = x + 2
    while i > n:
        if isPrime(i):
            return i
        else:
            i = i + 2
    return 0



# Exercise 3. It is sometimes necessary to find all prime numbers less than some integer n. Implement a function that takes in an integer n and returns a list of all primes that are less than or equal to n. Your algorithm should be effective for n ~ 1,000,000
def allPrimes(n):
    # Provide a correct implementation for this function
    list = []
    if n <= 2:
        return list
    list.append(2)
    i = 3
    while i < n:
        if isPrime(i):
            list.append(i)
        i = i + 2
    return list



# Exercsie 4. The Fundamental Theorem of Arithmetic tells us that every positive integer n, can be expressed uniquely as a product of primes in non-decreasing order. Implement the method covered in class (and not any other method), for finding prime factorizations of integers. The function below should take in an integer n, and return a list of the prime factors of n.
def factorize(n):
    # Provide a correct implementation for this function
    list = []
    i = 2
    while n % i == 0:
        n /= i
        list.append(i)
    i = i + 1
    while not(isPrime(n)) and i <= sqrt(n):
            if n % i == 0:
                n /= i
                list.append(i)
            else:
                i = i + 2
    list.append(n)
    return list



# Exercise 5. The scrurity of many popular cryptographic schemes, such as RSA, rests on the fact that factorizing numbers is difficult, meaning that it takes long to factorize some numbers. Use your code from exrecise 4 to experiment with different inputs and try to figure out what makes some numbers take longer to factorize than others. Explain what you found in the string/comment below

ex5answer = """
Write your answer for exercise 5 within the triple-double quotes:
I was able to find out that the computation time of a certain program depends on if the given number can be factored by any number that is 3 less than that number on the first step. The easiest, fastest and most optimal way to get a number with this magnitude would be to multiply two large prime numbers and you will get a big non prime number. This is because the computer has to check all the primes that can be divided into it before it finds the single prime number that goes into it, which ultimately prolongs the result of the program.



"""



# Exercise 6. In some cryptographic applications, it is necessary to use a special kind of prime numbers called safe primes. These are primes of the form q = 2p + 1, where p is also prime. The integer p is known as a Sophie Germain prime. Write a function that takes in an integer n, and returns the first safe prime, such that p > n. Your function should output a tuple (p, q), comprising the Sophie Germain prime, and the safe prime.
def safePrime(n):
    # Provide a correct implementation for this function
    p = n + 1
    if p < 3:
        p = 2
    while p > n:
        q = 2*p + 1
        if isPrime(q):
            return (p, q)
        else:
            p = nextPrime(p)
    return (0, 0)





# TEST SUITE

# A simple comparison
def check (a, b):
    if a == b:
        print "PASSED"
        print
    else:
        print "FAILED"
        print

# Check to see if some numbers are prime
result1 = isPrime(7)
expected1 = True
print "7 is prime:\t\t\t\t", result1
check(result1, expected1)

result2 = isPrime(15)
expected2 = False
print "15 is prime:\t\t\t\t", result2
check(result2, expected2)

result3 = isPrime(1000000)
expected3 = False
print "1,000,000 is prime:\t\t\t", result3
check(result3, expected3)

result4 = isPrime(1000003)
expected4 = True
print "1,000,003 is prime:\t\t\t", result4
check(result4, expected4)

result5 = isPrime(999999999989)
expected5 = True
print "999,999,999,989 is prime:\t\t", result5
check(result5, expected5)

print "Overall isPrime functionality"
check ([result1, result2, result3, result4, result5], [True, False, False, True, True])


# Print the first 20 primes
k = 0
result = []
expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
for i in range(20):
    k = nextPrime(k)
    result.append(k)
print "The first 20 primes:\t\t\t", result
check(result, expected)


# Generate all primes
result = allPrimes(20)
expected = [2, 3, 5, 7, 11, 13, 17, 19]
print "All primes less than 20:\t\t", result
check(result, expected)



# Factorize some integers

result1 = factorize(2016)
expected1 = [2, 2, 2, 2, 2, 3, 3, 7]
print "Prime factorization of 2016:\t\t", result1
check(result1, expected1)

result2 = factorize(2017)
expected2 = [2017]
print "Prime factorization of 2017:\t\t", result2
check(result2, expected2)


result3 = factorize(999999999990)
expected3 = [2, 3, 3, 5, 21649, 513239]
print "Prime factorization of 999999999990:\t", result3
check(result3, expected3)

result4 = factorize(999999999989)
expected4 = [999999999989]
print "Prime factorization of 999999999989:\t", result4
check(result4, expected4)

print "Overall factorize functionality"
check([result1, result2, result3, result4], [expected1, expected2, expected3, expected4])


# Generate some safe primes
k = (0,0)
result = []
for i in range(7):
    k = safePrime(k[0])
    result.append(k)
expected = [(2, 5), (3, 7), (5, 11), (11, 23), (23, 47), (29, 59), (41, 83)]
print "The first 7 safe primes:\t\t", result
check(result, expected)
