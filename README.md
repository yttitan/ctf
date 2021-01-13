# 自己编写的以及从网上收集的一些CTF比赛用的脚本
脚本逻辑以及相关的具体知识点可参考我在51CTO学院的视频课程：https://edu.51cto.com/sd/ac096
## base1.py适用于Base家族循环解码类的题目：
```
root@kali:~/mygit# ./base1.py 
请输入要解码的文件路径：/root/ctf/base.txt
flag{b4Se_Fami1y_Is_FUn}
```
## base2.py可解所有的Base家族编码，这是个Python2的脚本：
```
root@kali:~/mygit# python base2.py 
Input base:@iH<,{bdR2H;i6*Tm,Wx2izpx2!
[-] b16decode wrong
[-] b32decode wrong
[-] b36decode wrong
[-] b58decode wrong
[-] b62decode wrong
[-] b64decode wrong
[-] b85decode wrong
[+] b91decode:flag{554a5058c9021c76} 
[-] b92decode wrong

```
