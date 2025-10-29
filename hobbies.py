from flask import Blueprint, request, jsonify
bp = Blueprint('hobbies', __name__, url_prefix='/hobbies')

@bp.route('', methods=['GET'])
def hobbies():
    return '<h1>Hobbies</h1>'

