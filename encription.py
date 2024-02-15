# encription.py
from key_Generation import KeyGeneration
from front_end import frontEnd
import random

keys_instance = KeyGeneration()
front_instance = frontEnd()
class encription:
    
#input message, public key(n,e) C = M^e mod n using fast modular exponentiation 


    def is_prime(self, n, k=5):
        """Check if a number is prime using Miller-Rabin primality test."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
    
        def check(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                return True
            for _ in range(s - 1):
                if x == n - 1:
                    return True
                x = pow(x, 2, n)
            return x == n - 1
    
        s = 0
        d = n - 1
        while d % 2 == 0:
            d //= 2
            s += 1
    
        for _ in range(k):
            a = random.randint(2, n - 1)
            if not check(a, s, d, n):
                return False
        return True
    
    
    def fme(self, base, exponent, modulus):
        """Compute (base^exponent) % modulus efficiently."""
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus
        return result
    
    def encrypt(self, message, public_key):
        """Encrypt a message using the public key."""
        base, modulus = public_key
        encrypted_message = [self.fme(ord(char), base, modulus) for char in message]
        return encrypted_message
    
    public_key = keys_instance.publicExponent()
    
    # Message to encrypt
    message = front_instance.message()
    
    # Encrypt the message
    encrypted_message = encrypt(message, public_key)
    
    # Print or use the encrypted message
    print("Encrypted message:", encrypted_message)
    
    def decrypt(self, message, private_key):
        """Decrypt a message using the Private Key."""
        base, modulus = private_key
        encrypted_message = [self.fme(ord(char), base, modulus) for char in message]
        return encrypted_message
    
    private_key = keys_instance.privateExponent()
    
    # Message to encrypt
    message = encrypted_message
    
    # Encrypt the message
    decrypted_message = decrypt(message, private_key)
    
    # Print or use the encrypted message
    print("Decrypted message:", decrypted_message)
