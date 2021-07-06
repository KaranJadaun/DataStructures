# This module is used to create arrays in python
# You can also use numpy array for it 
import array 

# Code for creating an array
# i for integers 
arr = array.array('i',[1,2,3,4])
arr2 = array.array('i',[5,6,7,8])

# Code for printing an array
for i in range(0,4):
    print(arr[i],end=" ")
# Output : 1 2 3 4 
# For printing new line
print("\r")

# Returns the datatype
print(arr.typecode)
# Output : 'i'

# Returns the size of array
print(arr.itemsize)
# Output : 4

# To print the buffer info
print(arr.buffer_info())
# Output : (40787152, 4)

# To count the number of occurences of element
print(arr.count(2))
# Output : 1

# Extend is used to add 2 arrays
arr.extend(arr2)
for i in range(0,8):
    print(arr[i],end=" ")
print("\r")
# Output : 1 2 3 4 5 6 7 8

list1 = [9,10,11]
# Used to append list at the end of array
arr.fromlist(list1)
for i in range(0,11):
    print(arr[i],end=" ")
print("\r")
# Output : 1 2 3 4 5 6 7 8 9 10 11 
# Used to convert an array into list 
list2 = arr.tolist()
print(list2)
# Output : [1,2,3,4,5,6,7,8,9,10,11]

# Thank you 
