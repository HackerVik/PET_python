from Utils import password_generator, charset_generator


def main():
    charset = charset_generator()
    password_generator(charset)


if __name__ == '__main__':
    main()
