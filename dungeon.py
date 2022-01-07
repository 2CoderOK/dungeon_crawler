from enum import Enum
from random import choice, randint


class RoomType(Enum):
    EMPTY = 0
    GOLD = 1
    HEALTH = 2
    MONSTER = 3
    TRAP = 4


def genRooms(r_num):
    return [choice(list(RoomType)) for r in range(0, r_num)]


def fight(health):
    monster_health = randint(2, 4)
    print(f"You got a monster {monster_health} here!!!")

    init_att = -1
    if randint(0, 1):
        print("You attack first!")
        init_att = 1

    while True:
        hero_roll = randint(1, 6) + init_att
        monster_roll = randint(1, 6)
        init_att = 0

        rt = f" hero roll {hero_roll}, monster roll {monster_roll}, hero health {health}, monster health {monster_health}"
        if hero_roll >= monster_roll:
            print(f"Nice !!! You got him once !!! {rt}")
            monster_health -= 1
        else:
            print(f"Ouch ... That was hard ... {rt}")
            health -= 1

        if monster_health < 1 or health < 1:
            break
    return health


health = 5
gold = 0
rooms = 0

print("<--- Hello Adventurer --->")

while health > 0:
    print("=" * 30)
    rooms += 1
    max_rooms = randint(2, 5)
    print(*range(1, max_rooms + 1), sep="\t")
    generated_rooms = genRooms(max_rooms)

    sr = 0
    while True:
        r = input("\nPlease select your room: ")
        if r.isdigit() and int(r) in range(1, max_rooms + 1):
            sr = int(r)
            break

    srt = generated_rooms[sr - 1]

    if srt == RoomType.EMPTY:
        print("This room is empty. Are you happy?")
    elif srt == RoomType.GOLD:
        g = randint(1, 20)
        print(f"You found {g} gold coins!")
        gold += g
    elif srt == RoomType.HEALTH:
        h = randint(1, 5)
        print(f"You found {h} health potions!")
        health += h
    elif srt == RoomType.MONSTER:
        health = fight(health)
    else:
        h = randint(0, 3)
        print(f"It's a trap. You get {h} hits!")
        health -= h

    print(f"STATS: health {health}, gold coins {gold}, rooms {rooms}")

print("=" * 30)
print("You are a hero! We will remember you forever! ... try again ;)")
print(f"You've survived {rooms} rooms and collected {gold} gold coins!")
