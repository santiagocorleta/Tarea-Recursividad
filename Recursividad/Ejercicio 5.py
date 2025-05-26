def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    if not romano:
        return 0
    if len(romano) == 1:
        return valores[romano]
    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + romano_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
numero_romano = input("Ingrese un número romano: ").upper()

decimal = romano_a_decimal(numero_romano)
print(f"El número romano {numero_romano} en decimal es {decimal}.")X