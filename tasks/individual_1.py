#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
В строке могут присутствовать скобки как круглые, так и квадратные скобки.
Каждой открывающей скобке соответствует закрывающая того же типа
(круглой – круглая,квадратной- квадратная). Напишите рекурсивную функцию,
проверяющую правильность расстановки скобок в этом случае.
"""


def f(q):
    q = ''.join(i for i in q if not i.isalpha())   # Удаляем буквы
    brackets = ['()', '[]']  # Список со скобочками
    if not q:  # Проверка на пустую строку
        return True
    for z in brackets:  # Проверка скобочек
        q = q.replace(z, '')  # Убираем скобочку
    if q and all([z not in q for z in brackets]):  # Если не правильно
        return False
    return f(q)  # Рекурсия


if __name__ == '__main__':
    if f(input('Введите строку:')):  # Ввод строки и запуск функции
        print('Скобочки расставлены правильно')
    else:
        print('Скобочки расставлены не правильно')