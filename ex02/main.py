'''
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''

from random import randint as rnd

# кто идет первый
whoStarts = rnd(1, 2)
print(whoStarts)

startValue = 2021

while startValue > 28:
    print(f'startValue: {startValue}')
    if whoStarts == 1:
        botinput = int(rnd(1, 28))
        startValue = int(startValue-botinput)
        print(f'ход бота-рандомайзера: {botinput}')
        if startValue <= 29:
            print("*" * 10, "победа бота-рандомайзера", "*" * 10)
            break
    else:
        bot2input = int(startValue % 29)
        startValue = int(startValue-bot2input)
        print(f'ход бота-умника: {bot2input}')
        if startValue <= 29:
            print("*" * 10, "победа бота-умника", "*" * 10)
            break
    whoStarts += 1
    if whoStarts > 2:
        whoStarts = 1
