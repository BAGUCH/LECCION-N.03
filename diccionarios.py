diccionario = {
"Leo": "Motos",
"Nacho": "Videojuegos",
"Allan" : "Gym",
"Cristian": "Deporte de Contacto",
"Carlos" : "Bici",
"Jose": "Fulbol",
"Ithamar" : "Comer"}

#print(diccionario["Cristian"])

diccionario["kevin"] = "leer"

#print(diccionario)

menu= {
    "hamburguesa":{
        "ingredientes": ["pan","tomate", "carne","lechuga" ],
        "precio": 1500
    }

}

print(menu["hamburguesa"]["precio"])

print(menu["hamburguesa"]["ingredientes"][2])

#print(menu["hamburguesa"]["precio"]["ingredientes"][2])
print(menu.keys())