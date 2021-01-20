#!/usr/bin/python3

filename = input("请输入要提取隐写信息的文件路径：")
#变量txt1用于存放Base64索引
#变量txt2用于存放Base64编码转换后的二进制数
#变量flag用于存放最终要提取的隐写数据
#变量base用于存放Base64码表
txt1 = txt2 = flag = ''
base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

with open(filename,"r") as f:
    for line in f:
        line = line.strip() #去除每行最后的换行符
        if line[-2:] == "==":
            txt1 = base.index(line[-3]) #取出倒数第3个字符的Base64索引
            txt2 = bin(txt1)[2:].zfill(6) #将索引转换为长度固定为6的二进制数
            flag = flag + txt2[-4:] #将后4位(隐写位)的数据累加存放到变量flag中
        elif line[-1] == "=":
            txt1 = base.index(line[-2]) #取出倒数第2个字符的Base64索引
            txt2 = bin(txt1)[2:].zfill(6)
            flag = flag + txt2[-2:] #将后2位(隐写位)的数据累加存放到变量flag中

#将隐写数据转换为ASCII字符
try:
    for i in range(0,len(flag),8):
        print(chr(int(flag[i:i+8],2)),end='')
except:
    pass
print()

