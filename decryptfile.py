# Read key from file
key = ''
with open('myTopSecretKey.key', 'rb') as file:
    key = file.read()

# Read the encrypted data
encryptedData = ''
with open('myTopSecretInfo.txt', 'rb') as file:  # fixed variable name
    encryptedData = file.read()

# Decrypted data
from cryptography.fernet import Fernet

f = Fernet(key)

# Decrypt the data
decryptedData = f.decrypt(encryptedData)

# Print the encrypted and decrypted data
print('Encrypted data:', encryptedData.decode())

print()

print('Decrypted data:', decryptedData.decode())
