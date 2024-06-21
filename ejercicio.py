import os , time 
from funciones import *






while True:
    print("Bienvenido a turbus")
    print("1. Mostrar asientos Disponibles")
    print("2. Comprar asiento")
    print("3. Mostrar ventas realizadas")
    print("4. Guardar o generar arhivo csv de ventas")
    print("5. Salir del progama")
    opc = int(input("Ingrese una opcion: "))

    while True:
        try:
            if opc in (1,2,3,4,5):
                break
            else:
                print("Elija la opción correcta:")
        except:
            print("Escriba números enteros!")
    os.system('cls') 
    if opc ==1:
        opc_1()
    if opc==2:
        opc_2()
    if opc==3:
        pass
    if opc==4:
        pass
    else:
        print()
    time.sleep(3)

