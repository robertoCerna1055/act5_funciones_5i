print("Funciones creadas por el usuario")
print("")

def Mi_Lista():
    amigos=["Lista1","Lista2","Lista3"]
    for a in amigos:
        print(a)

def Mi_Tupla():
    VariableTupla = ("Tupla1","Tupla2","Tupla3")
    for a in VariableTupla:
        print(a)

def Mi_Diccionario():
    VariableDiccionario = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964
    }
    
    print(VariableDiccionario)

    

def Mi_Conjunto():
    VariablesConjunto = {"Conjunto","Conjunto2","Conjunto3"}
    for b in VariablesConjunto:
        print(b)

# Llamada de funciones
print("Lista:")
Mi_Lista()
print("")
print("Conjunto:")
Mi_Conjunto()
print("")
print("Diccionario:")
Mi_Diccionario()
print("")
print("Tupla:")
Mi_Tupla()

