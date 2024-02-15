# front_end.py
from key_Generation import KeyGeneration
from encription import encription

keys_instance = KeyGeneration()
encrypt_instance = encription()

pubk = keys_instance.publicExponent()
privk = keys_instance.privateExponent()
class frontEnd:   
    
    u_type = 0
    print("RSA keys have been generated.")
    
    #loop prompts user and uses algorithms
    while u_type != 3:
        #user selects user type
        print("Please select your user type:\n")
        print("\t1. A public user\n")
        print("\t2. The owner of the keys\n")
        print("\t3. Exit program\n")
        u_type = int(input("Enter your choice: "))
    
        #define choice
        choice = 0
    
        # public user prompts
        if u_type == 1:
            
            while choice != 3:
                print("As a public user, what would you like to do?")
                print("\t1. Send an encypted message\n")
                print("\t2. Authenticate a digital signature\n")
                print("\t3. Exit\n")
                choice = int(input("Enter your choice: "))
        
                if choice == 1:
                    message = input("Enter a message:")
                    
                    #  ENCRYPTION----------------------------------------------------------
                    def encrypt(self, message, n):
                        message_as_int = int.from_bytes(message.encode('utf-8'), 'big')
                        
                        n, e = pubk
                        encrypted_message = pow(message_as_int, e, n)
                        return encrypted_message
                    
                    print(message)
                    encrypted_message = encrypt_instance.encrypt(message, pubk)
                    print("encrypted: ", encrypted_message)
                    print("Message encrypted and sent.\n")
                    # --------------------------------------------------------------------
                    
                if choice == 2:
                    message_choice = 0
                    #CHECK SIGNATURES
                    print("The following messages are available: \n")
                    #DISPLAY MESSAGES
                    int(input("Enter your choice: "))
                    print("The signature is valid.\n")
            
            
            # owner prompts
            if u_type == 2:
                
                while choice != 5:
                    print("As the owner of the keys, what would you like to do?")
                    print("\t1. Decrypt a received message\n")
                    print("\t2. Digitally sign a message\n")
                    print("\t3. Show the keys\n")
                    print("\t4. Generating a new set of keys\n")
                    print("\t5. Exit\n")
                    choice = int(input("Enter your choice: "))
                    
                    if choice == 1:
                        #CHECK MESSAGES
                        print("The following messages are available:\n")
                        #DISPLAY MESSAGE LENGTHS
                        print("Enter your choice: ")
    
                        # DECRYPTION-----------------------------------------------
                        print(message)
                        decrypted_message = encrypt_instance.decrypt(message, privk)
                        print("encrypted: ", encrypted_message)
                        print("Message encrypted and sent.\n")
                        # ---------------------------------------------------------
                    if choice == 2:
                        #SIGN MESSAGE
                        input("Enter a message: ")
                        print("Message signed and sent.\n")
            
           
    print("Bye for now!\n")