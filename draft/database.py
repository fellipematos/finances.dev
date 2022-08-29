from peewee import  SqliteDatabase, Model, CharField, DateTimeField, IntegerField, FloatField

#Banco de Dados
database = SqliteDatabase("database.db")

#Banco de Dados Modelo
class BaseModel (Model):
    class Meta:
        database = database

class Transaction(BaseModel):
    date = CharField()
    operation = IntegerField()
    description = CharField()
    value = FloatField()

#Cria Banco de Dados
Transaction.create_table()
