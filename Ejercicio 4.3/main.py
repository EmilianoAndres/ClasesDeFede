import methods as mth

print("Bienvenido al ejercicio 4.3 \n")
print("Por favor, elija una de las siguientes opciones: \n")
print("1: Contador de Letras de una palabra u oración\n")
print("2: Comparador de cantidad de caracteres entre 2 palabras u oraciones \n")
print("3: Removedor de vocales en una palabra/oración \n")
opcion: int = 0;
while(True):
    try:
        opcion = int(input());
        if(opcion in [1,2,3]):
            break;
        else: print("Por favor, del 1 al 3.")
    except: 
        print("Por favor, elija un número.");

palabra1: str = "";
palabra2: str = "";
match(opcion):
    case 1:
        while(True):
                print("Introduzca la letra a verificar: ")
                palabra1 = input();
                if palabra1.isalpha() and len(palabra1) == 1:
                    print("Ahora, la palabra u oración a checkear: \n")
                    palabra2 = input();
                    print(f"La letra '{palabra1}' ocurre {mth.ContadorDeLetras(palabra1, palabra2)} veces")
                    break;
                else: print("Por favor, ingrese una sola letra")
    case 2:
        while(True):
            print("Introduzca la primer palabra u oración a comparar: \n");
            palabra1 = input();
            if len(palabra1)>1:
                print("Ahora, la segunda palabra u oración: \n")
                palabra2 = input();
                if(len(palabra1) == len(palabra2)):
                    print("Ambas tienen la misma longitud");
                    break;
                print(f"La {mth.CompararPalabras(palabra1, palabra2)} palabra u oración es la más larga")
                break;
            else: print("Por favor, ingrese una sola letra")
    case 3:
        while(True):
            print("Introduzca la palabra o frase a la cual le eliminaremos las vocales: \n")
            palabra1 = input();
            if len(palabra1) > 1:
                print(f"Luego de eliminar las vocales, la palabra u oración resultante es: \n")
                print(f"{mth.RemovedorDeVocales(palabra1)}");
                break;
            else: print("Por favor, ingrese una sola letra")
            
print("Gracias por utilizar el programa. Saludos.")