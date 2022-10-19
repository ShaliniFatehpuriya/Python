def check(user):
    new = user.lower()
    if 'cat' in new :
        if 'dog' in new:
            return True
        else: 
            return False
    else:
        return False        

user = input('Enter a string')
print(check(user))
