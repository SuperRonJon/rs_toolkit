import xp_calc as rs
import external

from farming.farming_profit import get_profit_per_herb
from osrs_net.hiscores import lookup


def xp(arguments):
    argument_assertion(1, arguments)
    exp = int(arguments[0])
    current_level = rs.get_level(exp)
    next_level = rs.get_next_level(exp)
    remaining = rs.get_remaining_xp(exp)
    print("Level {} with {:,} xp until {}".format(current_level, remaining, next_level))
    return remaining


def level(arguments):
    argument_assertion(1, arguments)
    level = int(arguments[0])
    level_xp = rs.get_experience(level)
    print("{:,} xp".format(level_xp))
    return level_xp


def add(arguments):
    argument_assertion(2, arguments)
    current_xp = int(arguments[0])
    add_xp = int(arguments[1])
    new_xp = current_xp + add_xp
    new_level = rs.get_level(new_xp)
    next_level = rs.get_next_level(new_xp)
    remaining = rs.get_remaining_xp(new_xp)
    print("Level {} with {:,} xp until {}".format(new_level, remaining, next_level))
    return new_xp


def sub(arguments):
    argument_assertion(2, arguments)
    target_level = int(arguments[0])
    current_xp = int(arguments[1])
    xp_remaining = rs.get_experience(target_level) - current_xp
    print("{:,} xp remaining until level {}".format(xp_remaining, target_level))
    return xp_remaining


def div(arguments):
    argument_assertion(2, arguments)
    result = float(arguments[0]) / float(arguments[1])
    print("Result: {}".format(result))
    return result


def search(arguments):
    assert len(arguments) > 0, 'Invalid search'
    search_term = arguments[0]
    for word in arguments[1:]:
        search_term += " " + word
    external.search_wiki(search_term)
    return None


def ping(arguments):
    argument_assertion(1, arguments)
    if arguments[0] == 'all':
        external.ping_all()
    else:
        world = int(arguments[0])
        ping = external.ping_specific(world)
        print(f'World {world}: {ping}ms')
    return None


def herbs(arguments):
    if len(arguments) == 0:
        herbs_list = ['ranarr', 'toadflax', 'irit', 'avantoe', 'kwuarm', 'snapdragon', 'cadantine', 'lantadyme',
                      'dwarf weed', 'torstol']
    else:
        herbs_list = arguments

    profits = get_profit_per_herb(herbs_list)
    for name, profit in profits.items():
        print('{}: {:,}'.format(name, profit))

    return None


def hiscores(arguments):
    player_name = " ".join(arguments[:-1])

    skill = arguments[len(arguments) - 1]
    player = lookup(player_name)
    xp = player.skills[skill].experience
    print('{:,} experience'.format(xp))
    return xp


def help(arguments):
    print("COMMANDS\n=====================")
    print("level [level]-\t\t\t\tReturns the experience points required for [level]")
    print("xp [xp]-\t\t\t\tReturns the level at [xp] experience points")
    print("add [current_xp] [additional_xp]-\tReturns the level at [current_xp] + [additional_xp]")
    print("sub [target_level] [current_xp]-\tReturns the experience difference between [current_xp] and [target_level]")
    print("search [query]-\t\t\t\tOpens a wiki search of [query]")
    return None


def argument_assertion(num_args, arguments):
    assert len(arguments) == num_args, 'Incorrect number of arguments, should be ' + num_args
