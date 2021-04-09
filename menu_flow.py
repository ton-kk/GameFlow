menu_dict = {1: "Game Start", 2: "settings", 3: "Quit"}


def main():
    print("please input number ... ")
    print("1. game start  2. settings  3. quit")

    while True:
        menu_num = input()
        try:
            menu_num = int(menu_num)
        except:
            print("please input 1, 2 or 3.")
            continue
        if menu_num not in [1, 2, 3]:
            print("you input " + str(menu_num) + ". please input 1,2 or 3.")
        else:
            break

    print("\r\nyou select " + str(menu_num) + ". " + menu_dict[menu_num] + ".\r\n")


if __name__ == '__main__':
    main()
