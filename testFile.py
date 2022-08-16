import hashlib
str = "sammy123"
result = hashlib.sha1(str.encode())
print(result.hexdigest())

#with open('top-10000-passwords.txt') as f:
    #lines = f.readlines()

#print(lines.replace("\n", ""))
#for i in lines:
    