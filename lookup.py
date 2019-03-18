import subprocess
import re
import webbrowser


def get_ping_for_world(world_num):
    world = str(world_num)
    host = f'oldschool{world}.runescape.com'

    ping = subprocess.Popen(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = ping.communicate()

    match = re.search(r'Average = (\d+)ms', out.decode('utf-8'))

    ping = 999999
    if match:
        ping = int(match.group(1))

    return ping


def ping_all():
    for i in range(1, 100):
        world = 300 + i
        ping = get_ping_for_world(i)
        print(f'World {world}: {ping}ms')

    for i in range(112, 226):
        world = 300 + i
        ping = get_ping_for_world(i)
        print(f'World {world}: {ping}ms')


def ping_specific(world_num):
    world = world_num - 300
    ping = get_ping_for_world(world)
    return ping


def search_wiki(search_term):
    base_url = "https://oldschool.runescape.wiki/?search="
    webbrowser.open(base_url + search_term)
