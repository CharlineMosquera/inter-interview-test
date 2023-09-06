# Ejercicio encontrar el número palíndromo mas alto

Aqui presento mi solución a un ejercicio que se realiza como parte de un proceso para aplicar a una vacante laboral.

## Descripción del Problema

Este ejercicio consiste en tomar una representación en cadena de un número y un número máximo de cambios que se le pueden aplicar y realizar cambios en ella para obtener el número palíndromo más grande posible dentro del límite de cambios establecido. Se debe conservar la longitud de la cadena y considerar los "0"s a la izquierda de todos los dígitos.

## ¿Por qué seleccione este ejercicio?

Me decidi por este ejercicio ya que representa un desafio de como optimizar una cadena de dígitos y convertirla en un palíndromo y al tener un limite en la cantidad de cambios que se pueden aplicar conlleva a un razonamiento algoritmico cautivador.

## ¿Cómo lo resolvi?

Me abstuve de empezar a escribir el código hasta no entender por completo el ejercicio y los ejemplos presentados.

Realice una solución en el lenguaje Python utilizando un ciclo que recorre cada carácter de la representación en cadena del número desde los extremos hacia el centro validando si son iguales y si no cambiando los dígitos por el mayor digito posible teniendo en cuenta el limite establecido de cambios posibles.

## ¿Cómo ejecutar el código?

Para ejecutar este ejercicio siga los siguientes pasos:

1. Clonar este repositorio `git clone https://github.com/CharlineMosquera/inter-interview-test.git`.
2. Ejecutar  `python3 highest_value_palindrome.py` proporcionando en una línea separada la cantidad de dígitos del número y el número máximo de cambios permitidos y en la siguiente línea una cadena de números de n dígitos.

### Ejemplo de uso

Ejecucion e ingreso de argumentos:
```bash
python3 highest_value_palindrome.py
4 1
3943
```

Salida:

```bash
3993
```

## Autor

Charline Mosquera - [Github](https://github.com/CharlineMosquera)
