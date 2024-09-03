
# Simplificación de Expresiones Booleanas con Python

Este proyecto muestra cómo simplificar expresiones booleanas utilizando Python, aprovechando la biblioteca `sympy` para manejar operaciones simbólicas y simplificación lógica.

## Descripción

La simplificación de expresiones booleanas es un paso clave en el diseño de circuitos digitales, y una de las herramientas más comunes para esto es el uso de mapas de Karnaugh. Este proyecto demuestra cómo implementar una simplificación de expresiones booleanas en Python, lo cual puede ser muy útil para la optimización de circuitos digitales.

## Requisitos

- Python 3.x
- sympy (`pip install sympy`)

## Implementación

El código se basa en la manipulación de expresiones booleanas usando `sympy`, una biblioteca que permite el manejo de expresiones simbólicas y operaciones algebraicas.

### Código Ejemplo

```python
from sympy import symbols, Or, And, Not
from sympy.logic.boolalg import truth_table, simplify_logic

# Definir las variables booleanas
A, B, C = symbols('A B C')

# Definir la función booleana usando las operaciones lógicas de sympy
# Ejemplo: F(A, B, C) = A'BC' + A'BC + ABC
expression = Or(And(Not(A), B, Not(C)), And(Not(A), B, C), And(A, B, C))

# Simplificación de la expresión usando sympy
simplified_expression = simplify_logic(expression, form='dnf')

print(f"Expresión original: {expression}")
print(f"Expresión simplificada: {simplified_expression}")

# Mostrar la tabla de verdad para la expresión simplificada
print("Tabla de verdad:")
for row in truth_table(simplified_expression, [A, B, C]):
    print(f"{row[0]}: {row[1]}")
```

### Explicación del Código

1. **Definición de Variables**:
   - Usamos `symbols` de `sympy` para definir las variables booleanas (A, B, C).

2. **Definición de la Expresión Booleana**:
   - Creamos la función booleana que queremos simplificar utilizando operadores lógicos como `And`, `Or`, y `Not`.

3. **Simplificación**:
   - Utilizamos la función `simplify_logic` de `sympy` para simplificar la expresión booleana. Aquí, `form='dnf'` especifica que la salida debe estar en forma normal disyuntiva, lo que es equivalente a la salida de un mapa de Karnaugh.

4. **Tabla de Verdad**:
   - La función `truth_table` genera la tabla de verdad de la expresión simplificada para validar su corrección.

## Consideraciones

- **Escalabilidad**: Este enfoque funciona bien para un número moderado de variables (hasta 4 o 5). Para un número mayor de variables, el algoritmo se vuelve más complejo.
- **Optimización**: La simplificación no siempre será mínima en todos los aspectos, pero `sympy` suele dar soluciones bastante optimizadas.
- **Flexibilidad**: Puedes modificar el código para trabajar con diferentes números de variables y diferentes formas de expresiones booleanas.

# Ejemplos de Simplificación de Expresiones Booleanas

Este documento proporciona varios ejemplos de cómo simplificar expresiones booleanas utilizando mapas de Karnaugh, una herramienta esencial en el diseño de circuitos digitales.

## Ejemplo 1: Tres Variables

### Tabla de Verdad

| A | B | C | F(A, B, C) |
|---|---|---|------------|
| 0 | 0 | 0 |      0     |
| 0 | 0 | 1 |      1     |
| 0 | 1 | 0 |      1     |
| 0 | 1 | 1 |      1     |
| 1 | 0 | 0 |      0     |
| 1 | 0 | 1 |      0     |
| 1 | 1 | 0 |      1     |
| 1 | 1 | 1 |      1     |

### Mapa de Karnaugh

| AB\C | 00 | 01 | 11 | 10 |
|------|----|----|----|----|
| **00** |  0  |  1  |  1  |  0  |
| **01** |  0  |  0  |  1  |  0  |

### Expresión Simplificada

\[ F(A, B, C) = B + C \]

## Ejemplo 2: Cuatro Variables

### Minitérminos

\[ F(A, B, C, D) = \Sigma(1, 3, 7, 11, 15) \]

### Mapa de Karnaugh

| AB\CD | 00 | 01 | 11 | 10 |
|-------|----|----|----|----|
| **00** |  0  |  1  |  0  |  0  |
| **01** |  0  |  1  |  0  |  0  |
| **11** |  0  |  1  |  1  |  0  |
| **10** |  0  |  0  |  0  |  0  |

### Expresión Simplificada

\[ F(A, B, C, D) = BD + CD \]

## Ejemplo 3: Dos Variables

### Tabla de Verdad

| A | B | F(A, B) |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    1    |
| 1 | 0 |    1    |
| 1 | 1 |    1    |

### Mapa de Karnaugh

| A\B | 0 | 1 |
|-----|---|---|
| **0** | 0 | 1 |
| **1** | 1 | 1 |

### Expresión Simplificada

\[ F(A, B) = A + B \]

## Ejemplo 4: Cuatro Variables Complejo

### Minitérminos

\[ F(A, B, C, D) = \Sigma(0, 1, 2, 5, 8, 9, 10, 11, 14, 15) \]

### Mapa de Karnaugh

| AB\CD | 00 | 01 | 11 | 10 |
|-------|----|----|----|----|
| **00** |  1  |  1  |  0  |  1  |
| **01** |  1  |  1  |  1  |  0  |
| **11** |  1  |  1  |  0  |  0  |
| **10** |  1  |  0  |  0  |  0  |

### Expresión Simplificada

\[ F(A, B, C, D) = A'B' + AB + CD' \]

Estos ejemplos ilustran cómo los mapas de Karnaugh son utilizados para simplificar expresiones booleanas, facilitando el diseño de circuitos digitales más eficientes.

## Uso

1. Clona este repositorio.
2. Asegúrate de tener instalados Python y la biblioteca `sympy`.
3. Ejecuta el script en tu entorno local y observa la simplificación de la expresión booleana y la tabla de verdad resultante.
