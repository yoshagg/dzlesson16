import json
from . import models, db


def load_data(filename):
    json_data = []
    with open(filename) as file:
        json_data == json.load(file)

    return json_data


def load_users(filename):
    users = load_data(filename)

    for user in users:
        new_user = models.User(**user)
        db.session.add(new_user)

    db.session.commit()

    print(models.User.get(1).to_dict_user())


def load_offers(filename):
    offers = load_data(filename)

    for offer in offers:
        new_offer = models.Offer(**offer)
        db.session.add(new_offer)

    db.session.commit()

    print(models.Offer.get(1).to_dict_offer())


def load_orders(filename):
    orders = load_data(filename)

    for order in orders:
        new_order = models.Order(**order)
        db.session.add(new_order)

    db.session.commit()

    print(models.Order.get(1).to_dict_order())

load_users('users.json')
load_offers('offers.json')
load_orders('orders.json')
