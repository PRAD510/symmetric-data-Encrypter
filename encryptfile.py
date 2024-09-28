# Read key from file
key = ''
with open('myTopSecretKey.key', 'rb') as file:
    key = file.read()

# Read data from file
data = ''
with open('toBeSecret.txt', 'r') as file:  # changed to 'r' for reading text
    data = file.read()

# Encrypt data
from cryptography.fernet import Fernet

f = Fernet(key)

# Encode the data to bytes before encryption
encryptedData = f.encrypt(data.encode())  # ensure text is converted to bytes

# Save the encrypted data into a file
with open('myTopSecretInfo.txt', 'wb') as file:
    file.write(encryptedData)
