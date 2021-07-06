# This module is used to create arrays in python
# You can also use numpy array for it 
import array 

# Code for creating an array
# i for integers 
arr = array.array('i',[1,2,3,4])

# Code for printing an array
for i in range(0,4):
    print(arr[i],end=" ")
# Output : 1 2 3 4 
# For printing new line
print("\r")

# Append is used to add elements in array 
arr.append(6)
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")
# Output : 1 2 3 4 6 

# Insert is used used to add 43 at index 0     
arr.insert(0,43)
for i in range(0,6):
    print(arr[i],end=" ")
print("\r")
# Output : 43 1 2 3 4 6 

# Pop will remove the first occurence of the number
arr.pop(2)
for i in range(0,5):
    print(arr[i],end=" ")
print("\r")
# Output : 43 1 3 4 6

# Remove the element from the array    
arr.remove(4)
for i in range(0,4):
    print(arr[i],end=" ")
print("\r")
# Output : 43 1 3 6

# For printing the value of index
print(arr.index(6))
# Output : 3

# Reverse is used to reverse the array
arr.reverse()
for i in range(0,4):
    print(arr[i],end=" ")
print("\r")
# Output : 6 3 1 43 

# Thank you 
