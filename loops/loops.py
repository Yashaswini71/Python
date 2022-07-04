#!/usr/bin/python

#for loop
for i in range(20):
    print(i)


#while loop
Employee = True
while Employee:
    print("Employee is in Thundersoft !")
    Employee = False
print("Employee has Resigned.")

num = 5
while num>0:
    if num==3:
        num = num-1
        continue
    elif num==2:
        break
    print(num)
    num = num-1




