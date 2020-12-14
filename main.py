print("""What do you want to do with message?
e = encrypt message
d = decipher message""")

choose = input()

  
alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("Please enter a message to encrypt or decipher:").lower()

encryptedmessage = ""

key = input("Please enter the key: ")
key = int(key)

if choose == 'e':
  for char in message:
    if char in alphabet:
      position = alphabet.find(char)
      newposition = (position + key) %26
      encryptedmessage = encryptedmessage + alphabet[newposition]
    else:
      encryptedmessage = encryptedmessage + char 
elif choose == 'd':
  for char in message:
    if char in alphabet:
      position = alphabet.find(char)
      newposition = (position - key) %26
      encryptedmessage = encryptedmessage + alphabet[newposition]
    else:
      encryptedmessage = encryptedmessage + char 

print("Your encrypted message is: ",encryptedmessage)