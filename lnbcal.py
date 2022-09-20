def mult():
    a = int(input('enter first digit'))
    b = int(input('enter second digit'))
    print(a*b)
    if a*b >500:
        return a+b
    else:
        return 'Hello LNB code is running fine !!'

print(mult())
