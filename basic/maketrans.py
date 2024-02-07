str1="hello guys and welcome"
str2="abcde"
str3="12345"
t=str1.maketrans(str2, str3)
print(t)
print(chr(97))
print(str1.translate(t))
str=input("enter the number: ")

# for i in range(len(str)):
#     for j in range (i+1,len(str)+1):
#         print(str[i:j], end=" ")
#     print()    
# a ab abc abcd 
# b bc bcd
# c cd
# d
list1=[]
for i in range(len(str)):
    for j in range(i+1,len(str)+1):
        list1.append(str1[i:j])
    print(list1)    