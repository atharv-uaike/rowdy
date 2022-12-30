s = input()
print('['+','.join([chr(ord(i)+1) for i in s if i!='z' and i!='z']) +']')
