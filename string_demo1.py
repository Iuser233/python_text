for i in range(12):
    print(chr(9800+i),end =" ")

print(ord('a'))


"2换行符和制表符"
print("language:\n\tpython\n\t")
#如果不想不想反斜杠1发生转义，在字符串前面加一个r

"3.字符串截取"
#3.1
str='language'
print(str[0:3])  #输出第一个到第三个字符
print(str[0:-1]) #输出第一个到倒数第二个字符
print(str*2)     #*表示复制，*2表示复制两次   
print(str+" python") #+表示连接
print(str+" python") #+表示连接

# #1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。
