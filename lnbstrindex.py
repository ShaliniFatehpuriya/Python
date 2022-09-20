def str_display():
    a = input('enter a string ')

    if len(a)>7 :
        print(a[::2])
    else:
        print(a[1::2])
str_display()
