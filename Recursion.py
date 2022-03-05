# Factorial Using Recursion 
# num1 = int(input())
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(num1))


# Fibonacci Using Recursion
# num1 = int(input())
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(num1):
#     print(fib(i),end=" ")


# Print n to 1 Using Recursion
# num1 = int(input())
# def prin(n):
#     if n <= 0:
#         return
#     else:
#         print(n,end=" ")
#         prin(n-1)
# prin(num1)


# Print 1 to n Using Recursion
# num1 = int(input())
# def prin(n):
#     if n <= 0:
#         return
#     else:
#         prin(n-1)
#         print(n)
# prin(num1)


# Checking Palindrome Using Recursion
# s = str(input())
# def check(s):
#     if len(s)<1:
#         return True
#     else:        
#         if s[0] == s[-1]:
#             return check(s[1:-1])
#         else:
#             return False
# if(check(s)==True):
#    print("The string is a palindrome")
# else:
#    print("The string isn't a palindrome")


# Sum of digits Using Recursion
# num1 = int(input())
# def sum(num1):
#     if num1==0:
#         return 0
#     return (num1 % 10 + sum(int(num1/10)))
# print(sum(num1))


#  Rod Cutting method is of Dynamic Programming


# Subsets of given set
# import itertools
# def findsubsets(set, num):
#     return list(itertools.combinations(set, num))
# s = list(map(int, input().split()))
# n = int(input())
# print(findsubsets(s,n))


# Tower of Hanoi is in my github repository


# Josephus Problem ( Nice problem :-))
# def who_goes_free(tot, k):
#     I = []
#     for i in range(tot):
#         I.append(i)
#     c = k-1
#     while(len(I)>1):
#         item = I[c%len(I)]
#         ic = c%len(I)
#         I.pop(ic)
#         c += k-1
#         c = c%len(I)
#     return I
# print(who_goes_free(9,2))
