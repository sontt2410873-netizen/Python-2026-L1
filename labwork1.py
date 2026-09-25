#Ex1:
radius = float(input("Enter the value of radius:"))
pi = 3.14
print(f"Circle area: {pi*radius*radius}")

#Ex2:
a = float(input("Enter the temperature in C :"))
print(f"{int(a)} (C) = {a*9/5 + 32} (F)")

#Ex3:
a = int(input("Enter the number: "))
prime_num = True
if a <2 :
    prime_num = False
else:
    for i in range (2,int(a**0.5)+1):
        if a % i == 0:
            prime_num = False
            break
if prime_num:
    print(f"{a} is a prime number")
else:
    print(f"{a} is a not prime number")
#Ex4:
n = int(input("Enter the number:"))
Total_sum = sum([i for i in range(1,n)  if n % i == 0 ])
if Total_sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")


#Ex5:
my_color = ["red", "blue","black"]
color = input("Enter the favorite color:")
if  color in my_color:
    print(f"Your color is at index {my_color.index(color)} in my list")
else:
    print("Sorry, I Could'n find your color")

#Ex6:
print("range 1 |", list(range(7)))
print("range 2 |", list(range(1,11,3)))
print("range 3 |", list(range(5,0,-1)))
print("range 4 |", list(range(6,-3,-2)))

#Ex7:
def remove_dollar_sign(s):
    return s.replace("$","")  
#Ex8:
integer = [1,4,5,-1,10]
even_list = []
def extract_even (a):
    for  numbers in a:
        numbers  % 2 == 0
        even_list.append(numbers)
print(even_list)  
        
#Ex9:
def factorial_number(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial_number(n-1)
#Ex 10:
def divisors_number(n):
   print([i for i in range(1,n+1) if n %i == 0])
#Ex11:
import math 
x1,y1 = [float(i) for i in input("Enter the point A(x1, y1) :").split(",")]
x2,y2 = [float(i) for i in input("Enter the point B(x2, y2) :").split(",")]
distance = math.sqrt((x2 - x1)**2 +(y2 - y1)**2)
print(f" The distance between two points is : {distance}")

   
#Ex12:
def patten_size(m,n):
    for i in range(m):
        for j in range(n): 
           if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            # first column (i == 0) , final row ( i == m - 1)
            # first column (j == 0) , final column(j== n - 1)
             print("*", end= " ")
           else:
             print(" ",end= " ")
        print()

