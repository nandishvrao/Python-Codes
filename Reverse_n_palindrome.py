#Author Nandish V

#program to reverse a string
a=input("enter a string:")
i=len(a)

rev=""
while (i!=0):
    rev=rev+a[i-1]
    i=i-1
print(rev)

#program to check wether a number is palindrome or not
if (a==rev):
    print("entered string is a palindrome")
else:
    print("its not a palindrome")
