import random
import string

def password_generator(length=12):
 characters = string.ascii_letters + string.digits + string.punctuation
 password = ''.join(random.choice(characters) for _ in range(length))
 print(f"Your generated password is: {password}")
 
 # Example usage
password_generator()