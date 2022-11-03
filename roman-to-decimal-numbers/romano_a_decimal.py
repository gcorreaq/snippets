# Este archivo puede estar desactualizado. Si encuentra cosas que no estan aqui pero si
# estan presentes en roman_to_decimal.py, por favor crear un nuevo issue en el proyecto


# Este diccionario establece las equivalencias entre las letras de numerales romanos
# y sus valores decimales
EQUIVALENCIAS: dict[str, int] = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


def romano_a_decimal(numeral_romano: str) -> int:
    """Transforma un numeral romano a decimal.

    String vacios o con caracteres no soportados resultan en excepciones.

    Notar que el mayor valor que se puede transformar es MMMCMXCIX (3999). Para mas
    detalles ver https://en.wikipedia.org/wiki/Roman_numerals#Standard_form
    """

    # Siempre revisamos que el string tenga algo
    if len(numeral_romano) < 1:
        # ValueError es la excepcion estandar que mas se acerca a indicar lo que paso acá
        raise ValueError("El valor no puede estar vacio")

    # Al usar string.upper() nos aseguramos de que los caracteres en el input siempre va a calzar
    # con nuestro diccionario de equivalencias
    numeral_romano = numeral_romano.upper()

    # Aqui llevamos el total, que despues sera el numero decimal
    resultado = 0
    # Para hacerlo mas facil, usamos como referencia de partida el primer caracter del numeral
    # romano. Esto es porque el algoritmo ocupa siempre el valor anterior para decidir que hacer
    valor_anterior = EQUIVALENCIAS[numeral_romano[0]]

    # Aca ocupamos la funcion enumerate() simplemente para tener mejores mensajes de error.
    # Para mas informacion sobre enumerate(), ver
    # https://docs.python.org/3/library/functions.html#enumerate
    for posicion, caracter in enumerate(numeral_romano, start=1):
        try:
            valor_actual = EQUIVALENCIAS[caracter]
        # Vamos a llegar a este bloque except solo cuando el caracter actual no este en el
        # diccionario de equivalencias.
        except KeyError as e:
            # Notar que aca se ocupa la sintaxis `raise A from B`. Esto ayuda a mantener la
            # excepcion original y nos permite agregar mas detalles de que sucedio
            raise KeyError(
                f"El caracter {caracter} en la posicion {posicion} no esta soportado o es invalido"
            ) from e

        # Cuando el valor anterior es mayor o igual que el actual, aplicamos suma
        if valor_anterior >= valor_actual:
            resultado += valor_actual
        else:
            # De lo contrario, tenemos que hacer algo un poco enredado
            # - Primero, dado que ya habiamos sumado el valor anterior, vamos a tener que sustraerlo
            #   para que no se cuente dos veces, asi que primero hacemos
            #
            #     `resultado - valor_actual`
            #
            # - Despues tenemos que tomar el valor actual y sustraerle el valor anterior
            #
            #     `valor_actual - valor_anterior`
            #
            # - Finalmente tenemos que tomar ambos valores y agregarlos al resultado, terminando con
            #   siguiente expresion
            #
            #     `result = (result - previous_value) + (current_value - previous_value)`
            #
            # Que es equivalente a la expresion aca
            resultado += valor_actual - (2 * valor_anterior)

        valor_anterior = valor_actual

    return resultado


if __name__ == "__main__":
    numeral_romano = input("Numeral romano: ")
    numero_decimal = romano_a_decimal(numeral_romano)
    print(f"Numero decimal: {numero_decimal}")
