import string
import binascii
import struct
from base64 import b16decode,b32decode,b64decode

def b36decode(s):
    key = '0123456789abcdefghijklmnopqrstuvwxyz'
    value = ''

    while number != 0:
        s, index = divmod(number, len(key))
        value = key[index] + s
    return value or '0'

def b58decode(s):#base58 have 2 table 
    key=['123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
         '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ']
    return hex(sum([j*(58**i) for i,j in enumerate([key[0].index(i) for i in s][::-1])]))[2:].decode('hex')
    #return [hex(sum([j*(58**i) for i,j in enumerate([key[k].index(i) for i in s][::-1])]))[2:].decode('hex') for k in range(2)]
    #return list with two table 

def b62decode(s):
    key=["0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
         "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    if s.startswith("0z"):
        s = s[2:]

    ret=0
    for i in range(len(s)):
        ret += key[0].index(s[i]) * (62 ** (len(s) - (i + 1)))

    return hex(ret)[2:].decode('hex')

def b85decode(s):
    b85dec = [None] * 256
    for i, c in enumerate(map(ord,"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")):
        b85dec[c] = i
    padding = (-len(s)) % 5
    s = s + '~' * padding
    out = []
    packI = struct.Struct('!I').pack
    for i in range(0, len(s), 5):
        chunk = s[i:i + 5]
        acc = 0
        for c in map(ord,chunk):
            acc = acc * 85 + b85dec[c]
        out.append(packI(acc))
    result = ''.join(out)
    if padding:
        result = result[:-padding]
    return result

def b91decode(s):
    ''' Decode Base91 string to a bytearray '''
    key='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'
    v = -1
    b = 0
    n = 0
    ret = ''
    for letter in s:
        if not letter in key:
            continue
        c = key.index(letter)
        if (v < 0):
            v = c
        else:
            v += c * 91
            b |= v << n
            n += 13 if (v & 8191) > 88 else 14
            while True:
                ret += struct.pack('B', b & 255)
                b >>= 8
                n -= 8
                if not n > 7:
                    break
            v = -1
    if v + 1:
        ret += struct.pack('B', (b | v << n) & 255)
    return ret

def b92decode(s):   
    key="!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}"
    bitstr = ''
    resstr = ''
    if s == '~':
        return ''
    # we always have pairs of characters
    for i in range(len(s)/2):
        x = key.index(s[2*i])*91 + key.index(s[2*i+1])
        bitstr += '{:013b}'.format(x)
        while 8 <= len(bitstr):
            resstr += chr(int(bitstr[0:8], 2))
            bitstr = bitstr[8:]
    # if we have an extra char, check for extras
    if len(s) % 2 == 1:
        x = key.index(s[-1])
        bitstr += '{:06b}'.format(x)
        while 8 <= len(bitstr):
            resstr += chr(int(bitstr[0:8], 2))
            bitstr = bitstr[8:]
    return resstr

def De2Any(num, key):# Decimal To any jinzhi 
    ret=[]
    while(num>=key):
        ret.append(num%key)
        #print "%s -> %s"%(a,ret)
        num/=key
    else:
        ret.append(num)
        ret.reverse()
        return ret
    print "Wrong In De2Any!"


def base(s):#16 32 36 58 62 64 85 91 92 
    # 105
    ret=[]
    fun_table=[b16decode,b32decode,b36decode,b58decode,b62decode,b64decode,b85decode,b91decode,b92decode]
    for i in fun_table:
        try:
            if '32' in i.func_name or '64' in i.func_name:#b32 b64 +buf
                temp=i(s+'='*(len(s)%8))
            else:
                temp=i(s)

            if check(temp):
                ret.append(i(s))
                print '\033[1;34;40m[+]\033[1;33;40m %s:%s \033[0;37;40m'%(i.func_name,i(s))
            else:
                print '[-] %s wrong'%i.func_name
        except:    
            print '[-] %s wrong'%i.func_name
    print '\033[0;31;40m-------------------------------------\033[0;37;40m'
    return ret
    #return [b16decode(s),b32decode(s),b64decode(s),b85decode(s),]

def check(s):
    import string
    table=string.printable
    if sum([i in table for i in s])==len(s):
        return 1
    return 0


if __name__=='__main__':
    s=raw_input('Input base:')
    ret=[]
    while(1):
        s=base(s)
        if len(s)!=1:
            break
        s=s[0]
