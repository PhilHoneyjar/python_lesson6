# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.


def get_sequence():
    sequence_length = int(input('Enter sequence length: '))
    first_element = int(input('Enter first element of sequence: '))
    difference = int(input('Enter difference: '))
    return [(first_element + i * difference) for i in range(sequence_length)]


print(get_sequence())
