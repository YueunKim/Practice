# 10단원 연습문제
#
#
#1
# a=input("문장 =")
# b=a[0]
# c=b.upper()
# print(c,a[1:])

#
# #2
# b=input("내용을 입력하세요")
# c=len(b)
# d=b.split()
# e=len(d)
# print("글자수 =", c, "단어수 =", e)
#
#
# #3
# str1 = "My name is John"
# str2 = "I like chicken"
# str3 = "My hobby is football"
#
# name=input("이름 = ")
# food=input("좋아하는 음식 = ")
# hobby=input("취미 = ")
#
# print(str1.replace('John', name))
# print(str2.replace('chicken', food))
# print(str3.replace('football', hobby))
#
#
# #4
# a=input("이름/음식/취미 =")
# b=a.split("/")
# print(str1.replace('John', b[0]))
# print(str2.replace('chicken', b[1]))
# print(str3.replace('football', b[2]))


##################10단원 3,4번

# #1
# def TF(alp): # 글자 하나
#     a=ord(alp)
#     if a>=97 and a<=122:
#         return False
#     elif a>=65 and a<=90:
#         return True
#     else:
#         return "알파벳이 아닙니다"


# #3

# abc=input("")

# def change(abc):
#     a = ""
#     for i in range(len(abc)):
#         if ord(abc[i])>=65 and ord(abc[i])<=90:
#             b=ord(abc[i])+32
#             a+=chr(b)
#         else:
#             b=ord(abc[i])-32
#             a+=chr(b)

#     return a

# print(change(abc))


# #4

# number = input("")
# number1=""
# def myint(number):
#     for i in range(0,len(number)):
#         number1.append(ord(number[i]))

#     return number1

# print(number1)

# print(number1 + 1)


# alp = '1053'
# ascii = []
# for x in range(0, len(alp)):
#     ascii.append(ord(alp[x]))
# str1 = ''
# for x in range(0, len(ascii)):
#     str1 = str1 + chr(ascii[x])
# print(str1)

# print(str1+1)


############### 카이사르 암호

# def caesar(c):
#     a = list(c)
#     for i in range(len(a)):
#         if ord(a[i])>=65 and ord(a[i])<=90:
#             a[i]=chr((ord(a[i])-ord('A')+3)%26+ord('A'))
#         elif ord(a[i])>=97 and ord(a[i])<=122:
#              a[i]=chr((ord(a[i])-ord('a')+3)%26+ord('a'))
#     b = "".join(a)

#     return b

# print(caesar("I Love You"))


# 암호해독

# def decode(c):
#     a = list(c)
#     for i in range(len(a)):
#         if ord(a[i])>=65 and ord(a[i])<=90:
#             a[i]=chr((ord(a[i])-ord('A')-3)%26+ord('A'))
#         elif ord(a[i])>=97 and ord(a[i])<=122:
#              a[i]=chr((ord(a[i])-ord('a')-3)%26+ord('a'))
#     b = "".join(a)

#     return b

# print(decode("L Oryh Brx"))
