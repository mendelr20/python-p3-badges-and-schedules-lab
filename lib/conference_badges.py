def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    list = []
    for name in names:
        list.append(f'Hello, my name is {name}.')
    return list

def assign_rooms(names):
    list = []
    num = 1
    for name in names:
        list.append(f'Hello, {name}! You\'ll be assigned to room {num}!')
        num += 1
    return list

def printer(names):
    for badge in batch_badge_creator(names):
         print(badge)
    
    for assignment in assign_rooms(names):
         print(assignment)

