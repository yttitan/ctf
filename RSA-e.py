#!/usr/bin/python3

import libnum
import gmpy2

c = int(input("请输入c："))
e = int(input("请输入e："))
n = int(input("请输入n："))

k = 0
while True:
    result = gmpy2.iroot(k*n+c,e)
    k = k + 1
    if result[1]:
        print(k)
        print(libnum.n2s(int(result[0])))
        break

