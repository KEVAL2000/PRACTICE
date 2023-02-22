import random
#Single line comment
"""Multi line
comment"""
x=10
print(type(x))
alpha = ['a','b','c']
x,y,z = alpha
print(x)
print(y)
print(z)
y=10
def fun():
    global y
    y=20
fun()
print(y)
list = [1,2,3]
tuple = (1,2,3)
set = {1,2,3}
dict = {'n1':1,'n2':2,'n3':3}
print(list)
print(tuple)
print(set)
print(dict)
print(random.randrange(1,10))
str = "HELLO WORLD"
print(str[0:11])#HELLO WORLD
print(str[0:])#HELLO WORLD
print(str[:11])#HELLO WORLD
print(str[::])#HELLO WORLD
print(str[::1])#HELLO WORLD
print(str[::-1])#DLROW OLLEH
print(str[-11:-1])#HELLO WORL
print(len(str))#length
print(str.upper())#upper
print(str.lower())#lower
print(str.strip())#remove whitespace
print(str.replace("HELLO","hello"))#replace
str = "one one one"
print(str.replace("one","two",2))
str2 = "HELLO,WORLD"
print(str2.split(","))#split
txt = "Age is {0} in year {1}"
print(txt.format(22,2023))#insert number
txt2 = "My name is \'Keval\'"
print(txt2)#insert sigle quote
name = "keval"
print(name.capitalize())#capitalize
print(name.center(15,"-"))#center
print(name.encode(encoding="ascii"))#encode
name2 = "My name is Keval."
print(name2.find("Keval"))#find
print(name2.index("Keval"))#find
print(name2.endswith("."))#end with
print(name2.startswith("My"))#start with
number = "1\t2\t3"
print(number.expandtabs(4))#expand
rate = "Only {:.2f} Rs"
print(rate.format(50))
rate = "Only {:>10} dollars"
print(rate.format(10))
rate = "Only {:<10} dollars"
print(rate.format(10))
rate = "Only {:^10} dollars"
print(rate.format(10))
rate = "Only {:=10} dollars"
print(rate.format(-10))
rate = "Only {:+} dollars"
print(rate.format(10))
rate = "Only {:-} dollars"
print(rate.format(10))
rate = "Only {: } dollars"
print(rate.format(10))
rate = "Only {:,} dollars"
print(rate.format(10000))
rate = "Only {:b} dollars"
print(rate.format(10))
rate = "Only {:.0%} dollars"
print(rate.format(0.25))
user = "Keval"
user2 = "Keval123"
user3 = "123"
user4 = "Keval_123"
user5 = "KEVAL"
user6 = "keval"
user7 = " "
user8 = "My name\nisKeval"
user9 = "My Name Is Keval"
print(user.isalpha())
print(user2.isalnum())
print(user3.isdigit())
print(user3.isnumeric())
print(user3.isdecimal())
print(user4.isidentifier())
print(user5.isupper())
print(user6.islower())
print(user7.isspace())
print(user8.isprintable())
print(user9.istitle())
fruit = ["mango","banana","orange"]
print("#".join(fruit))
str = "Keval"
print(str.ljust(10,"-"))
print(str.rjust(10,"-"))
str = "     Keval     "
print(str.lstrip())
print(str.rstrip())
str = "Hello Sam"
x = "mSa"
y = "eJo"
z = "Hello "
new = str.maketrans(x,y,z)
print(str.translate(new))
txt = "I love banana fruit"
print(txt.partition("banana"))
str = "Keval"
print(str.rfind("l"))
print(str.rindex("l"))
txt = "I love banana and banana is fruit"
print(txt.rpartition("banana"))
fruit = "apple, banana, mango"
print(fruit.rsplit(", ",2))
txt = "I love banana \n banana is fruit"
print(txt.splitlines())
str = "KEVAL keval"
print(str.swapcase())
txt ="...Keval,,,"
print(txt.strip(".,"))
txt = "my name is keval"
print(txt.title())
txt = "Hello Sam"
x = {83:80}
print(txt.translate(x))
number = "10"
print(number.zfill(10))
#0000 0000 0000 0000(0)
#0000 0000 0000 0001(1)
#0000 0000 0000 0010(2)
#0000 0000 0000 0011(3)
#0000 0000 0000 0100(4)
#0000 0000 0000 0101(5)
#0000 0000 0000 0110(6)
#0000 0000 0000 0111(7)
#0000 0000 0000 1000(8)
#0000 0000 0000 1001(9)
#0000 0000 0000 1010(10)
#0000 0000 0000 1011(11)
#0000 0000 0000 1100(12)
#Arithmetic + - * / % ** //
#Assignment = += -= *= /= %= **= //= &= |= ^= >>= <<=
#Comparison == != > < >= <=
#Logical and or not
#Bitwise & | ^ ~ << >>
#Identity is is not
#Membership in not in
#Precedence () ** ~ *,/ //,% +,- <<,>> & ^ | == !=,> >=,< <= is,isnot in,notin not and or

#       ordered changeable duplicate indexed
#List   yes     yes        yes       yes 
#Tuple  yes     not        yes       yes
#Set    not     not        not       not
#Dict   yes     yes        not

#For List
list = ["apple", "mango", "banana"]
print(list[0:3])

list[0:3] = ["cherry"]
print(list)

list = ["apple", "mango", "banana"]
list[2:] = ["banana","cherry","melon"]
print(list)

