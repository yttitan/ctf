#!/usr/bin/python3

import libnum
import gmpy2

n = **************
e1 = ************
e2 = ************
c1 = ************
c2 = ************

s1 = int(gmpy2.gcdext(e1,e2)[1])
s2 = int(gmpy2.gcdext(e1,e2)[2])
m = pow(c1,s1,n) * pow(c2,s2,n) % n
print(libnum.n2s(m))
