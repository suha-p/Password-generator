import random
import string
print("Hello!!Welcome password generator")
length=int(input("Enter the length of password:"))
all = string.ascii_letters + string.digits + string.punctuation
temp=random.sample(all,length)
password="".join(temp)
print(password)