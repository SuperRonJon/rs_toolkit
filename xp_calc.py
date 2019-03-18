import math


def get_experience(level):
    current = 0
    for i in range(1, level):
        value = math.floor(i + 300 * 2 ** (i / 7))
        current += value
    return math.floor(current / 4)


def get_level(experience):
    experience_table = [get_experience(i) for i in range(1, 100)]
    for index, value in reversed(list(enumerate(experience_table))):
        if experience >= value:
            return index + 1


def get_next_level(experience):
    experience_table = [get_experience(i) for i in range(1, 100)]
    for index, value in reversed(list(enumerate(experience_table))):
        if experience >= value:
            return index + 2


def get_remaining_xp(experience):
    experience_table = [get_experience(i) for i in range(1, 100)]
    for index, value in reversed(list(enumerate(experience_table))):
        if experience >= value:
            return experience_table[index + 1] - experience


def add(current, to_add):
    return get_level(current + to_add)


def sub(target_level, current_xp):
    return get_experience(target_level) - current_xp
