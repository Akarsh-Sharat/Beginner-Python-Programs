#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Num= input("enter numbers seprated by ','")
List= Num.split(",")
Tuple= tuple(List)
print('List:',List)
print('Tuple:',Tuple)

