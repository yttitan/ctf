#!/usr/bin/python3

txt = input("请输入密文：")
confirm = input("需要推荐明文吗?(Y/N)").strip().lower()
print()

for key in range(1,26):
    plain = ''
    for i in txt:
        if i.isupper():
            plain = plain + chr(65+(ord(i)-65-key)%26)
        elif i.islower():
            plain = plain + chr(97+(ord(i)-97-key)%26)
        else:
            plain = plain + i

    if confirm == "y":
        words = ('flag','key','ctf','is','the','you','to','have','for','than')
        for j in words:
            if j in plain.lower():
                print("明文可能是：",plain)
                print()
                break
    elif confirm == "n":
        print(plain)
        print()
