import random


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

    # random event
    event_seed = random.randint(0, 99)

    if event_seed < 21:
        print("and find some scraps.")
        print(" --- will increase 1 points.")
        status["will"] = min(status["will"] + 1, 5)
    elif event_seed < 51:
        print("and find talking skill book.")
        print(" --- talking increase 1 points.")
        status["talking"] = min(status["talking"] + 1, 30)
    else:
        print("and find nothing...")

    # common event
    print(" --- health decrease 20 points.")
    status["health"] = status["health"] - 20


def break_command(status):
    print("i have a break. sometimes need a break everyone.")
    print(" --- health increase 40 points.")
    status["health"] = min(status["health"] + 40, 100)


def setting(status):
    print("show your status.")
    print(status)


def save(player):
    print("data saved.")


def main():
    print("<< this is game flow demo. >>")
    print("----------------")
    pre_event()

    # player character initialize
    player = player_init()
    print("player character has been created.")
    print("status is ...")
    print(player)
    print("----------------")

    # main loop
    menu_dict = {1: "search", 2: "break", 3: "setting", 4: "save & quit"}
    limit = 9
    while True:
        while True:
            print("last " + str(limit) + " turn. select your action.")

            menu_num = input("1. search  2. break  3.setting 4.save & quit ... ")
            try:
                menu_num = int(menu_num)
            except:
                print("\'!! input error !!\' please input 1, 2, 3 or 4.")
                print("----------------")
                continue
            if menu_num not in [1, 2, 3]:
                print("\'!! input error !!\' you input " + str(menu_num) + ". out of lange.")
                print("----------------")
            else:
                break

        print("you select [[ " + str(menu_num) + " ]] " + menu_dict[menu_num] + ".")
        print("----------------")
        if menu_num == 1:
            search_command(player)
        elif menu_num == 2:
            break_command(player)
        elif menu_num == 3:
            setting(player)
            limit = 0
        else:
            save(player)
        print("----------------")

        # check limit
        if limit != 0:
            limit = limit - 1
        else:
            break
    print("turns are over.")
    print("this is game end.")


if __name__ == '__main__':
    main()
