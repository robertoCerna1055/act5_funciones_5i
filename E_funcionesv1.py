print("Manejo de funciones V1")
print("")

def hola_mundo():
    print("Hello world!")

def Mensa(msg):
    print(msg)

def EscribeNC(nombre, apellido):
    print("Su nombre es: ",nombre)
    print("Su apellido es: ",apellido)
    print(f"Tu nombre competo es {nombre} {apellido}")

def suma2numeros(n1,n2):
    res = n1 + n2
    return f"La suma de sus {n1} + {n2} es: ",res
   
  
    

# Llamando a la funcion
hola_mundo()
Mensa("Hola everyone") # Llama a Mensa() con un parametro
Mensa("El profe me sorprendio enviando mensajes") # Llama a Mensa() con un parametro
EscribeNC("Roberto","Cerna")
print("Funciones que regresan valores")
print(suma2numeros(7, 3))
print(suma2numeros(15, 45))