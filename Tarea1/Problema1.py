def procesar_lista(valores):
    # 1. Eliminar negativos
    positivos = [v for v in valores if v >= 0]

    # 2. Eliminar duplicados
    sin_duplicados = list(set(positivos))

    # 3. Ordenar
    ordenados = sorted(sin_duplicados)

    return ordenados


# Ejemplo de uso
lista = [4, -1, 2, 4, 3, -5, 2]
resultado = procesar_lista(lista)
print("Resultado final:", resultado)
