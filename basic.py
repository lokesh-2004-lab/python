#decision making statements
#it used to help decides the based on the conidtion

# marks=int(input("enter marks :"))
# if marks>=90:
#     print("a crade")
# elif marks>=80 and marks<90:
#     print("B grade")
# elif marks>=70 and marks<80:
#     print("C grade")
# elif marks>=60 and marks<70:
#     print("D grade") 
# elif marks>=50 & marks<60:
#     print("E grade")  
# else:
# #     print("fail")    
# company_name =["rgf_phb","rgf_madhapur","rgf_miyapur"]
# empolye_count=[45,23,21]
# ratings=[4.1,3.3,4.3]
# print(company_name)



# # non-primitative(mutable)
# list
# tuples
# set 
# dictroniry

# 1.list
# it is used stored collection of data
# it is mutable 
# its posible change in this list 

# it used curd operation
# curd-->
# list stored the collection of data
# list1=[1,6,"arjun",9,"renu"] 
# print(list1)  # it crates values
# list1.append("nani")#add the value
# print(list1)
# # convert list to tuple
# convert_list1=tuple(list1)
# print(convert_list1)
# list1.remove("arjun")
# print(list1)
# list1[1]="ram" # change the value
# print(list1)

# 2.tuples
#  it is immutable
#  cannot change the values in this tupple
# tuple=(1,2,3,'hi','welcome')
# print(tuple)
# tuple[2]='hi'
# tuple2=([1,2],4,5)

# print(tuple2[0][1])

list=["arun","ram","raju","yuva","nani"]
print(list)
print(list[4])
print(list[0])
list[3]=("python_student")
print(list)
# del (list[2])
# print(list)
# print(len(list))


# tuple2=("eshwar","chakram","ragavendra","bujjigadu")
# print(tuple2)

# list2=list(tuple2)
# print(list2)
# list2.append("excel")
# print(list2)
# tuple1=tuple(list2)
# print(tuple1)
# print(len(tuple1))

# movies={"kiran",4,"hello","deva",4,"kiran","hello",8}  #set cannot append  values  
# print(movies)
# movies=movies|{"babu"}
# print(movies)
# movies=movies -{4}
# print(movies)
# movie=list(movies)
# print(movie)
# # #
# # empolye={"mame":"anil","age":20,"city":"chennai"}
# print(empolye)
# empolye["role"]="goti analyst"
# print(empolye)
# empolye[2]=21
# print(empolye)
# print(empolye["mame"])
# print(len(empolye))


# rating=1
# marks=("excellent" if rating >=4 else 
#        "good" if rating >=3.6 else
#        "average" if rating >=3 else
#        "above agerage" if rating >=2 else
#        "poor")
# print(marks)

# limit_available=int(input("enter the limit amount:"))
# spending_available=int(input("enter the spending amount:"))
# due_amount=int(input("enter the due amount:"))
# if limit_available:
#        print("limit is access")
# elif limit_unavailable:
#        print("no limit")
# if spending_available:
#        print("spend the money")
# elif spending_unavailable:
#        print("not spend money")
# if due_amount<spending_available:
#        print("you will not pay the bill")
# else:

    #    print("pay the bill because due ")      
# movies={'loki','yash',5,'srihari',5,'loki'}
# print(movies)
 

#  LIST CONCEPT
# list=["loki",2,"yash","sallar",34,8,"hari"]
# list.extend([1,3])       it is add the values using extend
# print(list)

# list=["loki",2,"yash","sallar",34,8,"hari"]
# list.insert(1,9)
# print(list)    add another value in list give index and value


# list=["loki",2,"yash","sallar",34,8,"hari"]
# list.remove(2)   remove is used delete  particular data in list
# print(list)

# list=["loki",2,"yash","sallar",34,8,"hari"]
# list.pop(2)
# print(list)


# list=["loki",2,"yash","sallar",34,8,"hari"]
# list[2]="rajani"
# print(list)

# list=["loki",2,"yash","sallar",34,8,"hari"]
# list.pop[4]
# print(list)

