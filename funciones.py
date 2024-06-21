import csv

lista_bus = [["O" for x in range(1,6)] for y in range(6)]
lista_bus [0][3] = "x"
lista_bus [1][2] = "x"
personas = []



def opc_1():
    print("Asientos del bus: ")
    for f in lista_bus:
        print(f)




def opc_2():
    print("Estos son sus asientos disponibles: ")
    for f in lista_bus:
        print(f)

       
    print("El valor de los asientos es de $50000:")
    asiento_escojido1 = int(input("Escoja un columna desea: "))
    asiento_escojido2 = int(input("Ingrese que fila desea:"))
    if lista_bus[asiento_escojido1-1][asiento_escojido2-1] == "x":
        print("El asiento escojido esta ocupado!")
    else:
        lista_bus[asiento_escojido1][asiento_escojido2] = "x"
        nombre = input("Ingrese su nombre:")
        while True:
            try:
                if nombre.isalpha():
                    break
            except:
                print("Escriba su nombre con letras alfabeticas!")
        edad = int(input("Ingrese su edad: "))
        numero_telefono = int(input("Ingrese su número de telefono: "))
      

    


    
    

        

            
       


        
 



