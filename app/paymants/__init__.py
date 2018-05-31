from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api

payments = Blueprint('payments', __name__)
api = Api(payments)


class GetListPayments(Resource):

    def get(self):
        pass


class GetPayment(Resource):

    def get(self, id):
        pass


api.add_resource(GetListPayments, '.json')
api.add_resource(GetPayment, '/<int:id>.json')
