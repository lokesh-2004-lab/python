# functions
# it is a block of code use multiple ties in different inputs
# it is reuseble code
# it by default fun ction return the none value
# it is helps to repeat the code 
# syntax of function
# ---------------------------------------------------------------

# static function
# def sample():   # in this function is used always display same output tak without any input
#     print("hello my sample") in this function call multiple times 
# sample() call the function
# -----------------------------------------------------------------
# dynamic function
# in thsi dynamic function give different inputs in different outputs
# always inputs should be taken in the form 1)argument----->name 2)parameters--->citys 
# def heroes(name,movie,city,budget):
#     print(name,movie,city,budget)
# heroes("prabhas","saaho","hyd","6000000")
# # -----------------------------------------------------------------
# sevaral types of dynamc arguments functions

# 1--->default argument
# # -->alwas give default values in end of the function
# #  when we insert the default values in this it cannot be changed
# def functions(x,y,z=26):
#     print(x,y,z)
# functions(5,6)
#  it automatically display the inside default values
#  values replaces it possible inside this

# -------------------------------------------------------------------
# 2)----->orbitary arguments
# def students(*royal): #it is use how many unknown keyword in this and 
#                       #* in thsi symbol is used display output in tuple type
#     print(*royal)
# students("nani","raju","ani")

# def legends(*mama):
#     print(mama)
# legends('venkat','lalu','hari','karthi','challa','komal','yash','manga','lalu')

# --------------------------------------------------
# 3)--->key word orbitary arguments
# when it is used  how many unknown keywords are in this 
# it is display output dict fromat 
# def students(son1,son2,son3):
#     print(f" first son name is {son1}, second son is {son2},third son is {son3}")
# students("ram","lakshman","bharat")
# -------------------------------------------------------------------------

# return

# def manga(name,city,salary):
#     print(name,city,salary)
    

# print(manga('arjun','hyd',60000)

# def student(*name):
#     print(name)
# student('raj','rani')

# def my_func():#it is scope function
#     x=23
#     print(x)
# my_func()
# x=34
# def my_func():
#     x=23
#     print(x)
#     def my_func1():
#         x=33
#         print(x)
#         def my_func2():

#             x=35
#             print(x)
#         my_func2()
#     my_func1()        
# my_func()
# print(x)   



# x=65
# def my_func1():
#     global x
#     x=55
#     print(x)
#     def my_func2():
#         x=44
#         print(x)
#     my_func2()
# my_func1()
# print(x)

# x=40
# def func():
#     x=25
#     print(x)
#     def func1():
#         nonlocal x
#         x=24
#         print(x)
#     func1()
#     print(x)
# func()
# print(x)
    
    
# def recu(n):
#     if n>=0:
#         print(n)
#         return recu(n-1)
# recu(10)


# functions
# n=int(input("number of terms:"))
# a=0
# b=1
# print("fibnoci series:")
# for i in range(n):
#     print(a,end=" ")
#     a,b=b,a+b

# def recu(n):
#     if n>0:
#         print(n)
#         sum=n*(n+1)//2
#         print(sum)
#         return recu(n-1)
# recu(10)

n=int(input("enter a series:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")

a,b=b,a+b