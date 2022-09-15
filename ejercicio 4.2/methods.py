from math import pi

def Calculadora(a: int, b: int, operacion: str) -> (int | float | str):
    # Solución usando pattern matching
    match operacion:
        case "s":
            return a+b;
        case "m":
            return a*b;
        case "r":
            return a-b;
        case "d":
            return a/b;
    
    # Solución con simple if else
    # if (operacion == 's'):
    #     return a+b;
    # elif (operacion == 'r'):
    #     return a-b;
    # elif (operacion == 'm'):
    #     return a*b;
    # elif (operacion == 'd'):
    #     if(b == 0):
    #         return "Error, no se puede dividir por cero"
    #     else:
    #         return a/b;
        
def CalcularDosNumeros() -> None:
    print("Desea calcular? presione s para sí, cualquier otra tecla para salir");
    inicio: str = input();
    if(inicio == "s"):
        session: int = 1;
        while(session == 1):
            num1: int = 0;
            num2: int = 0;
            operacion: str = "";
            print("Por favor, elija dos números");
            while(True):
                try:
                    num1 = int(input());
                    num2 = int(input());
                    break;
                except: print("error de tipo, intente con números");
                
            print("Ahora, ingrese el tipo de operación que desea relizar: \n");
            print("Suma (s), Resta (r), Multiplicacion (m), División (d)");

            while(True):
                operacion = input()
                if(operacion in ['s','m','r','d']):
                    print(f"El resultado de su operacion es: {Calculadora(num1, num2, operacion)}");
                    break;
                else: 
                    print("Por favor, elija una opción correcta: \n");
                    print("Suma (s), Resta (r), Multiplicacion (m), División (d)");
            print("Desea realizar otra operacion? s/n")
            if(input() == "n"):
                session = 0;
    print("Hasta pronto!");
    
# programa debe contar con 4 operaciones, area y perimetro de un cuadrado, are y perimetro de un circulo
# menu de eleccion
# pedir parametros para calcular
# gestionar errores

def Calcular(a: float, operacion: str, figura: str) -> float:
    if(figura == "cu" and operacion == "a"):
        return a**2;
    elif(figura == "cu" and operacion == "p"):
        return a*4;
    elif(figura == "ci" and operacion == "a"):
        return pi*(a**2);
    elif(figura == "ci" and operacion == "p"):
        return pi*a*2;
    pass

def ElegirFigura() -> None:
    figura: str = "";
    operacion: str = "";
    dato: float = 0;
    print("Por favor elija una figura a calcular: \n")
    while(True):
        print("Círculo (ci) o Cuadrado (cu) \n")
        figura = input();
        if(figura in ["ci","cu"]):
            break;
        else: print("Por favor elija una figura de las dos siguientes: \n")
    print("Ahora, elija una operación a realizar: \n")
    while(True):
        print("Calcular el perímetro (p) o el área (a) \n");
        operacion = input();
        if(operacion in ["p", "a"]):
            break;
        else: print("Por favor, elija una de las dos operaciones siguientes: \n");
    if(figura == "cu"):
        while(True):
            try:
                print("Finalmente, ingrese el lado del cuadrado")
                dato = int(input());
                if(dato > 0):
                    break;
            except: print("Por favor ingrese un valor correcto. Número mayor que 0");
    if(figura == "ci"):
        while(True):
            try:
                print("Finalmente, ingrese el radio del círculo")
                dato = int(input());
                if(dato > 0):
                    break;
            except: print("Por favor ingrese un valor correcto. Número mayor que 0");
    print(f"El resultado es: {Calcular(dato, operacion, figura)}");
    
def ContadorDeLetras(letra: str, palabra: str) -> int:
    contador: int = 0;
    for i in palabra:
        if i == letra: contador+=1;
    return contador;
        
def CompararPalabras(palabra1: str, palabra2: str) -> str:
    if(len(palabra1)> len(palabra2)): return palabra1;
    else: return palabra2;
    
def RemovedorDeVocales(palabra: str) -> str:
    palabraresultante: str = "";
    for i in range(len(palabra)):
        if palabra[i] not in ["a","e","i","o","u"]:
            palabraresultante += palabra[i];
    return palabraresultante;