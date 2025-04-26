from time import sleep


def main():
    for i in range(3600):
        if i >= 2:
            exit(44)
        print(i)
        sleep(1)


if __name__ == '__main__':
    main()