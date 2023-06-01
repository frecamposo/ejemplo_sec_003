# crear aplicacion que administre pasajeros de un avion
from Pasajero import *
lista_pasajeros=[]
ciclo=True
while ciclo:
    print("Linea aerea 'Marcianeque' ")
    print("1) Agregar Pasajero")
    print("2) Listar Pasajeros")
    print("3) Salir")
    try:
        op=int(input("Seleccione (1-3):"))
        match op:
            case 1:
                print("Agregar Pasajero")
                pasajero= Pasajero()
                pasajero.rut=input("Ingrese un Rut:")
                pasajero.nombre=input("Ingrese Nombre:")
                try:
                    pasajero.edad=int(input("Ingrese Edad:"))
                    lista_pasajeros.append(pasajero)
                    print("Agrego Pasajero")
                except:
                    print("error al ingresar la edad")
            case 2:
                print("Listar Pasajeros")
                for item in lista_pasajeros:
                    print(f"Rut:{item.rut} \t Nombre:{item.nombre} \t Edad:{item.edad}")
            case 3:
                ciclo=False
            case _:
                print("opcion incorrecta")
    except BaseException as error:
        print(f"error: {error}")
