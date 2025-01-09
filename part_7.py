# ==========================
# 7.4
# Задача - 'До КОНЦА 1'
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» (без кавычек). При этом само слово «КОНЕЦ» не входит в последовательность, лишь символизируя её окончание.
# Напишите программу, которая выводит члены данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести члены данной последовательности.

# Решение
# word = input()
# while word != 'КОНЕЦ':
#     print(word)
#     word = input()

# Задача - 'До КОНЦА 2'
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек).
# При этом сами слова «КОНЕЦ» и «конец» не входят в последовательность, лишь символизируя её окончание.
# Напишите программу, которая выводит члены данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести члены данной последовательности.

# Решение
# word = input()
# while word != 'КОНЕЦ' and word != 'конец':
#     print(word)
#     word = input()

# Задача - 'Количество членов'
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек).
# Сами эти слова в последовательность не входят, лишь символизируя её окончание.
# Напишите программу, которая выводит общее количество членов данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести общее количество членов данной последовательности.

# Решение
# word = input()
# word_count = 0
# while word != 'стоп' and word != 'хватит' and word != 'достаточно':
#     word = input()
#     word_count += 1
# print(word_count)

# Задача - 'Пока делимся'
# На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке.
# Концом последовательности является любое число, не делящееся на 7 (само это число в последовательность не входит, лишь символизируя её конец).
# Напишите программу, которая выводит члены данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность чисел, каждое число на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести члены данной последовательности.

# Решение
# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())

# Задача - Сумма чисел
# На вход программе подается последовательность целых чисел, каждое число на отдельной строке.
# Признаком окончания последовательности является любое отрицательное число, при этом в саму последовательность оно не входит.
# Напишите программу, которая выводит сумму всех членов данной последовательности.
#
# Формат входных данных
# На вход программе подается последовательность чисел, каждое число на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести сумму членов данной последовательности.
#
# Примечание. Число 0 не является признаком окончания последовательности.

# Решение
# num = int(input())
# list_ = []
# while num > -1:
#     list_.append(num)
#     num = int(input())
# print(sum(list_))

# Задача - 'Количество пятёрок 5️'⃣
# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке.
# Концом последовательности является любое неположительное число либо число, большее 5. Напишите программу, которая выводит количество пятерок.
#
# Формат входных данных
# На вход программе подается последовательность чисел, каждое число на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести количество пятерок.
#
# Примечание. Не забываем, что неположительными числами являются все отрицательные числа и число 0. 😉

# Решение
# count_5 = 0
# num = int(input())
# while 1 <= num <= 5:
#     if num == 5:
#         count_5 += 1
#     num = int(input())
# print(count_5)



# Задача - 'Ведьмаку заплатите чеканной монетой'
# Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево.
# К тому же ведьмак не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1, 5, 10, 25.
#
# Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку.
#
# Формат входных данных
# На вход программе подается одно натуральное число - цена за услугу ведьмака.
#
# Формат выходных данных
# Программа должна вывести минимально возможное количество чеканных монет для оплаты.

# Решение
# Определение переменных
# price = int(input())  # Сумма, которую нужно собрать
# denominations = [25, 10, 5, 1]  # Номиналы монет
#
# # Инициализация массива dp
# dp = [float('inf')] * (price + 1)
# dp[0] = 0  # 0 монет для суммы 0
#
# # Динамическое программирование для нахождения минимального количества монет
# p = 1
# while p <= price:
#     coin_index = 0
#     while coin_index < len(denominations):
#         coin = denominations[coin_index]
#         if p - coin >= 0:  # Если можем использовать монету
#             dp[p] = min(dp[p], dp[p - coin] + 1)
#         coin_index += 1  # Переход к следующей монете
#     p += 1  # Переход к следующей сумме
#
# # Проверяем вывод результата
# print(dp[price])

#
# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)
#


# num = int(input())
# while num != 0:
#     num_last = num % 10
#     print(num_last)
#     num = num // 10


# num = int(input())
# num_new = []
# while num != 0:
#     num_last = num % 10
#     num_new.append(num_last)
#     num = num // 10
# for num in num_new:
#     print(num, end='')

# num = int(input())
# num_new = []
# while num != 0:
#     num_last = num % 10
#     num_new.append(num_last)
#     num = num // 10
# print(f' Максимальная цифра равна {max(num_new)}')
# print(f' Минимальная цифра равна {min(num_new)}')

# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')
#
#
# # Ввод числа
# n = int(input())
# n_str = str(n)  # Преобразуем число в строку
# first_digit = n_str[0]  # Запоминаем первую цифру
# index = 1  # Начинаем с индекса 1
#
# # Переменная для хранения результата
# all_same = True  # Предполагаем, что все цифры одинаковые
#
# # Цикл проверки с использованием while
# while index < len(n_str):
#     if n_str[index] != first_digit:  # Если цифра не совпадает с первой
#         all_same = False  # Мы нашли различие
#         break  # Прерываем цикл, так как нашли различие
#     index += 1  # Переходим к следующей цифре
#
# # Проверяем результат
# if all_same:
#     print("YES")  # Все цифры одинаковые
# else:
#     print("NO")   # Есть различные цифры

# 7.6
# num = int(input())
# for i in range(2, num+1):
#     if num % i == 0:
#         print(i)
#         break


# num = int(input())
# for i in range(1, num+1):
#     if 5<=i<=9 or 17<=i<=37 or 78<=i<=87:
#         continue
#     else:
#         print(i)