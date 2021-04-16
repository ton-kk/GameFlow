def pre_event():
    print("<< this is opening event section. >>")
    print("you select action fot 10 turns.")
    print("character grows according to the selection result.")
    print("----------------")


def player_init():
    return {"name": "JohnDoe", "health": 100, "will": 3, "attension": 8,
            "talking": 12, "strength": 7, "luck": 4}


def search_command(status):
    print("you searched around.")
    print(" --- health decrease 20 points.")
    status["health"] = status["health"] - 20

    # random event


def break_command(status):
    print("i have a break. sometimes need a break everyone.")
    print(" --- health increase 40 points.")
    status["health"] = min(status["health"] + 40, 100)


def setting(status):
    print("show your status.")
    print(status)


def main():
    print("<< this is game flow demo. >>")
    print("----------------")
    pre_event()

    # player character initialize
    player = player_init()

    # main loop
    menu_dict = {1: "search", 2: "break", 3: "setting"}
    limit = 10
    while True:
        while True:
            print("last " + str(limit) + " turn. select your action.")
            print(player)
            menu_num = input("1. search  2. break  3.setting ... ")
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
            search_command(player)
        elif menu_num == 2:
            break_command(player)
        else:
            setting(player)
        print("----------------")

        # check limit
        if limit != 0:
            limit = limit - 1
        else:
            break

    print("this is game end.")


if __name__ == '__main__':
    main()
