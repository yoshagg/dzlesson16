import json
from app import db, models


def load_data(filename):
    json_data = ""
    with open(filename, 'r') as file:
        json_data = json.load(file)

    return json_data


def load_users(filename):
    users = load_data(filename)

    for user in users:
        new_user = models.User(**user)
        db.session.add(new_user)

    db.session.commit()

    return users


def load_offers(filename):
    offers = load_data(filename)

    for offer in offers:
        new_offer = models.Offer(**offer)
        db.session.add(new_offer)

    db.session.commit()

    return offers


def load_orders(filename):
    orders = load_data(filename)

    for order in orders:
        new_order = models.Order(**order)
        db.session.add(new_order)

    db.session.commit()

    return orders


load_users('data/users.json')
load_offers('data/offers.json')
load_orders('data/orders.json')
