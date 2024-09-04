"""
'''
DATA STRUCTURES
--------------
list
tuple
set
dictionary

--------------------------------------------------------------------------------
list
----
list is an datastructure
unique(ordered)or(positioned)collection of different datatypes element(items)
list will including duplicate elements

                    mark=[3,"m",True,5.6,]
positive indexing -       0  1    2   3
negative indexing -      -4 -3   -2   -1
--------------------------------------------------------------------------------

'''
mark=[3,"m",True,5.6,]

print(mark)
print(mark[3])
print(mark[-1])
mark[3]="hi"
print(mark[3])
print(len(mark))

'''
slicing of list
----------------
slicing is splitting of the list and make a new list from it by giving start and ending point
slicing [start:end:steps]
'''
data =[10,20,30,40,50,60]
    #  0  1  2  3  4  5
    # -6 -5 -4 -3 -2 -1
    
#slicing [start:end:steps]
print(data[1:4])  #[20, 30, 40]
print(data[1:])   #[20, 30, 40, 50, 60]
print(data[:4])   #[10, 20, 30, 40]
print(data[:6])   #[10, 20, 30, 40, 50, 60]
print(data[-5:-1])#[20, 30, 40, 50]
print(data[:-4])  #[10, 20]
print(data[-1:])  #[60]

#steps
#-----
#print(data[first pos:sec pos:steps])
print(data[0:5:2])
print(data[-2:-3:-1])
print(data[-2:-5:-1])#revers order
print(data[::-1])#revers order
print(data[1:3:4])#[20]
a=[1,2,3,4,5,6]
print(a[-2:-4:-1])
print(a[2:4:1])
print(a[2:4:])
"""       
'''
-------------------------------------------------------------------------------
funtions of list(list methods)
------------------------------
append()
---------
append() function or method is used to add data or element in last position (into a excisting list'''

mark=[30,40]
mark.append(55)
     
'''   
insert()
--------
used to insert an item in a specific position'''
mark=[30,40]
mark.insert(1,55)
#          (pos,elemnt)
'''
remove()
--------
used to remove an item from list'''

mark=[30,40]
print(mark.remove(30)
'''
pop()
-----
used to delete or remove an item from a specific position'''
mark=[30,40]
mark.pop(1)
       #pos
'''
operation on list
-----------------'''
