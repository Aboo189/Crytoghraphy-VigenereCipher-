
english_abc_lower="abcdefghijklmnopqrstuvwxyz"
english_abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Vigenere (plain_text, key):
  cipher_text=""
  k = len(key)
  if (len(plain_text)!=len(key)):
    i=0
    while (len(key)<len(plain_text)):
       if (i==k):
        i=0
       key+=key[i]
       i+=1
    print("generated key =", key)
  for i in range(0, len(plain_text)):
    if plain_text[i].islower():
            index_p = english_abc_lower.find(plain_text[i])
            index_k = english_abc_lower.find(key[i])
            new_index_e = (index_p + index_k) % 26
            cipher_text += english_abc_lower[new_index_e]
    elif plain_text[i].isupper():
            index_p = english_abc_upper.find(plain_text[i])
            index_k = english_abc_upper.find(key[i])
            new_index_e = (index_p + index_k) % 26
            cipher_text += english_abc_upper[new_index_e]
    else:
            cipher_text += plain_text[i]
  return cipher_text
text = input("Enter the text: ")
key = input("Enter the key: ")
print(Vigenere(text, key))
