import hashlib

def crack_sha1_hash(hash, use_salts = False ):
    if use_salts == False:
        with open('top-10000-passwords.txt') as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                if(hashit(line) == hash):
                    return line
            return "PASSWORD NOT IN DATABASE"

    elif use_salts == True:
        with open('top-10000-passwords.txt') as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                with open('known-salts.txt') as foo:
                    for salt in foo.readlines():
                        salt = salt.replace("\n", "")
                        psaltedLine = salt + line 
                        AsaltedLine = line + salt
                        if(hashit(psaltedLine) == hash or hashit(AsaltedLine) == hash):
                            return line
                    
            return "PASSWORD NOT IN DATABASE"


def hashit(hash):
    result = hashlib.sha1(hash.encode())
    #if (result.hexdigest() == hash):
    return result.hexdigest()