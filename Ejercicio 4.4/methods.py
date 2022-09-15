


def ConversorTemperatura() -> None:
    temperatura: float = 0;
    seleccion: str = "";
    print("Indique la unidad incial: Celcius (c) o Fahrenheit (f)");
    while(True):
        try:
            seleccion = input();
            if(seleccion in ['f','c']):
                break;
            else: print("Por favor, indique 'c'elcius o 'f'ahrenheit ");
        except:
            print("ni idea qué error triggereaste pero probá de vuelta");
    print("Ahora la temperatura a convertir: \n");
    while(True):
        try:
            temperatura = int(input());
            break;
        except:
            print("Solo números, por favor");
    if(seleccion == 'c'):
        return print(f"El resultado es: {(temperatura * 9/5) + 32} grados Fahrenheit");
    else: return print(f"El resultado es: {(temperatura - 32 ) * 5/9} grados Celcius");
    
    
def ConversorMoneda() -> None:
    print("Este método toma como valor del dólar 285 pesos.")
    cantidad: float = 0;
    moneda: str = "";
    print("Indique la unidad incial: Pesos (p) o Dólares (d)");
    while(True):
        try:
            moneda = input();
            if(moneda in ['p','d']):
                break;
            else: print("Por favor, indique 'p'esos o 'd'ólares ");
        except:
            print("ni idea qué error triggereaste pero probá de vuelta");
    print("Ahora la cantidad a convertir: \n");
    while(True):
        try:
            cantidad = int(input());
            break;
        except:
            print("Solo números, por favor");
    if(moneda == 'p'):
        return print(f"El resultado es: {cantidad / 285} dolares");
    else: return print(f"El resultado es: {cantidad * 285} pesos");
    
def ConversorUnidades() -> None:
    cantidad: float = 0;
    seleccion: str = "";
    print("Indique la unidad incial: Centímetros Cúbicos (c) o Litros (l)");
    while(True):
        try:
            seleccion = input();
            if(seleccion in ['c','l']):
                break;
            else: print("Por favor, indique 'c'm3 o 'l'itros ");
        except:
            print("ni idea qué error triggereaste pero probá de vuelta");
    print("Ahora la cantidad a convertir: \n");
    while(True):
        try:
            cantidad = int(input());
            break;
        except:
            print("Solo números, por favor");
    if(seleccion == 'c'):
        return print(f"El resultado es: {cantidad / 1000} litros") ;
    else: return print(f"El resultado es: {cantidad * 1000} centímetros cúbicos");