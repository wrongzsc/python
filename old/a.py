xxx = "xx dh fgjtym thrthb thed xyc@sc.net dvdfnxbgh  fcntv fgjbx cgnghh"
x = xxx.find("@")
x1 = xxx[0:x].rfind(" ")
x2 = xxx[x:].find(" ")
xall = xxx[x1 + 1:x + x2]

print(x)
print(x2)
print(xall)
print(xxx)

x = 20

if x > 20:
    print(x)

if x < 19:
    print("shit")

print("aaa")

k = 1
while k < 5:
    print(k)
    k = k + 1

k = 1
while (True):
    print(k)
    k = k + 1
    if (k >= 5):
        break

print("sha")

str = input("请输入：")
str = int(str)
if str == 10:
    print("ooo")
else:
    print("xxx")

print("你输入的内容是: ", str)


def MAX(a, b):
    if a == b:
        print("max={0}and{1}", a, b)
    elif a > b:
        print("max=", a)
    else:
        print("max=", b)


MAX(3, 4)
