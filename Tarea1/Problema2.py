import string

def contar_palabras(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        texto = f.read()

    # Limpiar texto
    texto = texto.lower()
    for p in string.punctuation:
        texto = texto.replace(p, "")

    palabras = texto.split()

    # Contar frecuencias
    frecuencia = {}
    for palabra in palabras:
        if palabra not in frecuencia:
            frecuencia[palabra] = 1
        else:
            frecuencia[palabra] += 1

    # Devolver ordenado por clave
    return dict(sorted(frecuencia.items()))


# Script de prueba
if __name__ == "__main__":
    ruta = "texto_prueba.txt"
    resultado = contar_palabras(ruta)
    print("Frecuencia de palabras:")
    for palabra, veces in resultado.items():
        print(palabra, ":", veces)
