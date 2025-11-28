def operar_conjuntos(lista1, lista2):
    s1 = set(lista1)
    s2 = set(lista2)

    resultado = {
        "interseccion": list(s1 & s2),
        "union": list(s1 | s2),
        "diferencia_simetrica": list(s1 ^ s2)
    }

    return resultado


# Ejemplo de uso
if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2 = [3, 4, 5, 6]

    print(operar_conjuntos(l1, l2))
