# Курсовая работа на тему сжатия данных алгоритмом LZW.

Для использования программ, необходимо в консоли перейти в каталог вашего проекта.

Сжатие данных осуществляется с помощью файла compression.py
В программе реализован алгоритм сжатия данных - LZW.
Для корректной работы программы, требуется ввести название файла и количество битов через командную строку.
Сжатие реализуется с помощью словаря: ключ - символ, значение - ASCII.
Сжатый файл будет иметь расширение ".bereg". Файл будет находиться в папке проекта.

Формат ввода данных в консоль для сжатия:
python compression.py *.txt number

Восстановление данных осуществляется с помощью файла recovery.py
В программе реализован алгоритм восстановления данных.
Для корректной работы программы, требуется ввести название файла и количество битов через командную строку.
Восстановление реализуется с помощью словаря: ключ - символ, значение - ASCII.
Восстановленный файл будет иметь преписку "_gg" и формат ".txt". Файл будет находиться в папке проекта.

Формат ввода данных в консоль для восстановления:
python recovery.py *.bereg number

History:
20.12.2021 - Первый коммит. Создание readme, gitignore.

Анекдот:
Сидит ворона на дереве. Смотрит - корова подходит к берёзе и начинает на неё лезть. Ворона пришла в шок. Говорит:
= Корова, ты чего на березу лезешь?
Корова ей отвечает:
= Яблоки кушать.
Ворона пришла ещё в больший шок.
= Дура, это же берёза.
Корова на неё посмотрела и говорит:
= Так я со своими.


Главный вопрос седьмого семестра: если акула и медведь будут драться на мелководье, то кто победит?
