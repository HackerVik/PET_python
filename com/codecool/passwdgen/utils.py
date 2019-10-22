import random


def password_generator(charset):
    try:
        password_length = int(input('Enter the lenght of the ' +
                                    'password(8-64): '))
        password_number = int(input('Enter the number of the ' +
                                    'passwords(1-1000): '))

    except ValueError:
        print('Only integers in the specified range recommended!')

    try:
        print("")
        for i in range(0, password_number):
            print(f'{"".join(random.sample(charset, password_length))}')

    except NameError:
        print('Exiting program...')


def charset_generator():
    charset = ""
    for i in range(33, 95):
        charset += (chr(i))
    for i in range(96, 127):
        charset += (chr(i))
    return charset
