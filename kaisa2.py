#!/usr/bin/python3

txt = input("请输入密文：")
confirm = input("需要推荐明文吗?(Y/N)").strip().lower()
print()

for key in range(1,94):
    plain = ''
    for i in txt:
        plain = plain + chr(33+(ord(i)-33-key)%94)

    if confirm == "y":
        words = ('flag','key','ctf','is','about','the','you','to','have','for','much','than')
        for j in words:
            if j in plain.lower():
                print("明文可能是：",plain)
                print()
                break
    elif confirm == "n":
        print(plain)
        print()
