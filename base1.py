#!/usr/bin/python3

import base64
filename = input("请输入要解码的文件路径：")
with open(filename,"r") as f:
    txt = f.read()
    
while True:
    try:
        txt = base64.b32decode(txt).decode()
    except:
        try:
            txt = base64.b64decode(txt).decode()
        except:
            try:
                txt = base64.b16decode(txt).decode()
            except:
                try:
                    txt = base64.b85decode(txt).decode()
                except:
                    break
print(txt)
