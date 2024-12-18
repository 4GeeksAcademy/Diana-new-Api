"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User , Planet,Character,Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_user():
    all_users = User.query.all()  
    result = [user.serialize() for user in all_users]  
    return jsonify(result), 200

    


@app.route('/people', methods=['GET'])
def get_all_people():
    all_people = Character.query.all()
    result = [people.serialize() for people in all_people]  
    return jsonify(result) ,200

@app.route('/planets', methods=['GET'])
def get_all_planets():
    all_planets = Planet.query.all()
    result = [user.serialize() for user in all_planets]  
    return jsonify(result) ,200


@app.route('/vehicle', methods=['GET'])
def get_vehicle():
    get_vehicle = Vehicle.query.all()
    result = [user.serialize() for user in get_vehicle]  
    return jsonify(result) ,200
    

@app.route('/planet/<int:id>', methods=['GET'])
def get_one_planet(id):
     one_planet = Planet.query.get(id)
     if one_planet is None: 
      return "PLANETA NO SE ENCUENTRA", 400
     result = one_planet.serialize()
     return jsonify(result),200

@app.route('/vehicle/<int:id>', methods=['GET'])
def get_one_vehicle(id):
     one_vehicle = Vehicle.query.get(id)
     if one_vehicle is None: 
      return "VEHICLE NO SE ENCUENTRA", 400
     result = one_vehicle.serialize()
     return jsonify(result),200

@app.route('/character/<int:id>', methods=['GET'])
def get_one_character(id):
    one_character = Character.query.get(id)
    if one_character is None: 
        return "CHARACTER NO ENCONTRADO", 400
    result = one_character.serialize() 
    return jsonify(result), 200




    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
