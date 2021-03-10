import sys as system
# Zadanie 1
# sport= ["piłka nożna", "siatkówka", "koszykówka"]
# print(sport)
# sport.reverse()
# print(sport)
# sportm= ("piłka ręczna", "kolarstwo", "żużel")
# sport.append(sportm)
# print(sport)

#Zadanie2
#slownik= {'np': 'na przykład', 'dr': 'doktor', 'mgr': 'magister', 'cdn.': 'ciąg dalszy nastąpi', 'itd.': 'i tak dalej'}

#Zadanie3
# gry= {'Moba': 'League of Legends', 'MMO RPG': 'Margonem', 'FPS': 'Counter-Strike', 'Strategia': 'Heroes of Might and Magic', 'RPG': 'Fable'}
# ile= len(gry)
# print(ile)

#Zadanie4
# zd= input("Podaj zdanie:")
# ile = 0
# for a in zd:
#  if a == "a":
#    ile += 1
# print(ile)

#Zadanie5
# system.stdout.write("Podaj liczby: ")
# a= system.stdin.readline()
# b= system.stdin.readline()
# c= system.stdin.readline()
# wynik= (int(a)**int(b))+int(c)
# system.stdout.write("Wynik: %d"%wynik)

#Zadanie6
# a = input("Podaj 1 liczbe: ")
# b = input("Podaj 2 liczbe: ")
# c = input("Podaj 3 liczbe: ")
# if a>b:
#    if a>c:
#        print(a)
#    else:
#        print(c)
# elif b>c:
#    print(b)
# else:
#    print(c)

#Zadanie7
# liczby = [2, 4, 9.91, 10, 25, 14.817, 8123]
# for pow in liczby:
#     print(pow ** 2)

#Zadanie8
# x = 0
# list = []
# while x < 10:
#     print("Podaj liczbę: ")
#     a = input()
#     lp = int(a)%2
#     if lp == 0:
#         list.append(a)
#     x += 1
# print(list)

#Zadanie9
# list = [1, 2, 3, 4, 5]
# for licz in list:
#     a = int(licz)%2
#     if a == 0:
#         print("E")
#     else:
#         print("EEEEEE")

#Zadanie10
# import math
# print("Podaj liczbę dodatnią: ")
# a = int(input())
# try:
#     a = (math.sqrt(a))
#     print(a)
# except:
#     print("Błąd liczba jest mniejsza od 0")