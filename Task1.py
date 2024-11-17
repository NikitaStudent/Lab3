#Task1
import math
def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        n = int(input('Введите целое положительное число больше 1: '))
        if n <= 1:
            print('Вы ввели число меньше 2')
            return
        if prime_number(n):
            print('Число {} является простым'.format(n))
        else:
            print('Число {} не является простым'.format(n))
    except ValueError:
        print('Некорректный ввод, введите целое положительное число')

main()