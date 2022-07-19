from flask import request
from flask_restx import Resource, Namespace

from DAO.models.director import DirectorSchema
from implemented import director_serv

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_serv.get_all()
        return DirectorSchema(many=True).dump(directors), 200

    def post(self):
        json_req = request.json
        ent = director_serv.create(json_req)
        return "", 201, {"location": f"/directors/{ent.id}"}


@director_ns.route('/<int:bid>')
class DirectorView(Resource):
    def get(self, bid):
        director = director_serv.get_one(bid)

    def put(self, bid):
        json_req = request.json
        json_req["id"] = bid
        director_serv.update(json_req)
        return "", 204

    def patch(self, bid):
        json_req = request.json
        json_req["id"] = bid
        director_serv.part_update(json_req)
        return "", 204

    def delete(self, bid):
        director_serv.delete(bid)
        return "", 204



