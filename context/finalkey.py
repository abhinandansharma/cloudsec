from cryptography.fernet import Fernet


def finalkeygeneration(data):
    data = data.encode()
    key = Fernet.generate_key()
    s = Fernet(key)
    encrypt = s.encrypt(data)
    return ( encrypt, key)

def keydecryption(key,data):
    s = Fernet(key)
    decryptdata = s.decrypt(data)
    return decryptdata
