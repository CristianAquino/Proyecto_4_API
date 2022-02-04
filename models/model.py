#necesario para hacer consultas a la base de datos
from sqlalchemy import Table,Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, Integer, String
from config.db import meta

image = Table('image',meta,Column(
    'image_id',Integer,primary_key=True),
    Column('name_file',String(20)),
    Column('name_extension',String(20)),
    Column('fecha',Date)
)

name_file = Table('name_file',meta,Column(
    'name_id',Integer,primary_key=True),
    Column('name_file',String(20))
)
