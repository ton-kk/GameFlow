# character skill seeds.
# player or main character or sub or another
# 0 player 1 main 2 sub 3 another  reverse
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
# test 0 physical 1 features

class character:
    profile = {}
    priority = 0
    ptype = {"physical": 0, "features": 0}

    def __init__(self, name, priority, ptype):
        self.priority = priority
        self.ptype[ptype] = 1
        # generate identity
        self.profile["name"] = name
        self.profile["age"] = int(random.uniform(10, 65))
        self.profile["sex"] = round(random.random())
        self.profile["shape"] = int(random.uniform(0, 10))
        # generate physical
        for key in ["strength", "agility", "endurance", "dexterity", "intelligence", "luck"]:
            self.profile[key] = min(20, int(random.uniform(1, 20)
                                            + self.priority + self.ptype["physical"]))
        # generate features
        for key in ["sight", "hearing", "insight", "concentration", "immunity"]:
            self.profile[key] = min(10, int(random.uniform(1, 10)
                                            + (self.priority / 2) + self.ptype["features"]))
        # generate points
        for key in ["health", "hunger", "thirst", "fatigue"]:
            self.profile[key] = 100
        # generate skills

    def param_update_value(self, key, value):
        self.profile[key] = self.profile[key] + value

    def param_updates_value(self, array):
        for key, value in array:
            self.param_update(key, value)


def main():
    player = character("a player", 3, "features")
    print(player.profile)
    non_player = character("b player", 2, "features")
    print(non_player.profile)
    mob = character("b player", 1, "physical")
    print(mob.profile)
    another = character("john doe", 0, "other")
    print(another.profile)

    pass


if __name__ == '__main__':
    main()
