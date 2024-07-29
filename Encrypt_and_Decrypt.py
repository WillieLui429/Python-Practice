from First_Encrypt import Encrypt
from First_Decrypt import Decrypt
phrase = input("Enter a phrase:")
ephrase = Encrypt(phrase)
print("The phrase encrypted is: " + ephrase)
dphrase = Decrypt(ephrase)
print("The phrase decrypted is: " + dphrase)