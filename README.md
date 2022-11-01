# 自己编写的以及从网上收集的一些CTF比赛用的脚本
脚本逻辑以及相关的具体知识点可参考我在51CTO学院的视频课程：https://edu.51cto.com/sd/ac096
## 1. 解码或解密类脚本
### base1.py适用于Base家族循环解码类的题目：
```
# ./base1.py 
请输入要解码的文件路径：/root/ctf/base.txt
flag{b4Se_Fami1y_Is_FUn}
```
### base2.py可解所有的Base家族编码，这是个Python2的脚本：
```
# python base2.py 
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
# ./baseStego.py 
请输入要提取隐写信息的文件路径：stego.txt
Base_sixty_four_point_five
```
### morse.py可解密摩斯密码，密码之间可以是空格间隔，也可以是/间隔。密码形式可以是.-，也可以是01，同时输出大小写明文。
```
# ./morse.py 
11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110
MORSECODEISSOINTERESTING
morsecodeissointeresting
# ./morse.py 
..-. .-.. .- --. . --... .---- -.-. .- ..... -.-. -.. -....- --... -.. -... ----. -....- ....- -... .- ...-- -....- ----. ...-- ---.. ...-- -....- .---- .- ..-. ---.. -.... --... ---.. ---.. .---- ..-. ----- --...
FLAGE71CA5CD-7DB9-4BA3-9383-1AF867881F07
flage71ca5cd-7db9-4ba3-9383-1af867881f07
```
### kaisa.py可解凯撒密码，以大小写英文字母作为密码表，并能自动推荐最有可能的明文。
### kaisa2.py以所有可打印字符作为密码表，在kaisa.py脚本无法正常解密的情况下可尝试使用。
```
# ./kaisa.py 
请输入密文：synt{mur_VF_syn9_svtug1at}
需要推荐明文吗?(Y/N)y

明文可能是： flag{zhe_IS_fla9_fight1ng}
```
### bacon.py可解培根密码，分别用两种密码表解密，并自动将英文大小写字母转换为AB形式的标准密文。
```
# ./bacon.py 
请输入密文：bacoN is one of aMerICa'S sWEethEartS. it's A dARlinG, SuCCulEnt fOoD tHAt PaIRs FlawLE
标准培根密码表：  bacon(ij)snotfood
扩展培根密码表：  bacnmirmnsfnnd
```
### fence.py可解栅栏密码
```
# ./fence.py 
请输入明文或密文：flag{6fde4163df05d900}
2栏：fa{fe13f590lg6d46d0d0}
11栏：f6l3adgf{065fdd9e0401}
```
### md5.py和md5-2.py可对MD5暴力破解，以可打印ASCII码作为取值范围，可根据实际情况进行调整。
```
md5.py采用纯暴力破解。
md5-2.py采用了迭代器，效率更高。
```
### RSA-e.py用于RSA低加密指数分解攻击，即e比较小的情况。脚本运行时需要输入n、e、c。
### RSA-n.py用于RSA共模攻击，即m和n相同的情况。脚本运行时需要输入n、e、c。
### crsFix.py用于修复图片crc错误，图片要命名为1.png，而且要与脚本放在同一个目录中，修复后会生成1.png.png。
```
python crcFix.py
```

## 2. Web安全类脚本
### blind.py是采用二分法编写的布尔盲注脚本，脚本以SQLi-labs Less-5为例。
### sql.py是SQL注入的Fuzz测试脚本，sql.txt是测试字典。
