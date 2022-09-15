import methods as mth
from productOnlyId import *

cantDeProductos: int = 0
print("Por favor ingrese la cantidad de productos a agregar")
while True:
    try:
        cantDeProductos = int(input())
        break
    except:
        print("Por favor solo valores numéricos")

listOfProdcts: list[ProductOnlyId] = list[cantDeProductos]()

for i in range(1, cantDeProductos+1):
    mth.CrearProducto(i, listOfProdcts)

flag: bool = True
medio: int = 0
usuario: str = ""
contrasenia: str = ""
autorizacion: bool = False
saldo: float = 0

print("Declare su saldo inicial: ")
saldo = mth.declararSaldo()

while flag:
    eleccion: int = mth.verMenu()
    match eleccion:
        case 1:
            mth.ConsultarProductos(listOfProdcts)
        case 2:
            while True:
                if not autorizacion:
                    print("Usted no cuenta con la autorización necesaria")
                    print("Por favor, identifiquese.")
                    print("Ingrese su usuario: ")
                    usuario = input()
                    print("Ingrese su contraseña: ")
                    contrasenia = input()
                    if mth.checkearAdmin(usuario, contrasenia):
                        autorizacion = mth.checkearAdmin(
                            usuario, contrasenia)
                        print("Credenciales validadas")
                        listOfProdcts = mth.ModificarProductos(
                            listOfProdcts)
                        break
                    else:
                        print("Usuario o Contraseña incorrectos")
                        break
                if autorizacion:
                    listOfProdcts = mth.ModificarProductos(listOfProdcts)

        case 3:
            while True:
                if not autorizacion:
                    print("Usted no cuenta con la autorización necesaria")
                    print("Por favor, identifiquese.")
                    print("Ingrese su usuario: ")
                    usuario = input()
                    print("Ingrese su contraseña: ")
                    contrasenia = input()
                    if mth.checkearAdmin(usuario, contrasenia):
                        autorizacion = mth.checkearAdmin(
                            usuario, contrasenia)
                        print("Credenciales validadas")
                        listOfProdcts = mth.eliminarProducto(
                            listOfProdcts)
                        break
                    else:
                        print("Usuario o Contraseña incorrectos")
                        break
                if autorizacion:
                    listOfProdcts = mth.eliminarProducto(listOfProdcts)
        case 4:
            mth.checkIds(listOfProdcts)
        case 5:
            medio = mth.medioDePago()
            listOfProducts, saldo = mth.comprar(listOfProdcts, saldo, medio)
        case 6:
            print(f"Su saldo es de: {saldo}")
        case 7:
            flag = False

print("Hasta luego!")
