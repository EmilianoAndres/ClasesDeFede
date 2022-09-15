def ContadorDeLetras(letra: str, palabra: str) -> int:
    contador: int = 0;
    for i in palabra:
        if i == letra: contador+=1;
    return contador;
        
def CompararPalabras(palabra1: str, palabra2: str) -> str:
    if(len(palabra1)> len(palabra2)): return "primer";
    else: return "segunda";
    
def RemovedorDeVocales(palabra: str) -> str:
    palabraresultante: str = "";
    for i in range(len(palabra)):
        if palabra[i] not in ["a","e","i","o","u","A","E","I","O","U"]:
            palabraresultante += palabra[i];
    return palabraresultante;