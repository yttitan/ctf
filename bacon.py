#!/usr/bin/python3

def trans(txt): 
    '''将大小写字母分别转换为ab和ba'''
    result1 = result2 = ''
    for i in txt:
        if i.isupper():
            result1 = result1 + 'a'
            result2 = result2 + 'b'
        elif i.islower():
            result1 = result1 + 'b'
            result2 = result2 + 'a'
    return result1,result2

def bacon(txt):
    '''对密文按两种不同的密码表分别解密'''
    cipher1 = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","babaa","babab","babba","babbb"]
    plain1 = ['a','b','c','d','e','f','g','h','(ij)','k','l','m','n','o','p','q','r','s','t','(uv)','w','x','y','z']
    key1 = dict(zip(cipher1,plain1))
    cipher2 = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","babaa","babab","babba","babbb","bbaaa","bbaab"]
    plain2 = 'abcdefghijklmnopqrstuvwxyz'
    key2 = dict(zip(cipher2,plain2))
    try:
        flag1 = ''
        for i in range(0,len(txt),5):
            flag1 = flag1 + key1.get(txt[i:i+5])
    except:
        pass
    try:
        flag2 = ''
        for i in range(0,len(txt),5):
            flag2 = flag2 + key2.get(txt[i:i+5])
    except:
        pass

    return flag1,flag2

if __name__ == '__main__':
    txt = input('请输入密文：')
    if 'aaa' in txt or 'AAA' in txt:#判断是否是AB形式的标准密文
        txt = txt.replace(' ','').lower()
        flag1,flag2 = bacon(txt)
        print('标准培根密码表：',flag1)
        print('扩展培根密码表：',flag2)
    else:                           #对于大小写形式的密文，会给出4个解密结果
        result1,result2 = trans(txt)
        flag1,flag2 = bacon(result1)
        flag3,flag4 = bacon(result2)
        print('标准培根密码表：',flag1,flag3)
        print('扩展培根密码表：',flag2,flag4)

