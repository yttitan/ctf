# 自己编写的以及从网上收集的一些CTF比赛用的脚本
脚本逻辑以及相关的具体知识点可参考我在51CTO学院的视频课程：https://edu.51cto.com/sd/ac096
## 1. 解码或解密类脚本
### base1.py适用于Base家族循环解码类的题目：
```
root@kali:~/mygit# ./base1.py 
请输入要解码的文件路径：/root/ctf/base.txt
flag{b4Se_Fami1y_Is_FUn}
```
### base2.py可解所有的Base家族编码，这是个Python2的脚本：
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
### baseStego.py可提取Base64隐写信息
```
root@kali:~/mygit# ./baseStego.py 
请输入要提取隐写信息的文件路径：stego.txt
Base_sixty_four_point_five
```
### morse.py可解密摩斯密码，密码之间可以是空格间隔，也可以是/间隔。密码形式可以是.-，也可以是01，同时输出大小写明文。
```
root@kali:~/mygit# ./morse.py 
11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110
MORSECODEISSOINTERESTING
morsecodeissointeresting
root@kali:~/mygit# ./morse.py 
..-. .-.. .- --. . --... .---- -.-. .- ..... -.-. -.. -....- --... -.. -... ----. -....- ....- -... .- ...-- -....- ----. ...-- ---.. ...-- -....- .---- .- ..-. ---.. -.... --... ---.. ---.. .---- ..-. ----- --...
FLAGE71CA5CD-7DB9-4BA3-9383-1AF867881F07
flage71ca5cd-7db9-4ba3-9383-1af867881f07
```
