import methods as mth;

session: str = "s";
print("Bienvenido al ejercicio 4.4 \n");
print("Por favor, indique qué método utilizar: \n")
while(session == "s"):
    seleccion: int = 0;
    print("1. Conversor entre Celcius y Fahrenheit.")
    print("2. Conversor entre Pesos y Dólares.")
    print("3. Conversor entre Centímetros Cúbicos y Litros.")
    while(True):
        try:
            seleccion = int(input());
            if(seleccion in [1,2,3]):
                break;
            else: print("Del 1 al 3, por favor.")
        except:
            print("Por favor, solo números del 1 al 3")
    match seleccion:
        case 1:
            mth.ConversorTemperatura();
        case 2:
            mth.ConversorMoneda();
        case 3:
            mth.ConversorUnidades();
    print("Quiere iniciar el programa nuevamente? 's' para sí, cualquier otra tecla para salir")
    session = input();
    if(session != "s"):
        break;
print("Hasta la próxima!");