list = ["apple", "mango", "banana"]
list.insert(3, "cherry")
print(list)
list.append("melon")
print(list)

list1 = ["apple"]
list2 = ["mango", "banana"]
list1.extend(list2)
print(list1)

list = ["apple", "mango", "banana"]
list.remove("banana")
print(list)
list.pop(1)
print(list)
list.clear()
print(list)
del list

list = ["apple", "mango", "banana"]
for x in list:
    print(x)
[print(x) for x in list]

list1 = ["apple", "mango", "banana"]
list2 = []
for x in list1:
    list2.append(x)
print(list2)
list2.clear()
list2 = [x.upper() for x in list1]
print(list2)

list1 = ["apple", "mango", "banana"]
list2 = ["Hello" for x in list]
print(list2)

list1 = ["apple", "mango", "banana"]
list2 = [x if x!="banana" else "orange" for x in list1]
print(list2)

list = ["apple", "mango", "banana"]
list.sort(reverse=True)
print(list)

list1 = ["apple", "mango", "banana"]
list2 = list1.copy()
print(list2)

list1 = ["apple"]
list2 = ["mango", "banana"]
list3 = list1 + list2
print(list3)

list = ["apple", "apple", "apple"]
print(list.count("apple"))

#For tuple
tuple = ("apple", "mango", "banana")
del tuple

tuple = ("apple", "mango", "banana")
new = tuple*2
print(new)

#For Set
set = {"apple"}
set.add("mango")
print(set)

set1 = {"apple"}
set2 = {"mango", "banana"}
set1.update(set2)
print(set1)

set = {"apple", "mango", "banana"}
set.remove("banana")
print(set)
set.discard("mango")
print(set)

set = {"apple", "mango", "banana"}
set.pop()
print(set)
set.clear()
print(set)
del set

set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
set3 = set1.union(set2)#exclude duplicate
print(set3)
print(set1)
set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
set1.update(set2)#exclude duplicate
print(set1)
set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
set3 = set1.intersection(set2)#keep item exist in both
print(set3)
print(set1)
set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
set1.intersection_update(set2)#same as above but remove from original also
print(set1)
set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
set3 = set1.symmetric_difference(set2)#keep item not exist in both
print(set3)
print(set1)
set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
set1.symmetric_difference_update(set2)#same as above but remove from original also
print(set1)
set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
set3 = set1.difference(set2)#return item only in set1 not in set2
print(set3)
print(set1)
set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
set1.difference_update(set2)#same as above but remove from original also
print(set1)
set1 = {"a", "b", "c"}
set2 = {"a", "d", "c"}
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))

#For Dict
dict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2000
}
print(dict["brand"])
print(dict.get("brand"))
print(dict.keys())
print(dict.values())
print(dict.items())
dict["year"] = 2023
print(dict)
dict.update({"year":2000})
print(dict)
dict.update({"color":"red"})
print(dict)
dict.pop("color")
print(dict)
dict.popitem()
print(dict)
del dict["model"]
print(dict)
dict.clear()
print(dict)
del dict

dict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2000
}
for x in dict:
    print(x)
for x in dict:
    print(dict[x])
for x in dict.keys():
    print(x)
for x in dict.values():
    print(x)
for x,y in dict.items():
    print(x,y)

dict1 = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2000
}
dict2 = dict1.copy()
print(dict2)

child1 = {"name": "Keval"}
child2 = {"name": "Khyati"}
child = {
    "child1": child1,
    "child2": child2
    }
print(child)
print(child["child1"]["name"])

dict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2000
}
dict.setdefault("color","red")
print(dict)

#if else
a, b = 10, 20
if a<b: print("a is less than b")
print(b) if a<b else print(a)
a = b = 10
print(b) if a<b else print("equal") if a==b else print(a)

#recursion
def rec(k):
    if k>0:
        result = k + rec(k-1)
        print(result)
    else:
        result = 0
    return result
rec(6)

#lambda
x = lambda a : a + a
print(x(5))

#json
import json
x = '{"name":"Keval","age":22}'
y = json.loads(x)
print(y["name"])

x = {"name":"Keval","age":22}
y = json.dumps(x, indent=4, sort_keys=True)
print(y)

#regex
import re
txt = "My name is Keval"
print(re.findall("Keval",txt))#find
print((re.search("\s",txt)).start())#search
print(re.split("\s",txt,1))#split
print(re.sub("\s","-",txt))#replace

#exception
# x = -1
# if x<0:
#     raise Exception("Wrong")

try:
    f = open("demo.txt")
    try:
        f.write("Keval")
    except:
        print("Wrong")
    finally:
        f.close()
except:
    print("Wrong")
else:
    print("Not wrong")
finally:
    print("Finished")

#mysql
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mydatabase"
)
print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("KEVAL", "AHMEDABAD")
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount, " record inserted")
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [("KEVAL", "AHMEDABAD"),("KEVAL", "AHMEDABAD"),("KEVAL", "AHMEDABAD"),("KEVAL", "AHMEDABAD")]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount, " record inserted")
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# mycursor.execute("SELECT name,address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchone()
# print(myresult)
# sql = "SELECT * FROM customers WHERE address = 'AHMEDABAD'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# sql = "SELECT * FROM customers WHERE address LIKE '%BAD%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# sql = "DELETE FROM customers WHERE id = 5"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, " record deleted")
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("AHMEDABAD", "HIRAWADI")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, " row affected")