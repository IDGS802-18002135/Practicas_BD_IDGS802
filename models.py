from flask_sqlalchemy import SQLAlchemy
import datetime


db=SQLAlchemy()




class Maestros(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    amaterno=db.Column(db.String(50))
    edad=db.Column(db.Integer)
    direccion=db.Column(db.String(50))
    email=db.Column(db.String(50))
    create_date=db.Column(db.DateTime,default=datetime.datetime.now)


class Pizza(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    telefono=db.Column(db.String(50))
    tamaño=db.Column(db.String(50))
    ingredientes=db.Column(db.String(50))
    numeroPizza=db.Column(db.Integer)
    subtotal=db.Column(db.Integer)
    create_date = db.Column(db.DateTime)

class Venta(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombreVenta=db.Column(db.String(50))
    direccionVenta=db.Column(db.String(50))
    telefonoVenta=db.Column(db.String(50))
    totalVenta=db.Column(db.Integer)
    create_dateVenta = db.Column(db.DateTime)



class PizzaOrden:
    def __init__(self,nombre, direccion,telefono,tamaño,ingredientes,numeroPizza,subtotal,fecha):
        
        self.nombre = nombre
        self.direccion = direccion
        self.telefono= telefono
        self.tamaño = tamaño
        self.ingredientes = ingredientes
        self.numeroPizza = numeroPizza
        self.subtotal = subtotal
        self.fecha=fecha
