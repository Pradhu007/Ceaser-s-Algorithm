alphabetandnumbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910
#Contains the Alphabet from A-Z and numbers from 1-9 



print("WELCOME TO THE STRING ENCRYPTION ALGORITHM  \nby Pradhu007 ")
message = input("Please enter a string to encrypt") 
key = input("Enter your shift pattern")

def findindex(encrypting: str, char):
    for s in range(len(encrypting)):
        if encrypting[s] == char:
            return s
encrypt = ''

# The function findindex finds the index of a specific character supplied as an parameter


for i in message:

    if i == "," or i == "-" or i == "." or i == " ":
        continue
        # Unecessary characters that we dont want to encrypt 



    else:
     

     position = findindex(alphabetandnumbers,i) # Finds the  the index  each  character which is the equalivent to the alphabet  and numbers array
     newposition = position + int(key) # This shifts  the index's value depending on the value of the key
     encrypt = encrypt + alphabetandnumbers[newposition] # Appends the encrypted message 


print("Your original message:{}".format(message))
print("The encrypted message:{}".format(encrypt))
# Displays the original and the encrypted message 




def decrypt(message,key):
    decrypted  = ""
    for char in message:

        if char == "," or char == "-" or char == "." or char == " ":
            continue
        else:

            position = findindex(alphabetandnumbers, char)
            newposition = position - int(key) # Instead of shifting characters to right, it shifts it to the left. In other words it subracts each character's index 
            # depending on the value of the key 
            
            decrypted = decrypted + alphabetandnumbers[newposition]
    return "Orginal message: {} \n decrypted message: {}".format(message,decrypted)
            # The decrypted message is shown here 







decryptmessage = input("What string would you like to decrypt?")
key = input("Enter the shift pattern")
print(decrypt(decryptmessage,key)) # Calling the function decrypt
