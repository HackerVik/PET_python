import random


def string_generator():
    charset = ""
    for i in range(33, 95):
        charset += (chr(i))
    for i in range(96, 127):
        charset += (chr(i))
    return charset


def password_generator(s):

    try:
        password_length = int(input('Enter the lenght of the password(6-128): '))
        password_number = int(input('Enter the number of the ganaerated passwords(1-1000): '))

    except ValueError:
        print('Only integers in the specified range recommended!')

    # with open('password.txt', 'a') as out:
    #     for i in range(0, passnumber):
    #        out.write(f'{"".join(random.sample(s, passlen))}'+'\n')

    try:
        for i in range(0, password_number):
            print(f'{"".join(random.sample(s, password_length))}')
    except NameError:
        print('Exiting program...')


def main():
    charset = string_generator()
    password_generator(charset)


if __name__ == '__main__':
    main()
