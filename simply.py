from sympy import symbols, Or, And, Not
from sympy.logic.boolalg import truth_table, simplify_logic

A, B, C = symbols('A B C')


# Ejemplo: F(A, B, C) = A'BC' + A'BC + ABC
expression = Or(And(Not(A), B, Not(C)), And(Not(A), B, C), And(A, B, C))

# Simplificación
simplified_expression = simplify_logic(expression, form='dnf')

print(f"Expresión original: {expression}")
print(f"Expresión simplificada: {simplified_expression}")

# Mostrar la tabla de verdad para la expresión simplificada
print("\nTabla de verdad:")
for row in truth_table(simplified_expression, [A, B, C]):
    print(f"{row[0]}: {row[1]}")