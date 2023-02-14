# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

from random import randint


def get_list():
    return [randint(-10, 10) for x in range(randint(7, 10))]


def get_list_of_indexes(given_list):
    print(given_list)
    min_value = int(input('Set min value: '))
    max_value = int(input('Set max value: '))
    return [i for i in range(len(given_list)) if given_list[i] > min_value and given_list[i] < max_value]


print(get_list_of_indexes(get_list()))
