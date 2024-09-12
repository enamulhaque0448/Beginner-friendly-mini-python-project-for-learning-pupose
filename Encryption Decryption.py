alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    ctext = ''
    for i in plain_text:
        if i in alphabet:
            position = alphabet.index(i)
            newp = (position + shift_amount) % 26 
            ctext += alphabet[newp]
        else:
            ctext += i 
    print(f"Encrypted text: {ctext}")

def decrypt(plain_text, shift_amount):
    dtext = ''
    for i in plain_text:
        if i in alphabet:
            position = alphabet.index(i)
            newp = (position - shift_amount) % 26 
            dtext += alphabet[newp]
        else:
            dtext += i 
    print(f"Decrypted text: {dtext}")
while True:
    a = input("Type 'en' to encrypt or 'de' to decrypt: ").lower()
    text = input("Enter the text: ").lower()
    shift = int(input("Enter the shift value: "))
    if a == 'en':
        encrypt(text, shift)
    elif a == 'de':
        decrypt(text, shift)
    else:
        print("Invalid option. Please choose 'en' or 'de'.")
        
    continue_choice = input("Do you want to continue? Type 'yes' or 'no': ").lower()
    if continue_choice == 'no':
        print("Goodbye!")
        break
    elif continue_choice != 'yes':
        print("Invalid choice, exiting the program.")
        break
