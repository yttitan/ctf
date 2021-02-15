#!/usr/bin/python3

txt = input('请输入密文：')
password = input('请输入密钥：').lower()
key = [ord(i)-97 for i in password]
flag = ''
m = 0 #循环变量m专门用于对密钥取值

for i in range(len(txt)):
    if txt[i].islower():
        flag = flag + chr(97+(ord(txt[i])-97-key[m%len(key)])%26)
        m = m + 1
    elif txt[i].isupper():
        flag = flag + chr(65+(ord(txt[i])-65-key[m%len(key)])%26)
        m = m + 1
    else:
        flag = flag + txt[i]

print(flag)

