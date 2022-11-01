# Transformar números romanos a decimales

[README in english](README.md)

Este código fue inicialmente creado como una solución a un problema de la clase de Programación en la Universidad Técnica Federico Santa María (UTFSM o USM) en el tiempo en que fui ayudante. En algún momento puse el código en Github Gists pero nunca lo actualice, y ya han habido comentarios sobre problemas que la gente ha encontrado. Con el tiempo iré actualizando el script para dejarlo funcional con versiones modernas de Python.

Hay dos scripts:

- [`roman_to_decimal.py`](roman_to_decimal.py): El código actualizado para correr en versiones modernas de Python
- [`romano_a_decimal.py`](romano_a_decimal.py): El mismo código pero con comentarios en Español, explicando cada pequeño detalle del código

Ambos solo soportan transformar numeros hasta 3999 (Ver <https://en.wikipedia.org/wiki/Roman_numerals#Standard_form>)

Por cualquier pregunta, comentarios o sugerencias, por favor revisa la [lista de issues](https://github.com/gcorreaq/snippets/issues), y si no encuentras algo similar, por favor crea un [nuevo Issue](https://github.com/gcorreaq/snippets/issues/new) en este projecto.

## Explicación del algoritmo

La idea principal detrás de el código es la siguiente:

- Para transformar un numeral romano a un numero decimal, tenemos que considerar que los numerales romanos están representados por una cadena de caracteres, y la representación decimal del numeral romano es una combinación de adición y sustracción de los valores de la representación decimal de cada caracter a un total.
- Tenemos que tomar un caracter a la vez del numeral romano, y lo qye hacemos con cada caracter depende de la representacion decimal del caracter anterior. Esto también se puede hacer de manera inversa: tomamos cada caracter, y lo que hacemos con el dependende del valor decimal del caracter siguiente.
- Al final tomamos el total y lo usamos como nuestra representación decimal
