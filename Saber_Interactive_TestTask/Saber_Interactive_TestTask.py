while True:
    try:
        print(eval(input("Введите выражение: ")))
    except BaseException:
        print("Неверный формат ввода! Попробуйте еще раз")
