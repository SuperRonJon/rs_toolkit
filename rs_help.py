import math
import sys
import webbrowser


def get_experience(level):
    current = 0
    for i in range(1, level):
        value = math.floor(i + 300 * 2 ** (i/7))
        current += value
    return math.floor(current/4)


def get_level(experience):
    experience_table = [get_experience(i) for i in range(1, 100)]
    for index, value in reversed(list(enumerate(experience_table))):
        if experience >= value:
            return (index + 1, index + 2, experience_table[index + 1] - experience)


def add(current, to_add):
    return get_level(current + to_add)


def search_wiki(search_term):
    base_url = "https://oldschool.runescape.wiki/?search="
    webbrowser.open(base_url + search_term)


def execute_action(arguments):
    action = arguments[0]

    if action == 'xp':
        assert len(arguments) == 2, 'incorrect number of arguments, should be 2'
        value = int(arguments[1])
        current_level, next_level, remaining = get_level(value)
        print("Level {} with {:,} xp until {}".format(current_level, remaining, next_level))
    elif action == 'level':
        assert len(arguments) == 2, 'incorrect number of arguments, should be 2'
        value = int(arguments[1])
        print("{:,} xp".format(get_experience(value)))
    elif action == 'add':
        assert len(arguments) == 3, 'incorrect number of arguments, should be 3'
        current = int(arguments[1])
        add_xp = int(arguments[2])
        new_level, next_level, remaining = add(current, add_xp)
        print("Level {} with {:,} xp until {}".format(new_level, remaining, next_level))
    elif action == 'sub':
        assert len(arguments) == 3, 'incorrect number of arguments, should be 3'
        target_level = int(arguments[1])
        current_xp = int(arguments[2])
        xp_remaining = get_experience(target_level) - current_xp
        print("{:,} xp remaining until level {}".format(xp_remaining, target_level))
    elif action == 'search':
        search_term = arguments[1]
        for word in arguments[2:]:
            to_add = " " + word
            search_term += to_add
        search_wiki(search_term)
    elif action == 'help':
        display_help()
    else:
        print(str(action) + " is not a valid argument")


def display_help():
    print("COMMANDS\n=====================")
    print("level [level]-\t\t\t\tReturns the experience points required for [level]")
    print("xp [xp]-\t\t\t\tReturns the level at [xp] experience points")
    print("add [current_xp] [additional_xp]-\tReturns the level at [current_xp] + [additional_xp]")
    print("sub [target_level] [current_xp]-\tReturns the experience difference between [current_xp] and [target_level]")
    print("search [query]-\t\t\t\tOpens a wiki search of [query]")


print("Welcome to RS Help\ntype 'exit' to quit, 'help' for a list of commands")

args = ""
while args != "exit":
    args = input()
    if args != "exit":
        args = args.split()
        execute_action(args)
