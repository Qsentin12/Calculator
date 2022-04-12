while True:
    print("Добро пожаловать в Калькулятор")
    print("""
    Опирацыя для добавления +
    Опирацыя для отнимания -
    Опирацыя для умнажения *
    Опирацыя для разделения :
    """)

    wath = input("Введите опирацыю: ")
    num_1 = 0
    try:
        num_1 = int(input("Введите первое цисло: "))
    except ValueError:
        print("Вы ввели не число.")
    num_2 = 0
    try:
        num_2 = int(input("Введите первое цисло: "))
    except ValueError:
        print("Вы ввели не число.")
    num_3 = None

    if wath == "+":
        num_3 = num_2 + num_1

    elif wath == "-":
        num_3 = num_2 - num_1

    elif wath == "*":
        num_3 = num_2 * num_1

    elif wath == ":":
        num_3 = num_2 / num_1

    else:
        print("Неверная опирацыя.")

    print("Результат:", num_3)
