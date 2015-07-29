#!/usr/bin/python
# -*- coding: utf8 -*-
__author__ = 'jokan'

'''
a = list("world")
print a
b = ['jacob',2]
print b
c = list(("list",2))
print c
d = [['list',3],['list'],[3]]
print d
'''

'''
a = ['hat',3,'girl',5,'david',1234]
print a[0]
print a[-1]
print type(a[0])
print a[0]+' hello'#heterogeneous hello
print a[1]+5#8
print a[1:3]#[3, 'girl']
print a[:2]#['heterogeneous', 3]
print a[2:]#['girl', 5, 'david', 1234]
print len(a)#6
print [min(a),max(a)]#[3, 'heterogeneous'] 比較開頭字母在ASCII編碼的號碼大小
print a[::2]
    #['heterogeneous', 'girl', 'david']
    #for(i=0;i<len(a);i+=2)
print a[::-1]
    #[1234, 'david', 5, 'girl', 3, 'heterogeneous']
    #for(i=len(a);i>0;i--)
print a[0:4:2]
    #['heterogeneous', 'girl']
    #for(i=0;i<4;i+=2)
a.append(987)
print a#['hat', 3, 'girl', 5, 'david', 1234, 987]
a.sort()
print a#[3, 5, 987, 1234, 'david', 'girl', 'hat']
a.reverse()
print a#['hat', 'girl', 'david', 1234, 987, 5, 3]
'''

'''
a = 'this is a book, I loves Qoo'
print 'cat' in a
print 'book' in a
'''

'''
import copy
a = [1,2,3]
aa = copy.deepcopy(a)#Deep Copy
aaa = a
print 'a: ',a
print 'aa:',aa
print 'aaa:',aaa
a[1]=2000
print 'a: ',a
print 'aa: ',aa
print 'aaa:',aaa
'''

'''
nums = [1,2,3,4]
ary = []
for n in nums:
    ary.append(n*n)
print ary
squares = [n*n for n in nums]
print squares
ifSquares = [n*n for n in nums if n<=2]
print ifSquares

fruits = ['apple','cherry','banana','lemon']
upperFruits = [s.upper() for s in fruits]
print upperFruits
ifFruits = [s for s in fruits if 'a' in s]
print ifFruits
'''

'''
contact_list = []
while True:
    contact = raw_input("Add Contact: ")
    if contact == 'done':
        break
    else:
        contact_list.append(contact)
        #print "You have %d contacts" %(len(contact_list))
        print "You have {} contacts".format(len(contact_list))
print "Your Contacts: %s" %(contact_list)
'''

'''
cnt = 0
while True:
    if cnt >=10:
        break
    cnt+=1#implicit "else"
    print cnt

a = 9
b = 8
for i in range(1,10):
    if i == a:
        print str(a)+' found!'
    elif i==b:
        print str(b)+' found!'
    else:
        print str(a)+','+str(b)+' was not in the list'
print('finished')
'''

'''
for i in range (1,10,2):
    print i,
print

a = [1,2,3,4,5]
for i in a:
    print i,
print

a=0
sum=0
while(i<101):
    sum+=i
    i+=1
print sum
print
'''
'''
def addNum(a,b):
    return a+b

print addNum(1,3)

import math
a = math.ceil(3.5)
print a
'''
'''
import sys #Importing Modules
for ele in dir(sys):
    if 'ar' in ele:
        print ele

print(sys.argv) #Print Argument

print range(1,len(dir(sys.argv)))
'''

'''
for ele in range(1,10):
    print ele, #output element
print

print range(1,10) #output list
'''

'''
contact_list = []

def add_contact(name):
    contact_list.append(name)
    print "You have %d contacts" %(len(contact_list))

def get_contact():
    print "Your contacts: %s" %(contact_list)

def main():
    while True:
        contact = raw_input("Add Condact: ")
        if contact == "done":
            break
        else:
            add_contact(contact)
    get_contact()

if __name__ == "__main__":
    main()
'''

'''
a = range(1,100)
for page in a:
    if page == 55:
        print page
'''
'''
a = {'a':1,'b':2,'c':3,'z':26}
a['d'] = 4
a.update({'e':5,'f':6})
print a['z'],a['a']
print a.keys()
print a.values()
print a.get('b')
for rec in a:
    print rec,a[rec]
'''
'''
def switch_case(n):
    return  {'1':'case1','2':'case2'}.get(n)
print switch_case('1')
print switch_case('2')
print switch_case('3')
'''
'''
a = [1,2,3]
print type(a)
print dir(a)
b = (1,2,3)
print type(b)
print dir(b)
'''
'''
a = 1
b = 2
a,b = b,a
print a,b
'''
'''
a = 1
del a
print a
'''
'''
def func():
    return 1,2,3
a,b,c = func()
print a,b,c
'''

'''
for id, i in enumerate(range(1,10)):
    print "id %d : %d" %(id,i)
'''
'''
class Person():
    count = 0
    def __init__(self, name,city):
        self.name = name
        self.city = city
        Person.count +=1
    def number_of_person(self):
        return Person.count

first = Person('David','Singaport')
print first.number_of_person()
second = Person('Joy','Hsinchu')
print second.number_of_person()
print first.name, first.city
print second.name, second.city
'''
'''
class MyInteger():
    def __init__(self,integer):
        print 'constructor'
        self.integer = integer
    def __add__(self, integer):
        if reself.integer == 2 and integer==2:
            return 999
        else:
            return self.integer+integer

a = MyInteger(2)
print a+2
print a+3
'''

'''
class Vehicle():
    def my_own(self): return True
class Bicycle(Vehicle):
    def __init__(self,color): self.color = color
    def has_wheel(self): return True
    def __str__(self):return "%s is %s"%(self.__class__.__name__,self.color)
    # __str__:convert to string when printing object
class rent_Bike(Bicycle):
    def my_own(self): return False

Ubike = rent_Bike('yellow')
print "Has Wheel: %s" %(Ubike.has_wheel())
print "Color: %s"%(Ubike.color)
print "My_Own: %r" %(Ubike.my_own())
print
Giant = Bicycle('white')
print "Has Wheel: %s" %(Giant.has_wheel())
print "Color: %s" %(Giant.color)
print "My_Own: %r" %(Giant.my_own())
print Giant
print
Honda = Vehicle()
print Honda
print
print dir(Ubike)
print dir(Giant)
print dir(Honda)
'''
'''
fid = open('test.txt','w')
fid.write('Hello\nWorld\nNice to meet you\nI\'m Jacob')
fid.close()

fid = open('test.txt','r')
for line in fid:
    print("Line:"+line.strip())
fid.close

fid = open('test.txt','r')
s = fid.read()
fid.close()
print "line",s

fid = open('test.txt')
k=0
for line in fid:
    k = k+1
print(k)
fid.close()

f = open('test.txt','r')
cnt = 0
for line in f.readlines():
    print line.strip()
f.close()
'''

print len([line for line in open('test.txt')])
ary = []
for line in open('test.txt'):
    ary.append(line)
print len(ary)
print ary

