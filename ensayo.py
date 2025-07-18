from random import randint

def Busqueda_destino(destino):
    encontrado=False
    for clave in vuelos_chile:
        if destino in vuelos_chile[clave]:
            print("el vuelo con destino:", destino,"con origen de: ", vuelos_chile[clave][0], "con fecha de", vuelos_chile[clave][2], "con hora de salida ", vuelos_chile[clave][3], "por la puerta de salida: ", vuelos_chile[clave][4])
            encontrado=True
    if not encontrado:
        print("Lo sentimos no encontramos el destino ", destino)

def busqueda_origen(origen):
    encontrado=False
    for clave in vuelos_chile:
        if origen in vuelos_chile[clave]:
            print("el vuelo con destino:", origen,"con origen de: ", vuelos_chile[clave][1], "con fecha de", vuelos_chile[clave][2], "con hora de salida ", vuelos_chile[clave][3], "por la puerta de salida: ", vuelos_chile[clave][4], "con valor : ", info_vuelos[clave][0])
            encontrado=True
    if not encontrado:
        print("Lo sentimos no encontramos el destino ", destino)

def busqueda_valor(minimo,maximo):
    encontrado=False
    for clave in info_vuelos:
        if int(minimo)< info_vuelos[clave][0] and int(maximo)> info_vuelos[clave][0]:
            encontrado=True
            print("Los vuelos que cumplen con su rango de busqueda son: ",info_vuelos[clave][0], "con Origen: ", vuelos_chile[clave][0],"con stock de: ", info_vuelos[clave][1], "Con los asientos disponible", info_vuelos[clave][2])

    if not encontrado:
        print("No contamos con vuelos en el rango de valor que busca")

def comprar_pasaje():
    asiento=[]
    origen_compra=input("Ingresa el origen de salida: ")
    encontrado=False
    for clave in vuelos_chile:
        if origen_compra in vuelos_chile[clave]:
            print("el vuelo con destino:", origen_compra,"con origen de: ", vuelos_chile[clave][1], "con fecha de", vuelos_chile[clave][2], "con hora de salida ", vuelos_chile[clave][3], "por la puerta de salida: ", vuelos_chile[clave][4], "con valor : ", info_vuelos[clave][0])
            encontrado=True
            
            if info_vuelos[clave][1]>0:
                info_vuelos[clave][1]-=1
                asiento.append(info_vuelos[clave][2].pop(randint(0, len(info_vuelos[clave][2])-1)))
                nombre=input("Ingrese el nombre: ")
                rut=input("Ingrese el rut: ")
                ventas_realizadas[nombre]={}
                ventas_realizadas[nombre][rut]=asiento
                print("Se a a asignado el siguiente asiento:", asiento)




    if not encontrado:
        print("Lo sentimos no encontramos el destino ", destino)

def Stock_vuelos(stock):
    encontrado=False
    for clave in info_vuelos:
        if stock in vuelos_chile[clave]:
            encontrado=True
            print("el stock en el vuelo", stock, "cuenta con los siguiente asientos disponibles", info_vuelos[clave][2], "total: ", info_vuelos[clave][1] )
        
    if not encontrado:
        ("Lo sentimos no contamos con vuelos")

def carrito():
    print(ventas_realizadas)


vuelos_chile = {
    "SAPA": ["Santiago", "Punta Arenas", "2025-07-10", "08:30", "Puerta 12"],
    "ARCO": ["Arica", "Concepción", "2025-07-11", "14:45", "Puerta 3"],
    "COTO": ["Copiapó", "Tocopilla", "2025-07-12", "10:20", "Puerta 5"]
}

info_vuelos = {
    "SAPA": [75000, 5, ['3A', '3B', '3C', '3J', '3K']],
    "ARCO": [68000, 4, ['4A', '4B', '4C', '4D']],
    "COTO": [72000, 3, ['5A', '5B', '5C']]
}

ventas_realizadas ={}

while True:
    print("""
    --- AEROPUERTO SANTIAGO ---
    1. Buscar vuelos
    2. Comprar pasaje
    3. Ver stock
    4. Ver ventas realizadas
    5. Salir
          """)
    
    opcion=input("Ingrese una opcion: ")

    if opcion=="5":
        print("Gracias por visitarnos")

    if opcion=="1":
        
        while True:
            print("""
                  1. Buscar por destino
                  2. Buscar por Origen
                  3. Buscar por valor 
                  4. Salir """)
            
            filtro=input("Ingrese la opcion que prefiere: ")

            if filtro=="1":
                destino=input("Ingrese el destino: ")
                Busqueda_destino(destino)
            if filtro=="2":
                origen=input("Ingrese el origen de busqueda: ")
                busqueda_origen(origen)
            if filtro=="3":
                minimo=input("Ingrese el valor minimo a pagar: ")
                maximo=input("Ingrese el valor maximo a pagar: ")
                busqueda_valor(minimo,maximo)

    if opcion=="2":
        comprar_pasaje()

    if opcion=="3":
        stock=input("Ingrese el vuelo que desea ver el stock ")
        Stock_vuelos(stock)    

    if opcion=="4":
        carrito()

    print("Estoy media perdida")