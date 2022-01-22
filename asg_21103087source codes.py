#q1(a)length is including spaces
string_entered=input("")
length=len(string_entered)
print(length)

#q1(b)
string_entered=input("")
reversed_string=string_entered[-1::-1]
print(reversed_string)

#q1(c)
string_entered=input("")
string_sliced=string_entered[9:26]
print(string_sliced)

#q1(d)
string_entered=input("")
index_of_a=string_entered.find("a")
print(index_of_a)

#q1(e)
string_entered=input("")
string_without_spaces=string_entered.replace(" ","")
print(string_without_spaces)

#q2
name=input("name: ")
sid=int(input("SID: "))
Department=input("deptartment: ")
cgpa=float(input("CGPA: "))
print("Hey,%s Here!\n My SID is %i \nI am from %s department\n and my CGPA is %f "%(name,sid,Department,cgpa))
      
#q3(a)
a=4
b=5
print(a&b)
    
#q3(b)
a=4
b=5
print(a|b)
    
#q3(c)
a=4
b=5
print(a^b)

    
#q3(d)
a=4
b=5
print(a<<2)
print(b<<2)
    
#q3(e)
a=4
b=5
print(a>>2)
print(b>>2)
    
#q4
number1=input("number1: ")
number2=input("number2: ")
number3=input("number3: ")
if int(number1)>(int(number2) and int(number3)):
    print("the greatest no is:" ,int(number1))
elif int(number2)>(int(number1) and int(number3)):
    print("the greatest no is",int(number2))
else:
    print("the greatest no is",int(number3))

#q(5)
The_string=input("enter the string: ")
a="name"
if a in The_string:
    print("Yes: ")
else:
    print("no ")
      


    #q6
side1=int(input("side1: "))
side2=int(input("side2: "))
side3=int(input("side3: "))
if side1>side2 + side3 or side2>side1+side3 or side3> side1+side2:
    print("No: ")
elif side1==side2==side3==0:
    print("No: ")
else:
    print("Yes: ")


      


    


