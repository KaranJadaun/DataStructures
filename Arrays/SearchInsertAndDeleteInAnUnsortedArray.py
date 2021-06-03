# Basic Functions of an Array Discussed

# Enter Array
n = list(map(int, input("Enter Array ").split()))

# Operation from search, insert and delete
b = input("Enter Operation ")

# Enter Element on which operation has to be performed
a = int(input("Enter Element on which operation has to be performed "))

# Defining function for search operations
def search(n, a):
    for i in range(len(n)):
        if n[i] == a:
            return i
    return "Not Found"
  
# Conditional Statements for Checking b
if b == "search":
    d = search(n, a)
    if d != "Not Found":
        print("Element is Present at", str(d+1))
    else:
        print("Element is Not Present")
        
elif b == "insert":
    n.append(a)
    print(n)
    
elif b == "delete":
    n.remove(a)
    print(n)

else:
    print("Invalid Operation")
    
# Thank you
