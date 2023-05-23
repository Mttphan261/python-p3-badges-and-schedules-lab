def badge_maker(name):
    return f'Hello, my name is {name}.'


def batch_badge_creator(names):
    badge_list = []
    for name in names:
        badge_list.append(f'Hello, my name is {name}.')
    return badge_list


def assign_rooms(names):
    room_assignments = []
    index = 0
    for name in names:
        index += 1
        room_assignments.append(
            f"Hello, {name}! You'll be assigned to room {index}!")
    return room_assignments


def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for room in assign_rooms(names):
        print(room)