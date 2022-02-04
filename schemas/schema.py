#necesario para ingresar datos a la base de datos
from datetime import date
from pydantic import BaseModel
from typing import Optional

class IMAGE(BaseModel):
    image_id:Optional[int]
    name_file:str
    name_extension:str
    fecha:Optional[date]

class NAME_FILE(BaseModel):
    name_id:Optional[int]
    name_file:str