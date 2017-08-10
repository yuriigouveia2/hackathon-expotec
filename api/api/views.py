from api import app
from flask import jsonify, abort, request, make_response
from api import mongo, auth
from flask_pymongo import ObjectId
import bson

@app.route('/api/v1/usuarios', methods = ["GET"])
def get_all_users():
  users = mongo.db.users
  output = []
  for user in users.find():
    output.append({
      "id":str(user['_id']),
      "nome": user['nome'],
      "data-nascimento": user['data-nascimento'],
      "tipo-sanguineo": user['tipo-sanguineo'],
      "alergico": user['alergico'],
      "doencas-conhecidas": user['doencas-conhecidas'],
      "endereco": user['endereco'],
      "CPF": user['CPF'],
      "estado-civil": user['estado-civil'],
      "sexo": user['sexo']
      })
  return jsonify({"result":output}), 200

@app.route('/api/v1/usuarios/<string:user_id>', methods = ["GET"])
def get_user(user_id):
  users = mongo.db.users
  try:
    _id = ObjectId(user_id)
    result = users.find_one({"_id":_id})
    output = {
      "id":str(result['_id']),
      "nome": result['nome'],
      "data-nascimento": result['data-nascimento'],
      "tipo-sanguineo": result['tipo-sanguineo'],
      "alergico": result['alergico'],
      "doencas-conhecidas": result['doencas-conhecidas'],
      "endereco": result['endereco'],
      "CPF": result['CPF'],
      "estado-civil": result['estado-civil'],
      "sexo": result['sexo']
    }
    return jsonify({"result": output}), 200
  except bson.errors.InvalidId:
    return jsonify({"sucess": False}), 404
  except TypeError:
    return jsonify({"sucess":False}), 404

@app.route('/api/v1/usuarios/<string:user_id>', methods = ["DELETE"])
def remove_user(user_id):
  try:
    _id = ObjectId(user_id)
    if mongo.db.users.find_one({"_id":_id}) == None:
      return jsonify({"result": False}), 404

    result = mongo.db.users.delete_many({"_id":_id})
    return jsonify({"success": True}), 202
  except bson.errors.InvalidId:
    return jsonify({"sucess":False}), 404
  except TypeError:
    return jsonify({"sucess":False}), 404



@app.route('/api/v1/usuarios', methods = ["POST"])
def set_user():
  if not request.json:
    abort(400)
  users = mongo.db.users
  nome = request.json["nome"]
  data_nascimento = request.json["data-nascimento"]
  tipo_sanguineo = request.json["tipo-sanguineo"]
  alergico = request.json["alergico"]
  doencas_conhecidas = request.json["doencas-conhecidas"]
  endereco = request.json["endereco"]
  cpf = request.json["CPF"]
  estado_civil = request.json["estado-civil"]
  sexo = request.json["sexo"]

  post = {
    "nome":nome,
    "data-nascimento":data_nascimento,
    "tipo-sanguineo":tipo_sanguineo,
    "alergico":alergico,
    "doencas-conhecidas": doencas_conhecidas,
    "endereco":endereco,
    "CPF":cpf,
    "estado-civil":estado_civil,
    "sexo":sexo
    }

  users.insert_one(post)
  return jsonify({"sucess":True}), 201


@app.route('/api/v1/unidades', methods = ["GET"])
def get_units():
  units = mongo.db.units
  output = []

  for unit in units.find():
    output.append({
      "id": str(unit['_id']),
      "nome": unit['nome'],
      "endereco": unit['endereco'],
      "lat": unit['lat'],
      "long": unit['long'],
      "especialidades": unit['especialidades'],
      "avaliacoes": unit['avaliacoes'],
      "lotacao": unit['lotacao']
    })

  return jsonify({"result": output}), 200

@app.route('/api/v1/unidades/<string:unit_id>', methods = ["GET"])
def get_unit(unit_id):
  units = mongo.db.units
  try:
    _id = ObjectId(unit_id)
    result = units.find_one(({"_id":_id}))
    output = {
      "id": str(result['_id']),
      "nome": result['nome'],
      "endereco": result['endereco'],
      "lat": result['lat'],
      "long": result['long'],
      "especialidades": result['especialidades'],
      "avaliacoes": result['avaliacoes'],
      "lotacao": result['lotacao']
    }

    return jsonify({"result":output}), 200

  except bson.errors.InvalidId:
    return jsonify({"sucess": False}), 404
  except TypeError:
    return jsonify({"sucess":False}), 404
  
@app.route('/api/v1/unidades/<string:unit_id>', methods = ["DELETE"])
def remove_unit(unit_id):
  try:
    _id = ObjectId(unit_id)
    if mongo.db.units.find_one({"_id": _id}):
      return jsonify({"sucess": False}), 404
    result = mongo.db.units.delete_many({"_id":_id})
    return jsonify({"sucess": True}), 202
  except bson.errors.InvalidId:
    return jsonify({"sucess":False}), 404
  except TypeError:
    return jsonify({"sucess":False}), 404

@app.route('/api/v1/unidades', methods = ["POST"])
def set_unit():
  if not request.json:
    abort(400)
  
  units = mongo.db.units
  nome = request.json['nome']
  endereco = request.json['endereco']
  lat = request.json['lat']
  _long = request.json['long']
  especialidades = request.json['especialidades']
  avaliacoes = request.json['avaliacoes']
  lotacao = request.json['lotacao']

  post = {
    "nome": nome,
    "endereco": endereco,
    "lat": lat,
    "long": _long,
    "especialidades": especialidades,
    "avaliacoes": avaliacoes,
    "lotacao": lotacao
  }

  units.insert_one(post)
  return jsonify({"sucess": True}), 201

@app.route('/api/v1/unidades/<string:unit_id>/add', methods = ["PUT"])
def put_add_lot(unit_id):
  units = mongo.db.units
  try:
    _id = ObjectId(unit_id)
    result = units.find_one({"_id":_id})
    print(result['lotacao'])
    result['lotacao'] = int(result['lotacao'] + 1)
    units.save(result)
    output = {
      "_id": str(_id),
      "nome": result["nome"],
      "endereco": result["endereco"],
      "lat": result["lat"],
      "long": result["long"],
      "especialidades": result["especialidades"],
      "avaliacoes": result["avaliacoes"],
      "lotacao": result["lotacao"]
    }
    return jsonify({"result":output}), 200
  except bson.errors.InvalidId:
    return jsonify({"sucess":False}), 404
  except TypeError:
    return jsonify({"sucess":False}), 404

@app.route('/api/v1/unidades/<string:unit_id>/sub', methods = ["PUT"])
def put_sub_lot(unit_id):
  units = mongo.db.units
  try:
    _id = ObjectId(unit_id)
    result = units.find_one({"_id":_id})
    print(result['lotacao'])
    result['lotacao'] = int(result['lotacao'] - 1)
    units.save(result)
    output = {
      "_id": str(_id),
      "nome": result["nome"],
      "endereco": result["endereco"],
      "lat": result["lat"],
      "long": result["long"],
      "especialidades": result["especialidades"],
      "avaliacoes": result["avaliacoes"],
      "lotacao": result["lotacao"]
    }
    return jsonify({"result":output}), 200
  except bson.errors.InvalidId:
    return jsonify({"sucess":False}), 404
  except TypeError:
    return jsonify({"sucess":False}), 404
