def check_prime(x):
    prime_number = [2, 3]
    num = 5
    while len(prime_number) <= 1000:
        flag = True
        for i in prime_number:
            if num % i == 0:
                flag = False
                num+=1
                break

        if flag==True and num not in prime_number:
            prime_number.append(num)
            num+=1
    if x in prime_number:
        return True

def twin():
    for i in range(1000):
        if check_prime(i):
            if check_prime(i+2):
                print(f'twin prime is {i} {i+2}')

twin()
