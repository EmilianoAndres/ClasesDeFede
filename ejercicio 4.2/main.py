import methods as mth

opcion: str = "";
print("Bienvenido al ejercicio 4.2 \n");
print("Desea seguir o salir? s para seguir, cualquier tecla para salir")
opcion = input();
if(opcion == "s"):
    mth.ElegirFigura();
else: print("Ha salido del programa con éxito");


    