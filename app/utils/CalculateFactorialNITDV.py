# Este módulo contiene la clase CalculateFactorialNIT, 
# que proporciona una función para calcular el factorial 
# de cada dígito de un NIT (Número de Identificación Tributaria) 
# y sumar esos factoriales.
import math

def calculateFactorialNIT(nit: str) -> int:
    total = 0
    for digit in nit:
        if digit.isdigit():
            total += math.factorial(int(digit))
    return total

def calculateDV(total: int) -> int:
    return total % 10

nit = "800099304"

factorial_sum = calculateFactorialNIT(nit)
dv = calculateDV(factorial_sum)

print(f"Suma de factoriales: {factorial_sum}")
print(f"DV: {dv}")

