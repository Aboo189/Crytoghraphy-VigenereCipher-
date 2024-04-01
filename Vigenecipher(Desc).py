english_abc = "abcdefghijklmnopqrstuvwxyz"

def decryptVigenere(cipher_text, key):
    plain_text = ""
    k = len(key)
    # Extend the key to match the length of the cipher text, if necessary
    if (len(cipher_text) != len(key)):
        i = 0
        while (len(key) < len(cipher_text)):
            if (i == k):
                i = 0
            key += key[i]
            i += 1

    # Decryption process
    for i in range(0, len(cipher_text)):
        index_c = english_abc.find(cipher_text[i])
        index_k = english_abc.find(key[i])
        # Perform the decryption by reversing the encryption process
        new_index_d = (index_c - index_k) % 26
        plain_text += english_abc[new_index_d]

    return plain_text

cipher_text = input("Enter the cipher text: ")
key = input("Enter the key: ")
print("Decrypted text:", decryptVigenere(cipher_text, key))
