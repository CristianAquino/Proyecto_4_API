from fastapi import FastAPI
from models.model import image,name_file
from schemas.schema import IMAGE, NAME_FILE
from config.db import conn
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
import os #para abrir archivos

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],#muy necesario
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

#########################################################
#carga de imagenes
@app.post('/saveimag')
def post_img(img:IMAGE,nf:NAME_FILE):
    dataPath = 'C:/Users/51927/Desktop/Nueva carpeta (6)'
    peopleList = os.listdir(dataPath)

    new_name = {'name_file':nf.name_file}
    new_name['name_file'] = peopleList
    conn.execute(name_file.insert().values(new_name))

    faceData = []
    #especificamos la ruta de las carpetas
    for nameDir in peopleList:
        personPath = dataPath+'/'+nameDir
        #leemos las imagenes de cada carpeta
        for fileName in os.listdir(personPath):
            faceData.append(fileName)
            today = date.today()
            new_img = {"name_file":img.name_file,"name_extension":img.name_extension,"fecha":img.fecha}
            new_img['name_file'] = peopleList
            new_img['name_extension'] = fileName
            new_img['fecha']=today
            conn.execute(image.insert().values(new_img))
    return 'guardado'

#guardar imagen en archivo seleccionado
@app.post('/images/{name_file}/{name_extension}')
def post_images_file(name_file:str,name_extension:str,img:IMAGE):
    today = date.today()
    new_img = {"name_file":img.name_file,"name_extension":img.name_extension,"fecha":img.fecha}
    new_img['name_file'] = name_file
    new_img['name_extension'] = name_extension
    new_img['fecha']=today
    conn.execute(image.insert.where(image.c.name_file == name_file).values(new_img))
    return 'guardado'

#actualizar nombre archivo
@app.put('/image/update/{up_name_file}')
def put_update(up_name_file:str,img:IMAGE,nf:NAME_FILE):
    conn.execute(image.update().values(name_file = img.name_file).where(image.c.name_file == up_name_file))
    conn.execute(name_file.update().values(name_file = nf.name_file).where(name_file.c.name_file == up_name_file))
    return 'actualizado'

#mostrar todas las imagenes
@app.get('/images')
def get_images():
    data = conn.execute(image.select()).fetchall()
    return data

#mostrar imagenes por archivo
@app.get('/images/{name_file}')
def get_images_file(name_file:str):
    data = conn.execute(image.select().where(image.c.name_file == name_file)).fetchall()
    if data == []:
        return 'no se encontraron resultados'
    else:
        return data

#mostrar todos los archivos
@app.get('/files')
def get_images():
    data = conn.execute(name_file.select()).fetchall()
    return data

#mostrar archivo buscado
@app.get('/files/{file}')
def get_file(file:str):
    data = conn.execute(name_file.select().where(name_file.c.name_file == file)).fetchall()
    if data == []:
        return 'no se encontraron resultados'
    else:
        return data

#eliminar todas las imagenes y archivo
@app.delete('/images/delete/{file}')
def delete_images(file:str):
    conn.execute(image.delete().where(image.c.name_file == file))
    conn.execute(name_file.delete().where(name_file.c.name_file == file))
    return 'borrado'

#eliminar imagen dentro de archivo
@app.delete('/images/delete/{image_number}')
def delete_images_file(image_number:str):
    conn.execute(image.delete().where(image.c.name_extension == image_number))
    return 'borrado'