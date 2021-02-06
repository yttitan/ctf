#!/usr/bin/python3

def fence(txt,key):
    flag = ''
    for i in range(key):
        for j in range(i,len(txt),key):
            flag = flag + txt[j]
    return flag

if __name__ == '__main__':
    txt = input('请输入明文或密文：').strip()
    key = []
    for m in range(2,len(txt)):
        if len(txt)%m == 0:
            key.append(m)
    for n in key:
        flag = fence(txt,n)
        print(f'{n}栏：{flag}')
