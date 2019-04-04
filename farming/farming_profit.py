from osrs_net.item import Item
from osrs_net.grandexchange import GrandExchange

from .herb import Herb


def create_herb(herb_name):
    herb_name = herb_name.lower()
    if herb_name == 'ranarr':
        herb_name = 'ranarr weed'
    elif herb_name == 'irit':
        herb_name = 'irit leaf'
    herb_id = Item.get_ids(herb_name)
    if isinstance(herb_id, list):
        raise ValueError('Could not find herb {}'.format(herb_name))
    if herb_name == 'ranarr weed' or herb_name == 'irit leaf':
        seed_name = herb_name.split(' ')[0] + ' seed'
    else:
        seed_name = herb_name + ' seed'
    seed_id = Item.get_ids(seed_name)
    if isinstance(seed_id, list):
        raise ValueError('Could not find seed {}'.format(herb_name + " seed"))

    herb = GrandExchange.item(herb_id)
    seed = GrandExchange.item(seed_id)

    return Herb(herb_name, herb.price_data['price'], seed.price_data['price'])


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

