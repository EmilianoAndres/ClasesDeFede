from productOnlyId import *


def CheckearId(id: int, listOfProducts: list[ProductOnlyId]) -> bool:
    for product in listOfProducts:
        if product._id == id:
            return True
    return False


def CrearProducto(id: int, listOfProducts: list[ProductOnlyId]) -> list[ProductOnlyId]:
    for product in listOfProducts:
        if product._id == id:
            print("Ya existe un producto con esta id")
            return listOfProducts
    else:
        newProduct: ProductOnlyId = ProductOnlyId(id)
        print("Ingrese el nombre del producto")
        newProduct._nombre = input()
        print("Ingrese el precio del producto")
        while True:
            try:
                newProduct._precio = float(input())
                break
            except:
                print("Por favor solo valores numéricos")
        print("Ingrese el stock del producto")
        while True:
            try:
                newProduct._stock = int(input())
                break
            except:
                print("Por favor solo valores numéricos")
        listOfProducts.append(newProduct)
        return listOfProducts


def declararSaldo() -> float:
    saldo: float = 0
    print("Por favor, ingrese su saldo")
    while True:
        try:
            saldo = int(input())
            if saldo > 0:
                return saldo
            else:
                print("Ingrese un saldo mayor a 0")
        except:
            print("Por favor solo valores numéricos")


def comprar(listOfProducts: list[ProductOnlyId], saldo: float, medio: int):
    productoAComprar: str = ""
    cantidad: int = 0
    ConsultarProductos(listOfProducts)
    print("indique el nombre del producto a comprar: ")
    productoAComprar = input()
    productoAComprar.lower
    for producto in listOfProducts:
        if producto._nombre == productoAComprar:
            print(
                f"Indique la cantidad a adquirir del producto {producto._nombre}: ")
            while True:
                try:
                    cantidad = int(input())
                    diezPorcientoPrecio: float = (producto._precio / 10)
                    if (medio == 1):
                        print("Las compras en efectivo tienen un 10% de descuento")
                        if (cantidad > 0 and cantidad <= producto._stock and saldo >= ((producto._precio - diezPorcientoPrecio) * cantidad)):
                            saldo -= ((producto._precio -
                                      diezPorcientoPrecio) * cantidad)
                            producto._stock -= cantidad
                            print(
                                f"Usted compró {cantidad} unidades del producto '{producto._nombre} en efecitvo por un precio de {(producto._precio - diezPorcientoPrecio) * cantidad}")
                            break
                        else:
                            print(
                                "No se ha podido realizar la compra por falta de fondos, stock, o ausencia del producto")
                            break
                    if (medio == 2):
                        if (cantidad > 0 and cantidad <= producto._stock and saldo >= (producto._precio * cantidad)):
                            saldo -= (producto._precio * cantidad)
                            producto._stock -= cantidad
                            print(
                                f"Usted compró {cantidad} unidades del producto '{producto._nombre} con tarjeta de débito por un precio de {producto._precio  * cantidad}")
                            break
                        else:
                            print(
                                "No se ha podido realizar la compra por falta de fondos, stock, o ausencia del producto")
                            break
                    if (medio == 3):
                        print("Las compras en efectivo tienen un 10% de recargo")
                        if (cantidad > 0 and cantidad <= producto._stock and saldo >= ((producto._precio + diezPorcientoPrecio) * cantidad)):
                            saldo -= ((producto._precio +
                                      diezPorcientoPrecio) * cantidad)
                            producto._stock -= cantidad
                            print(
                                f"Usted compró {cantidad} unidades del producto '{producto._nombre} con tarjeta de crédito por un precio de {(producto._precio + diezPorcientoPrecio) * cantidad}")
                            break
                        else:
                            print(
                                "No se ha podido realizar la compra por falta de fondos, stock, o ausencia del producto")
                            break
                    else:
                        break
                except:
                    print("Solo valores numéricos")
            break
    return listOfProducts, saldo


