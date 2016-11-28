from random import randrange


def test():
    doors = [x for x in range(100)]
    correct_door = randrange(0, 100)
    chosen_door = randrange(0, 100)
    switch = True

    for x in range(100):
        if x == correct_door: continue
        if x == chosen_door: continue
        doors.remove(x)
    if chosen_door == correct_door:
        doors.append(chosen_door//2 + 5)
    chosen_door_index = doors.index(chosen_door)

    if switch:
        doors.remove(doors[chosen_door_index])
        final_door = doors[0]
    else:
        final_door = doors[chosen_door_index]

    if final_door == correct_door:
        return 1
    else:
        return 0

wins = 0
for debug in range(1000000):
    wins += test()
    print('Percent', debug/10000, '%')
print(wins/1000000)

input("paused")
