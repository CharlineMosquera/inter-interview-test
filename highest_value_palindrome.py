"""
Se desarrolla un ejercicio donde se busca obtener el numero palindromo
mas grande posible realizando una cantidad limitada de cambios,
la funcion recibe como parametros:

n (int): La cantidad de digitos de la cadena
k (int): La cantidad de cambios posibles
s (str): La representacion en cadena del numero

Y debe retornar el numero palindromo resultante como una cadena (str)
o "-1" si no fue posible realizar algun cambio.
"""


def highestValuePalindrome(n, k, s):
    """Modifica la cadena s para obtener el palindromo
    posible mas grande o retorna -1 si no es posible"""

    # Se convierte la cadena en una lista para que sea mutable
    s = list(s)

    # Para facilitar la lectura del codigo
    cambios_posibles = k

    # Para calcular los cambios minimos que se deben realizar
    cambios_need = cambios_necesarios(s, n)

    # Si la cantidad de cambios posibles
    # no es suficiente se retorna -1
    if cambios_posibles < cambios_need:
        return "-1"

    # Si la cadena tiene un solo digito se retorna
    # el mayor digito posible
    if n == 1 and cambios_posibles >= 1:
        return "9"

    adicionales = 0

    # Se evalua si hay cambios adicionales posibles
    # para obtener el palindromo mas alto
    if cambios_posibles > cambios_need:
        adicionales = cambios_posibles - cambios_need

        # Recorre desde los extremos y va cambiando
        # los digitos por 9 para obtener el numero
        # palindromo mayor posible
        for i in range(adicionales - 1):
            s[i] = '9'
            s[n - i - 1] = '9'

    # Para convertir la cadena en un palindromo
    # El ciclo for recorre la cadena
    for j in range(adicionales, n - adicionales // 2):
        # Si se encuentra que los digitos simetricos
        # son diferentes, se asigna el valor mayor
        # al digito menor para que sean iguales
        if s[j] != s[n - j - 1]:
            if int(s[j]) > int(s[n - j - 1]):
                s[n - j - 1] = s[j]
            else:
                s[j] = s[n - j - 1]

    # Se retorna s como una cadena
    return "".join(map(str, s))


def cambios_necesarios(s, n):
    """Esta funcion calcula cuantos digitos se deben
    modificar en s para obtener un palindromo"""
    cambios = 0
    index = 0

    # Se recorre la lista de caracteres
    while index < n // 2:
        # Si los caracteres simetricos son diferentes
        # Se incrementa la variable cambios
        if s[index] != s[n - index - 1]:
            cambios += 1
        # Se aumenta el indice hasta llegar al centro de la lista
        index += 1
    return cambios


if __name__ == "__main__":

    primera_linea = input().strip()

    # Para dividir la linea
    args = primera_linea.split()

    if len(args) == 2:
        # Se valida que n y k sean numeros enteros
        n, k = map(int, args)
    else:
        print("Error: Digite dos enteros separados por un espacio.")
        exit(1)

    s = input().strip()

    # Se valida que la cadena sea de digitos
    if not s.isdigit():
        print("Error: Digite un número entero.")
        exit(1)

    # se llama a la funcion y se almacena su resultado
    RESULTADO = highestValuePalindrome(n, k, s)
    print(RESULTADO)
