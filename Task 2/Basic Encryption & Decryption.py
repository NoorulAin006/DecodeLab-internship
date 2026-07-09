# ==========================================
# Caesar Cipher - Encryption & Decryption
# DecodeLabs Cyber Security Project 2
# ==========================================

def encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
          
            encrypted += char

    return encrypted


def decrypt(text, shift):
    decrypted = ""

    for char in text:
        if char.isalpha():

            # Handle uppercase letters
            if char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            # Handle lowercase letters
            else:
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            decrypted += char

    return decrypted


print("=" * 50)
print("     Caesar Cipher Encryption & Decryption")
print("=" * 50)

message = input("Enter your message: ")
shift = int(input("Enter shift key (1-25): "))

encrypted_text = encrypt(message, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\n========== RESULT ==========")
print("Original Message :", message)
print("Encrypted Message:", encrypted_text)
print("Decrypted Message:", decrypted_text)
print("============================")