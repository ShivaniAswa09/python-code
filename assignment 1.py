# Write a program to give a five subject input user, find total and percentage

'''mango=float(input("enter mango marks"))
orange=float(input("enter orange marks"))
apple=float(input("enter apple marks"))
banana=float(input("enter banana marks"))
grapes=float(input("enter grapes marks"))

total=mango+orange+apple+banana+grapes
percentage=(total/500)*100

print("\ntotal marks is:  \t",total)
print("\npercentage marks is:  \t",percentage)

if(percentage>70 and percentage<100):
     print("selected")
    
else:
    print(" not selected")'''

# Write a program to find out the highest number in between three input user:

num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))

if(num1>num2)and(num1>num3):
    print("num1 is largest no")
elif(num2>num1)and(num2>num3):
    print("num2 is largest no")
elif(num3>num1)and(num3>num2):
    print("num3 is largest no")
else:
    print("Same")
