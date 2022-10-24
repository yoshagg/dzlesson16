from app import models
from flask import current_app as app, request, jsonify
from app import db


@app.route('/')
def foo():
    return 'ass we can'


@app.route('/users', methods=['GET', 'POST'])
def users_page():
    result = []
    if request.method == 'GET':
        for user in models.User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        user_data = request.json

        new_user = models.User(**user_data)

        db.session.add(new_user)
        db.session.commit()

        for user in models.User.query.all():
            result.append(user.to_dict())

    return jsonify(result), 200


@app.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def user_function(uid):
    if request.method == 'GET':
        user = models.User.query.all(uid)
        return jsonify(user.to_dict()), 200
    elif request.method == 'PUT':
        user_data = request.json
        user = models.User.query.get(uid)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        user = models.User.query.get(uid)
        return jsonify(user.to_dict()), 200

    elif request.method == 'DELETE':
        user = models.User.query.get(uid)
        db.session.delete(user)
        db.session.commit

        return 'Удаление успешно завершено', 204


@app.route('/offers', methods=['GET', 'POST'])
def offers_page():
    if request.method == 'GET':
        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())
            return jsonify(result), 200
    elif request.method == 'POST':
        offer_data = request.json

        new_offer = models.Offer(**offer_data)

        db.session.add(new_offer)
        db.session.commit()

        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())

        return jsonify(result), 200


@app.route('/offers/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def offer_function(uid):
    if request.method == 'GET':
        offer = models.Offer.query.all(uid)
        return jsonify(offer.to_dict()), 200
    elif request.method == 'PUT':
        offer_data = request.json
        offer = models.Offer.query.get(uid)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        db.session.add(offer)
        db.session.commit()

        return jsonify(offer.to_dict()), 200

    elif request.method == 'DELETE':
        offer = models.Offer.query.get(uid)
        db.session.delete(offer)
        db.session.commit

        return 'Удаление успешно выполнено', 204


@app.route('/orders', methods=['GET', 'POST'])
def orders_page():
    result = []
    if request.method == 'GET':
        for order in models.Order.query.all():
            result.append(order.to_dict())
            return jsonify(result), 200
    elif request.method == 'POST':
        order_data = request.json

        new_order = models.Order(**order_data)

        db.session.add(new_order)
        db.session.commit()

        for order in models.Order.query.all():
            result.append(order.to_dict())

        return jsonify(result), 200


@app.route('/orders/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def order_function(uid):
    if request.method == 'GET':
        order = models.Offer.query.all(uid)
        return jsonify(order.to_dict()), 200
    elif request.method == 'PUT':
        order_data = request.json
        order = models.Order.query.get(uid)
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.address = order_data['address']
        order.price = order_data['price']
        order.customer_id = order_data['customer_id']
        order.executor_id = order_data['executor_id']

        db.session.add(order)
        db.session.commit()

        order = models.Order.query.get(uid)
        return jsonify(order.to_dict()), 200

    elif request.method == 'DELETE':
        order = models.Order.query.get(uid)
        db.session.delete(order)
        db.session.commit

        return 'Удаление завершено успешно', 204
