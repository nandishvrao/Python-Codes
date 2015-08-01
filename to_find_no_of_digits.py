#Author : Nandish V

#program to find number of digits present in a number

n=int(input("enter a number:"))
#here we use str function to convert num to string
num=str(n)
count=0
for i in num:
    count=count+1

print("the number of digits present is:",count)
