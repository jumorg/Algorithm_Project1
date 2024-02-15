# key_Generation.py

import random
import math

class KeyGeneration: 
    
    def __init__(self): 
        self.bit_length = 1024
        self.pseudoPrimeOne = self.generate_pseudo_prime(self.bit_length)
        self.pseudoPrimeTwo = self.generate_pseudo_prime(self.bit_length)
        self.phi = (self.pseudoPrimeOne - 1) * (self.pseudoPrimeTwo - 1)
        self.modulus = self.pseudoPrimeOne * self.pseudoPrimeTwo
        self.publicExponent = self.findE(self.phi)
        self.privateExponent = self.findPrivateExponent(self.publicExponent, self.phi)
    
    # Generate the pseudo prime and validate with fermat little test and millerTest 
    def generate_pseudo_prime(self, bit_length): 
        while True: 
            # Generate a random num 
            p = random.getrandbits(bit_length) 
            
            # Set highest and lowest bit to 1 to ensure its correct size 
            p |= (1 << bit_length - 1) | 1
            
            # Use the fermat little test and Miller-Rabin test to see if the number is prime 
            if self.FermatsTest(p): 
                return p
    
    # Test if is a prime using Fermats test to reduce the likehood of composite
    # Algo: Fermat's test
    def FermatsTest(self, n, k=30): 
        if n in (2, 3): 
            return True
        
        # If number is even or less than 2, it is not than prime
        if n <= 1 or n % 2 == 0: 
            return False
        
        # Perfome the fermat Test k times
        for _ in range(k): 
           
            a = random.randint(2, n - 2)
            
            if pow(a, n - 1, n) != 1:
                return False
        
        return True
    
    # Find an public exponent (e) relative prime to (p-1)(q-1)
    # Algo: Euclid's gcd
    def findE(self, phi): 
        e = random.randint(2, phi)
        
        while (math.gcd(e, phi) != 1): 
            e = random.randint(2, phi)
        
        return e
    
    # Compute the greatest common divisor of two numbers iteratively
    def extended_gcd(self, a, b):
        x, last_x, y, last_y = 0, 1, 1, 0
        while b != 0:
            q = a // b
            a, b = b, a % b
            x, last_x = last_x - q * x, x
            y, last_y = last_y - q * y, y
            
        return last_x, last_y, a
    
    # Finds the private expone 'd' for RSA encryption
    def findPrivateExponent(self, e, phi):
        x, _, gcd = self.extended_gcd(e, phi)
        if gcd != 1:
            raise Exception('e and phi are not coprime')
        else:
            # Ensure d is positive
            d = x % phi
            return d
        

if __name__ == "__main__": 
    keyGenerate = KeyGeneration() 
    
    print(f'One prime: {keyGenerate.pseudoPrimeOne}')
    print(f'Two prime: {keyGenerate.pseudoPrimeTwo}')
    
    print(f'\nPhi : {keyGenerate.phi}')
    print(f'Modulus: {keyGenerate.modulus}')

    print(f'\npublic Exponent: {keyGenerate.publicExponent}')
    print(f'Private Exponent: {keyGenerate.privateExponent}')
 
    