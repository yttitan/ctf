#!/usr/bin/python3

import hashlib

for a in range(33,127):
    for b in range(33,127):
        flag = chr(a) + chr(b)
        s = "You_are_" + flag +"_good" 
        md5 = hashlib.md5(s.encode()).hexdigest()
        if md5 == "77d7cf3f2ec29e86025118b3ff265649":
            print(flag)
            exit

