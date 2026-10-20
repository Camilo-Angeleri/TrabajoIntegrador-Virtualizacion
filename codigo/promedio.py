"""Programa de promedios.

Pide notas por teclado (de 0 a 10, se aceptan decimales) hasta que el
usuario escribe 'stop'. Al final muestra las notas ingresadas y su promedio.
"""

NOTA_MIN = 0
NOTA_MAX = 10


def pedir_notas():
    """Pide notas al usuario hasta que escribe 'stop' y devuelve la lista."""
    notas = []  # lista vacía donde se guardan solo las notas válidas

    while True:
        # Se lee lo que escribe el usuario. strip() quita espacios sobrantes
        # y replace() permite escribir decimales con coma (por ejemplo 7,5).
        entrada = input(f"Nota {len(notas) + 1}: ").strip().replace(",", ".")

        # Condición de salida del bucle.
        if entrada.lower() == "stop":
            break

        # Se intenta convertir el texto a número; si no se puede, se avisa.
        try:
            nota = float(entrada)
        except ValueError:
            print("Valor inválido: ingresá un número, por ejemplo 8 o 7.5.")
            continue

        # Se valida que la nota esté dentro del rango permitido.
        if not NOTA_MIN <= nota <= NOTA_MAX:
            print(f"La nota debe estar entre {NOTA_MIN} y {NOTA_MAX}.")
            continue

        notas.append(nota)

    return notas


def calcular_promedio(notas):
    """Devuelve el promedio: la suma de las notas dividida por la cantidad."""
    return sum(notas) / len(notas)


def main():
    print("-" * 40)
    print("Ingresá tus notas (0 a 10, se aceptan decimales).")
    print("Para terminar, escribí 'stop'.")
    print("-" * 40)

    notas = pedir_notas()

    print("\n" + "-" * 40)
    if notas:
        print("Tus notas:")
        for i, nota in enumerate(notas, start=1):
            print(f"  {i}. {nota}")
        print(f"\nPromedio: {calcular_promedio(notas):.2f}")
    else:
        print("No se ingresaron notas.")
    print("-" * 40)


# Este bloque hace que main() se ejecute solo cuando se corre el archivo
# directamente (python3 promedio.py) y no cuando se importa desde otro.
if __name__ == "__main__":
    main()
