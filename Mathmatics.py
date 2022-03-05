

# Count Digits
# n = int(input())
# i = 0
# while(n>0):
#     n //= 10
#     i += 1
# print(i)


# Palindrome Number Check
# n = str(input())
# if (n == n[::-1]):
#     print("Palindrome")
# else:
#     print("Nope")


# Factorial of Numbers
# n = int(input())
# def fact(n):
#     if (n == 0):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(n))


# GCD of Two Numbers
# num1 = int(input())
# num2 = int(input())
# num3 = max(num1, num2)
# num4 = min(num1, num2)
# rem = num3%num4
# while (rem == 0):
#     num3 = num4
#     num4 = rem
# print(rem)


# LCM of Two Numbers
# num1 = int(input())
# num2 = int(input())
# num3 = max(num1, num2)
# while (True):
#     if (num3%num1==0 and num3%num2 == 0):
#         print(num3)
#         break
#     else:
#         num3 += 1


# Prime Number Check
# num1 = int(input())
# count = 0
# for i in range(2,num1):
#     if (num1%i == 0):
#         count += 1
# print("Prime" if (count==0) else "Not Prime")


# Prime Numbers
# num1 = int(input())
# i = 2
# while (num1 != 1):
#     if (num1%i == 0):
#         num1 /= i
#         print(i)
#     else:
#         i += 1


# Sieve of Eraosthenes
# num1 = int(input())
# l = []
# k = []
# m = []
# for i in range(2,num1):
#     l.append(i)
# for i in range(2,num1):
#     for j in range(2,num1):
#         if (i%j==0):
#             k.append(i)
# for i in k:
#     if (k.count(i)==1):
#         m.append(i)
# for i in m:
#     print(i,end=" ")


# Computing Power
# num1 = int(input())
# num2 = num1
# pow = int(input())
# for i in range(1,pow):
#     num1 *= num2
# print(num1)


# Brian Kernighan's Algorithm
# num1 = int(input())
# def kenighan_algo(num1):
#     count = 0
#     while (num1!=0):
#         count += 1
#         num1 = num1 & num1-1
#     return count
# print(kenighan_algo(num1))
