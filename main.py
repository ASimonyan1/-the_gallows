def the_gallows(word):
    Sowpods = word
    fails = 0
    spisok = set()
    a = len(word)
    while fails < 10:
        n = input("введите букву: ")
        if n in Sowpods:
            spisok.add(n)
            print("одна из букв отгадана!")
            print("отгаданные буквы:", spisok)
        else:
            fails += 1
            print("ошибок:", fails, "/10")
            print("неверно!!!")
        if a == len(spisok):
            print("ура победа!")
            print("загаданное слово: ", word)
            break


def main():
    the_gallows(input("загадайте слово: "))


if __name__ == "__main__":
    main()
