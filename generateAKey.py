# use pip install cryptography to install the lib

#generate a symmetric key
from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open('myTopSecretKey.key', 'wb') as file:
    file.write(key)
