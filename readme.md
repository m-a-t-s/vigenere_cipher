In this implementation, the vigenere_cipher() function takes two parameters: message and keyword. The message parameter is the message to be encrypted, and the keyword parameter is the keyword used to generate the shifts.

The function initializes an empty string to store the encrypted message, and then loops through each letter in the input message. For each letter, the function gets the corresponding letter of the keyword, applies the shift, and adds the encrypted letter to the encrypted_message string.

Finally, the function returns the encrypted message.

To use this implementation, you can call the vigenere_cipher() function with a message and a keyword. The function will return the encrypted message, which you can then use as needed.