# 1.请输入一盒年龄：33
myage =  input("请输入一个年龄:")
print(myage)
# 2.把这个年龄添加到：迪迦的年龄是33
myname = input("请输入你的姓名：")
# myname_age = myname + "的年龄是" + myage
myname_age = "{}的年龄是{}".format(myname,myage)
print(myname_age)
print(type(myname_age))
# 3.再把这个字符串添加到数组中a = []
a = []
a.append(myname_age)
print(a)
# 4.再添加一个奥特曼字符串
b = "奥特曼"
a.append(b)
print(a)
# 5.统计奥特曼在a数组中出现的个数
el = a.count("奥特曼")
print(el)