def verMenu() -> int:
    opcion: int = 0
    print("Presione 1 para consultar los productos")
    print("Presione 2 para modificar un producto")
    print("Presione 3 para eliminar un producto")
    print("Presione 4 para consultar las IDs de los productos")
    print("Presione 5 para comprar")
    print("Presione 6 para consultar el saldo")
    print("Presione 7 para salir")
    while True:
        try:
            opcion = int(input())
            if opcion in [1, 2, 3, 4, 5, 6, 7]:
                return opcion
            else:
                print("Por favor, seleccione 1 para consulta de productos")
                print("2 para modificar un producto, 3 para eliminar un producto")
                print("4 para consultar IDs de productos, 5 para comprar")
                print("6 para comsultar el saldo, 7 para salir")
        except:
            print("Solo valores numéricos")


def medioDePago() -> int:
    medio: int = 0
    print("Seleccione 1 si abona en efectivo")
    print("Seleccione 2 si abona en débito")
    print("Seleccione 3 si abona en crédito")
    while True:
        try:
            medio = int(input())
            if (medio in [1, 2, 3]):
                return medio
            else:
                print("Por favor, indique si paga en efectivo (1)")
                print("con débito (2) o con crédito (3) \n")
        except:
            print("Las opciones aceptadas son solo numéricas")


def checkearAdmin(user: str, password: str) -> bool:
    if user == "admin" and password == "1234":
        return True
    return False


def ConsultarProductos(listOfProducts: list[ProductOnlyId]) -> None:
    print("Estos son los productos actualmente en stock: ")
    for product in listOfProducts:
        print(f"{product._nombre}, con un precio de {product._precio}")
        print(f"cuenta con un stock de {product._stock} \n")


def ModificarProductos(listOfProducts: list[ProductOnlyId]) -> list[ProductOnlyId]:
    id: int = 0
    productExists: bool = False
    indiceDelProducto: int = 0
    print("Ingrese la ID del producto a modificar: ")
    while True:
        try:
            id = int(input())
            for product in listOfProducts:
                if (product._id == id):
                    productExists = True
                    indiceDelProducto = listOfProducts.index(product)
                    break
            if productExists == False:
                print("No se encontró la ID del producto")
                break
            break
        except:
            print("Solo valores numéricos")
    if productExists:
        print("Ingrese el nuevo precio del producto: ")
        while True:
            try:
                listOfProducts[indiceDelProducto]._precio = float(input())
                if (listOfProducts[indiceDelProducto]._precio > 0):
                    break
                else:
                    print("Por favor, valores mayores a 0")
            except:
                print("Solo valores numéricos.")
        print("Ahora ingrese el nuevo stock del producto: ")
        while True:
            try:
                listOfProducts[indiceDelProducto]._stock = int(input())
                if (listOfProducts[indiceDelProducto]._stock > 0):
                    break
                else:
                    print("Por favor, valores mayores a 0")
            except:
                print("Solo valores numéricos.")
    return listOfProducts


def checkIds(listOfProducts: list[ProductOnlyId]) -> None:
    for product in listOfProducts:
        print(f"{product._id}, {product._nombre}")


def eliminarProducto(listOfProducts: list[ProductOnlyId]) -> list[ProductOnlyId]:
    elementoEliminado: bool = False
    id: int = 0
    length: int = len(listOfProducts) - 1
    print("Ingrese la ID del producto a eliminar")
    while True:
        try:
            id = int(input())
            if (id <= 0):
                print("No existen productos con IDs menores a 0")
                break
            for product in listOfProducts:
                if product._id == id:
                    index: int = listOfProducts.index(product)
                    listOfProducts.pop(index)
                    for i in range(index, length):
                        listOfProducts[i]._id -= 1
                    elementoEliminado = True
                    break
            if not elementoEliminado:
                print("No se encontró el producto")
            break
        except:
            print("Solo valores numéricos")
    return listOfProducts
