def check(user):
    check_list = user.split()
    for i in check_list:
        if len(i) <= 4:
            check_list.remove(i)
    return check_list

user = input('Enter a string or paragraph')
print(check(user))
