# 1. Create a function for modular addition
def modAdd(x, y, m):
    
    
    int g= (x+y) %m;
    return g;
    
print "7 + 9 (mod 11):\t\t\t", modAdd(7, 9, 11) # => 5
    

# 2. Create a function for modular multiplication
def modTimes(x, y, m):
    # Provide your code here
    int g=(x*y) %m;
    
print "7 * 9 (mod 11):\t\t\t", modTimes(7, 9, 11) # => 8
   
   
# 3. Create a function for converting binary to decimal. Binary numbers are represented as strings of 1 and 0        
def binToDec(n):
    # Provide your code here
        
        
        
print  "1010000100 in decimal:\t\t", binToDec('1010000100') # => 644


# 4. Create a function for converting decimal to binary. Binary numbers are represented as strings of 1 and 0
def decToBin(n):
   
return bin(n);
    
    
print "644 in binary:\t\t\t", decToBin(644) # => 1010000100


# 5. Create a function for modular exponentiation. Your function should compute in a reasonable time for exponents on the order of 10 billion
def modExp(n, p, m):
   
    return (a**b) % c   

    
    
print "3^644 (mod 645):\t\t", modExp(3, 644, 645) # => 36

print "3^9876543210 (mod 2017):\t", modExp(3, 9876543210, 2017) # => 1040


# 6. Write a function to determine the last digit of an integer represented as a base raised to an exponent.


def lastDigit(base, exponent):

    if exponent ==0;
    return 1;

    loopval =[base%10]
        
        while True:
        
        nextval = (loopval[-1] * base) % 10
        if nextval==loopval[0]:
            break
            loopval.append(nextval);
        return loopval[(exponent-1) % len(loopval)]
    

print "Last digit of 7^56746365435748:\t", lastDigit(7, 56746365435748) # => 1
