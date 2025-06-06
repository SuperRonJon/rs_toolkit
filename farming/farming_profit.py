from osrs_net.item import Item
from osrs_net.grandexchange import GrandExchange

from .herb import Herb


def create_herb(herb_name):
    herb_name = herb_name.lower()
    if herb_name == 'ranarr':
        herb_name = 'ranarr weed'
    elif herb_name == 'irit':
        herb_name = 'irit leaf'
    herb_id = GrandExchange.item_id_from_name(herb_name)
    if herb_id is None:
        raise ValueError('Could not find herb {}'.format(herb_name))
    if herb_name == 'ranarr weed' or herb_name == 'irit leaf':
        seed_name = herb_name.split(' ')[0] + ' seed'
    else:
        seed_name = herb_name + ' seed'
    seed_id = GrandExchange.item_id_from_name(seed_name)
    if seed_id is None:
        raise ValueError('Could not find seed {}'.format(herb_name + " seed"))

    herb_price = GrandExchange.latest_price_by_id(herb_id)
    seed_price = GrandExchange.latest_price_by_id(seed_id)

    return Herb(herb_name, herb_price['low'], seed_price['high'])


def get_herb_list(herb_names):
    herbs = list()
    for herb in herb_names:
        herbs.append(create_herb(herb))
    return herbs


def get_profit_per_herb(herb_names_list):
    herbs = get_herb_list(herb_names_list)
    profit_dict = dict()
    for herb in herbs:
        profit_dict[herb.name] = herb.get_profit()

    return profit_dict

