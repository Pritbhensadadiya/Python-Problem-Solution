import string 
import random

if __name__== "main_":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits

    plen = int(input("Enter pass length:"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    
    random.shuffle(s)
    
    print("".join(s[0:plen]))