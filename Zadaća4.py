import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def check(email):

    if(re.search(regex, email)):
        print("Validan Email")

    else:
        print("Nevalidan Email")
    
        

 
