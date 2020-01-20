encoded_mess = input()
key_int = int(input())
summer = 0
for i in (key_int).to_bytes(2,'big'):
    summer += i
strin = ''
for i in encoded_mess:
    strin += chr(ord(i)+summer)
print(strin)
