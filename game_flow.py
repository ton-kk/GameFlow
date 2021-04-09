


def pre_event():
    print("<< this is pre event section. >>")
    print("you select action fot 10 turns.")
    print("character grows according to the selection result.")
    print("----------------")



def main():
    print("<< this is game flow demo. >>")
    print("----------------")
    pre_event()

    limit = 10
    while True:
        while True:
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
            search_command()
        elif menu_num == 2:
            break_command()
        else:
            setting()

        # check limit
        if limit == 0:
            limit = limit -1
        else:
            break






if __name__ == '__main__':
    main()