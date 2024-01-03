import random 
import string 
characters=string.ascii_letters + string.digits  
s=int(input("Enter the Lenght of password: "))
password= ''.join(random.choice(characters) for n in range(s)) 
print("Generated Password:",password)