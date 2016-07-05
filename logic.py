def getCiphertext(keyE,plaintext):
    ciphertext=""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                num = ord(char)+key
                if num > 122:
                    num=num-26
                    ciphertext = ciphertext + chr(num)
                else:
                    ciphertext = ciphertext + chr(num)
            else:
                    num = ord(char)+key
                    if num > 90:
                        num=num-26
                        ciphertext = ciphertext + chr(num)
                    else:
                        ciphertext = ciphertext + chr(num)
        else:
            ciphertext = ciphertext + char
    return ciphertext

def getPlaintext(keyD,ciphertext):
    return "plaintextk  " + keyD + ciphertext
