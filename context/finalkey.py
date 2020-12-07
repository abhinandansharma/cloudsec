from cryptography.fernet import Fernet


def finalkeygeneration(key,data):
    if(len(key) > 0):
        s = Fernet(key)
        encrypt = s.encrypt(data) # In byte
    else:
        key = Fernet.generate_key()
        s = Fernet(key)
        encrypt = s.encrypt(data)


    return (encrypt,key)

def keydecryption(key,data):
    s = Fernet(key)
    decryptdata = s.decrypt(data)
    return decryptdata