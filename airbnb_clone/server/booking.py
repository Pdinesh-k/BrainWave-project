from flask import Blueprint, request, jsonify, make_response
from models import db, Property, AddMyBooking, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.to_dict import to_dict

booking_bp = Blueprint('booking', __name__)

@booking_bp.route("/add/<int:property_id>", methods=["POST"])
@jwt_required()
def add_to_booking(property_id):
    current_user = get_jwt_identity()

    try:
        booking_item = AddMyBooking(hotel_id=int(property_id), user_id=current_user)
        db.session.add(booking_item)
        db.session.commit()
        return jsonify({'message': 'Property added to booking successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@booking_bp.route("/get", methods=["GET"])
@jwt_required()
def get_bookings():
    try:
        user_id = get_jwt_identity()
        booking_items = AddMyBooking.query.filter_by(user_id=user_id).all()
        if not booking_items:
            return jsonify({'message': 'No items in booking'}), 404

        properties = [Property.query.get(booking_item.hotel_id) for booking_item in booking_items]
        properties_dict = [to_dict(property) for property in properties]

        return jsonify(properties_dict), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@booking_bp.route("/remove/<int:property_id>", methods=["DELETE"])
@jwt_required()
def remove_from_booking(property_id):
    current_user = get_jwt_identity()

    try:
        booking_item = AddMyBooking.query.filter_by(hotel_id=property_id, user_id=current_user).first()
        if not booking_item:
            return jsonify({'message': 'Item not found in booking'}), 404

        db.session.delete(booking_item)
        db.session.commit()
        return jsonify({'message': 'Property removed from booking successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
