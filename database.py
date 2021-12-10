from peewee import *
from modelos import *

db = SqliteDatabase('pokemones.db')

class Pokemones(Model):
    nombre = CharField(100)
    tipo = CharField()
    color = CharField()
    nivel = CharField()
    comentario = TextField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()

db.create_tables([Pokemones])

def guardarPokemones(obj:pokemones):
  per = Pokemones()
  per.nombre = obj.nombre
  per.tipo = obj.tipo
  per.color = obj.color
  per.nivel = obj.nivel
  per.comentario = obj.comentario
  per.save()

def cargar_pokemones():
  pokemoness = []
  for per in Pokemones.select().dicts():
    pokemoness.append(per)
  return pokemoness 

def actualizarPokemones(obj:pokemones):
  per = Pokemones.get(Pokemones.id == obj.id)
  per.nombre = obj.nombre
  per.tipo = obj.tipo
  per.color = obj.color
  per.nivel = obj.nivel
  per.comentario = obj.comentario
  per.save()

def eliminarPokemones(obj:pokemones):
    qry=Pokemones.delete().where (Pokemones.id == obj.id)
    qry.execute()