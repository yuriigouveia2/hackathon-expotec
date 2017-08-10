from api import app
from flask import jsonify, abort, request, make_response
from api import mongo, auth
from flask_pymongo import ObjectId
import bson

@app.route('/api/v1/usuarios', methods = ["GET"])
def get_all_units():
  units = mongo.db.units
  output = []
  for unit in units.find():
    output.append({
      "id":str(unit['_id']),
      "nome": unit['nome'],
      "data-nascimento": unit['data-nascimento'],
      "tipo-sanguineo": unit['tipo-sanguineo'],
      "alergico": unit['alergico'],
      "endereco": unit['endereco'],
      "CPF": unit['CPF'],
      "estado-civil": unit['estado-civil'],
      "sexo": unit['sexo']
      })
  return jsonify({"result":output}), 200

@app.route('/api/v1/usuarios/<string:user_id>', methods = ["GET"])
def get_unit(user_id):
  units = mongo.db.units
  try:
    _id = ObjectId(user_id)
    result = units.find_one({"_id":_id})
    output = {
      "id":str(result['_id']),
      "nome": result['nome'],
      "data-nascimento": result['data-nascimento'],
      "tipo-sanguineo": result['tipo-sanguineo'],
      "alergico": result['alergico'],
      "endereco": result['endereco'],
      "CPF": result['CPF'],
      "estado-civil": result['estado-civil'],
      "sexo": result['sexo']
    }
    return jsonify({"result": output}), 200
  except bson.errors.InvalidId:
    return jsonify({"result": False}), 404
  except TypeError:
    return jsonify({"result":False}), 404


"""
  --------------FIX----------------
  Mesmo que um registro seja deletado, aparentemente, o id continua válido. 
  Isso faz com que o sempre retorne "True", mesmo quando o tento deletar 
  o mesmo id mais de uma vez 
"""
@app.route('/api/v1/usuarios/<string:user_id>', methods = ["DELETE"])
def remove_unit(user_id):
  try:
    _id = ObjectId(user_id)
    result = mongo.db.units.delete_many({"_id":_id})
    return jsonify({"success": True}), 202
  except bson.errors.InvalidId:
    return jsonify({"sucess":False}), 404
  except TypeError:
    return jsonify({"sucess":False}), 404



@app.route('/api/v1/usuarios', methods = ["POST"])
def set_unit():
  if not request.json:
    abort(400)
  unit = mongo.db.units
  nome = request.json["nome"]
  data_nascimento = request.json["data-nascimento"]
  tipo_sanguineo = request.json["tipo-sanguineo"]
  alergico = request.json["alergico"]
  endereco = request.json["endereco"]
  cpf = request.json["CPF"]
  estado_civil = request.json["estado-civil"]
  sexo = request.json["sexo"]

  post = {
    "nome":nome,
    "data-nascimento":data_nascimento,
    "tipo-sanguineo":tipo_sanguineo,
    "alergico":alergico,
    "endereco":endereco,
    "CPF":cpf,
    "estado-civil":estado_civil,
    "sexo":sexo
    }

  unit.insert_one(post)
  return jsonify({"result":post}), 201
