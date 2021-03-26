#!/usr/bin/python3

import hashlib
import itertools

a = b = [chr(n) for n in range(33,127)]
x = itertools.product(a,b)
for i in x:
    flag = ''.join(i)
    s = "You_are_" + flag +"_good" 
    md5 = hashlib.md5(s.encode()).hexdigest()
    if md5 == "77d7cf3f2ec29e86025118b3ff265649":
        print(flag)
        break
