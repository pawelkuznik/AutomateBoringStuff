def collatz(nb):
    if (nb % 2 == 0):
       nb = nb // 2
    elif (nb) % 2 == 1:
        nb = 3 * nb + 1
    print(nb)
    return nb


try:
    number = int(input('Enter a number: '))
    while number != 1:
        number = collatz(number)
except ValueError:
    print('You have to insert a INT value!')



