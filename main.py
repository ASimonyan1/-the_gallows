def the_gallows(word):
    Sowpods = word
    fails = 0
    spisok = set()
    a = set(word)
    while fails < 10:
        n = input("введите букву: ")
        if n in Sowpods and n not in spisok:
            spisok.add(n)
            print("одна из букв отгадана!")
            print("отгаданные буквы:", spisok)
        elif n in spisok:
            print("вы уже отгадали эту букву!")
            print("отгаданные буквы:", spisok)
        else:
            fails += 1
            print("ошибок:", fails, "/10")
            print("неверно!!!")
        if len(a) == len(spisok):
            print("ура победа!")
            print("загаданное слово: ", word)
            break


def main():
    the_gallows(input("загадайте слово: "))


if __name__ == "__main__":
    main()
