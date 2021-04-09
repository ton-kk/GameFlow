menu_dict = {1: "Game Start", 2: "settings", 3: "Quit"}


def settings():
    print("<< this is game setting section. >>")
    print("return game menu.")
    print("----------------")


def game_main():
    print("<< this is game main section. >>")
    print("return game menu.")
    print("----------------")


def main():
    while True:
        print("<< this is menu flow demo. >>")
        print("please input number ... ")

        while True:
            menu_num = input("1. game start  2. settings  3. quit ... ")
            try:
                menu_num = int(menu_num)
            except:
                print("please input 1, 2 or 3.")
                print("----------------")
                continue
            if menu_num not in [1, 2, 3]:
                print("you input " + str(menu_num) + ". please input 1,2 or 3.")
                print("----------------")
            else:
                break

        print("you select [[ " + str(menu_num) + " ]] " + menu_dict[menu_num] + ".")
        print("----------------")
        if menu_num == 1:
            game_main()
        elif menu_num == 2:
            settings()
        else:
            break
    print("you select game quit. bye.")


if __name__ == '__main__':
    main()
