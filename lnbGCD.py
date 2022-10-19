def gcd(a,b):
    if a==b or b==0:
        return a
 

    if a>b:
        return gcd(a-b,b)
    else:
        return gcd(b-a,a)
print(gcd(3,15))
