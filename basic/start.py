# i=5
# for i in range(i):
#     for j in range(i+1):
#         print("*", end="" )
#     print()

    
# i = int(input("Enter the number "))
# for i in range(i):
#     for j in range(i+1):
#          print("*", end="" )
#     print()
# # output
# *
# **
# ***
# ****
# *****
# num = int(input("Enter the number "))
# for i in range(num):
#     # for use space
#     for j in range(num-i-1):
#          print(" ", end="")
#         #  for use pattern
#     for j in range(i+1):
#          print("*", end="" )
#     print()
#     *
#    **
#   ***
#  ****
# *****
# num = int(input("Enter the number "))
# for i in range(num):
#     # for use space
#     for j in range(num-i-1):
#          print(" ", end="")
#         #  for use pattern
#     for j in range(i+1):
#          print("*", end=" " )
#     print()
# n=int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print("*", end="")
#     for j in range(i+1):
#         print(" ", end="")  
#     print()      
#     output
#     Enter the number: 5
# ****
# ***
# **
# *
# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n-i):
#         print("*", end="")     
#     print()      
#     output
# *****    
#  ****
#   ***
#    **
#     * 
# r=4
# for i in range (1, r+1):
#     num =i
#     for j in range (1, i +1):
#         print(num, end=" ")
#         num +=r-j
#     print()    
# output
# 1 
# 2 5
# 3 6 8
# 4 7 9 10
r=4
for i in range(1,r+1):
    num=i

    for j in range(1, i+1,):
        print(num, end=" ")
        num +=r+j
    print()



