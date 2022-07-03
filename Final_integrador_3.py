import json  
ruta="C:/Users/rodol/Desktop/python-course/CursoPython"
# heroes = {     {
#                 "nombre": "Flash",
#                 "identidadSecreta": "Bartholomew Henry 'Barry' Allen",
#                 "poderes": ["Inmensa velocidad","agilidad","Electrokinesis"]
#                },
               
#                {
#                 "nombre": "Batman",
#                 "identidadSecreta": "Bruce Wayne",
#                 "poderes": ["Super fuerza","super velocidad"]
#                },
#                {
#                 "nombre": "Super Man",
#                 "identidadSecreta": "Clark Joseph Kent",
#                 "poderes": ["Super fuerza","super velocidad","resistencia","agilidad","reflejos","durabilidad","sentidos y longevidad"]
#                }
#         }
heroes = {
"nombre": "Flash",
"identidadSecreta": "Bartholomew Henry 'Barry' Allen",
"poderes": [
"Inmensa velocidad",
"agilidad",
"Electrokinesis"]},{"nombre": "Batman",
"identidadSecreta": "Bruce Wayne",
"poderes": ["Super fuerza",
"super velocidad"]},{ "nombre": "Super Man",
"identidadSecreta": "Clark Joseph Kent",
"poderes": ["Super fuerza",
"super velocidad",
"resistencia",
"agilidad",
"reflejos",
"durabilidad",
"sentidos y longevidad"]
}

archivo_json= open( ruta + "/super_heroes.json","w")
json.dump(heroes,archivo_json,indent=4)
archivo_json.close()