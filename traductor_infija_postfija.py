# tokens de ejemplo
tokens = ["2", "+", "3", "*", "4"]

# Estructuras del algoritmo Shunting-Yard
output = []     # Aquì ira la salida en postfijo
stack = []      # Esta es la pila

# Prioridad de operadores
precedencia = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

print("Tokens cargados:", tokens)
print("Estructuras listas para iniciar el algoritmo.")
