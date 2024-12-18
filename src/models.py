from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }
     
class User(db.Model):
    __tablename__ = 'user'
   
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), unique=True ,nullable=False)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    fecha_suscripcion = db.Column(db.DateTime(timezone=True), nullable=False)

    def serialize(self):
     return {
        "id": self.id,
        "user_name": self.user_name,
        "first_name": self.first_name,
        "last name":self.last_name,
        "email": self.email,
        "password": self.password,
        "fecha_suscripcion": self.fecha_suscripcion
    }
      

class Planet(db.Model):
    __tablename__= 'planet'

    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(250),nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)

    def serialize(self):
       return {
           "id": self.id,
           "planet_name": self.planet_name,
           "diameter": self.diameter,
           "population":self.population,
           "climate": self.climate,
        
    }
    
  
class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250),nullable=False)
    height = db.Column(db.Integer,nullable=False)
    hair_color = db.Column(db.String(250),nullable=False)
    eye_color = db.Column(db.String(250),nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'character_name ': self.character_name,
            'height': self.height,
            'hair_color': self.hair_color,
            'eye_color': self.eye_color
        }
    
 

class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_name = db.Column(db.String(250),nullable=False)
    cost_in_credits = db.Column(db.String(250),nullable=False)
    model = db.Column(db.String(250),nullable=False)
    passengers = db.Column(db.String(250),nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'vehicle_name': self.vehicle_name,
            'model': self.model,
            'cost_in_credits':self.cost_in_credits,
            'passengers': self.passengers
        }
   


class Create_Planet(db.Model):
    __tablename__ = 'create_planet'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_create_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    planet = db.relationship('Planet')
    user = db.relationship('User')
    

class Create_Vehicle(db.Model):
    __tablename__ = 'create_vehicle'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_create_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    vehicle= db.relationship('Vehicle')
    user = db.relationship('User')
    
class Create_Character(db.Model):
    __tablename__ = 'create_character'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_create_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    character = db.relationship('Character')
    user = db.relationship('User')
    

class Favorito_Planet(db.Model):
    __tablename__ = 'favorito_planet'

    id = db.Column(db.Integer, primary_key=True)
    planet_favorito_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet = db.relationship('Planet')
    user = db.relationship('User')
    
    
class Favorito_Character(db.Model):
    __tablename__ = 'favorito_character'

    id = db.Column(db.Integer, primary_key=True)
    character_favorito_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character = db.relationship('Character')
    user = db.relationship('User')
    
class Favorito_Vehicle(db.Model):
    __tablename__ = 'favorito_vehicle'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_favorito_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle = db.relationship('Vehicle')
    user = db.relationship('User')
    

