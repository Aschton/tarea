
while True:
    print("Elija la opcion que usted requiera")
    print("""
    1-spamear palabra "Mensaje"
    2-suma de numeros
    3-resta de numeros
    4-Salir
    """)
    opcion=input("")
    if opcion == "1":
        repeticiones=0
        cantidad=int(input("Cuantas repeticiones de mensajes quiere "))
        for repeticiones in range(cantidad):
            print("Mensaje")
    if opcion == "2":
        print("ingrese los dos numeros")
        num1=int(input(""))
        num2=int(input(""))
        suma=num1+num2
        print("El resultado es: ",suma)
    if opcion == "3":
        print("ingrese los dos numeros")
        num1=int(input(""))
        num2=int(input(""))
        resta=num1-num2
        print("El resultado es: ",resta)
    if opcion =="4":
        print("Deteniendo el menu...")
        break