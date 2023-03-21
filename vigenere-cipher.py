def vigenere_cipher(message, keyword):
    # Convert the message and keyword to uppercase
    message = message.upper()
    keyword = keyword.upper()
    
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""
    
    # Loop through each letter in the message
    for i in range(len(message)):
        # Get the current letter of the message and the corresponding letter of the keyword
        message_letter = message[i]
        keyword_letter = keyword[i % len(keyword)]
        
        # Convert the letters to numbers between 0 and 25
        message_num = ord(message_letter) - 65
        keyword_num = ord(keyword_letter) - 65
        
        # Apply the shift and convert back to a letter
        new_letter_num = (message_num + keyword_num) % 26
        new_letter = chr(new_letter_num + 65)
        
        # Add the encrypted letter to the encrypted message
        encrypted_message += new_letter
    
    return encrypted_message

if __name__ == '__main__':
    # Get the message and keyword from the user
    message = input("Enter the message to encrypt: ")
    keyword = input("Enter the keyword: ")
    
    # Encrypt the message using the Vigenère Cipher
    encrypted_message = vigenere_cipher(message, keyword)
    
    # Print the encrypted message
    print("Encrypted message:", encrypted_message)
