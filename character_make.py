# character skill seeds.
# player or main character or sub or another
# 0 player 1 main 2 sub 3 another
import math
import random

seeds = []


# status
# identity: name age sex shape
# physical: strength agility endurance dexterity intelligence luck
# features: sight hearing insight concentration immunity
# points: health hunger thirst fatigue
# skills: <<may be boolean dictionary>>

# player-type
# power wise speed seek special
# 0 power 1 wise 2 speed 3 seek  special

class character:
    profile = {}


    def __init__(self, name, priority, ptype):
        # generate identity
        self.profile["name"] = name
        self.profile["age"] = int(random.uniform(10, 100))
        self.profile["sex"] = round(random.random())
        self.profile["shape"] = int(random.uniform(0, 10))
        # generate physical
        for key in ["strength", "agility", "endurance", "dexterity", "intelligence", "luck"]:
            self.profile[key] = int(random.uniform(1, 20))
        # generate features
        for key in ["sight", "hearing", "insight", "concentration", "immunity"]:
            self.profile[key] = int(random.uniform(1, 10))
        # generate points
        for key in ["health", "hunger", "thirst", "fatigue"]:
            self.profile[key] = 100
        # generate skills
        print("charcter created!")


def main():
    player = character("a player", 0, 4)
    print(player.profile)
    pass


if __name__ == '__main__':
    main()
