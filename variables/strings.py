#Strings

str1="python"
print("str1:",id(str1))
str2="python"
print("str2:",id(str2))
str1=str1+str2 #immutable
print("str1:",id(str1))

#index
s="python"
print("s[0]:",s[0])
print("s[1]:",s[1])
print("s[2]:",s[2])
print("s[3]:",s[3])
print("s[4]:",s[4])
print("s[5]:",s[5])
print("s[-1]:",s[-1])
print("s[-2]:",s[-2])
print("s[-3]:",s[-3])
print("s[-4]:",s[-4])
print("s[-5]:",s[-5])
print("s[-6]:",s[-6])

#slicing
s="python"
print(s[1:4])
print(s[1:])
print(s[:4])
print(s[:])
print(s[-4:-2])
print(s[-5:4])
print(s[1:4:2])
print(s[-1:6:-2])

