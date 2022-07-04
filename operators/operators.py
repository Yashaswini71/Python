#operators
#arthmetic operators
x = 5
y = 3
print(x + y)#addition

#subtraction
x = 5
y = 3
print(x - y)

#multiplication
x = 5
y = 3
print(x * y)

#division
x = 12
y = 3
print(x / y)

#modulus
x = 5
y = 2
print(x % y)

#Exponentiation
x = 2
y = 5
print(x ** y)

#floor division
x = 15
y = 2
print(x // y)

#assignment operators
x = 5
print(x)

x = 5
x += 3
print(x)

x = 5
x -= 3
print(x)

#Comparison operators

x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x <= y)



#logical operators
x = 5
print(x > 3 and x < 10)#and

x = 5
print(x > 3 or x < 4)#or

x = 5
print(not(x > 3 and x < 10))#not

#identity operators
#is
x = ["yashu", "nandu"]
y = ["yashu", "nandu"]
z = x
print(x is z)
print(x is y)
print(x == y)

#is not
x = ["yashu", "nandu"]
y = ["yashu", "nandu"]
z = x
print(x is not z)
print(x is not y)
print(x != y)


#membership operators

x = ["yashu", "nandu"]
print("nandu" in x)#in

x = ["yashu", "nandu"]
print("kavya" not in x)#not in

