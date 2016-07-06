def getCiphertext(keyE,plaintext):
    ciphertext=""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                num = ord(char)+int(keyE)
                if num > 122:
                    num=num-26
                    ciphertext = ciphertext + chr(num)
                else:
                    ciphertext = ciphertext + chr(num)
            else:
                num = ord(char)+int(keyE)
                if num > 90:
                    num=num-26
                    ciphertext = ciphertext + chr(num)
                else:
                    ciphertext = ciphertext + chr(num)
        else:
            ciphertext = ciphertext + char
    return ciphertext

def getPlaintext(keyD,ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                num = ord(char)-int(keyD)
                if num < 97:
                    num=num+26
                    plaintext = plaintext + chr(num)
                else:
                    plaintext = plaintext + chr(num)
            else:
                num = ord(char)-int(keyD)
                if num < 65:
                    num = num+26
                    plaintext = plaintext + chr(num)
                else:
                    plaintext = plaintext + chr(num)
        else:
            plaintext = plaintext + char
    return plaintext
