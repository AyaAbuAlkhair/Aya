import math

a= float(input("a= "))
if a==0:
    print("wrong input")
b= float(input("b= "))
c= float(input("c= "))

w= (b**2)- (4*a*c)
s= math.sqrt(abs(w))
x1= (-b-s)/2*a
x2= (-b+s)/2*a
if w>0:
    print("The solutions are", x1,x2)
elif w==0:
    print(-b/2*a)
else:
    print("error")



