"""
Public Key Generator for EXAMPLE :
"""
import crypto.PublicKey.DSA
import crypto.PublicKey.RSA
import random

# DSA
task = crypto.PublicKey.DSA
print(task.DsaKey({ 'g' : random.randint(0, 9999) , 'q': random.randint(0, 9999), 'p' : random.randint(0, 9999), 'y' : random.randint(0, 9999)}).export_key())

# RSA
task2 = crypto.PublicKey.RSA
print(task2.generate(random.randint(1024, 9999)).export_key())

