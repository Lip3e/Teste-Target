def inverter_string(string):
    inverted_string = ''
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

# Exemplo de uso:
entrada = input("Escreva uma string para inverter: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)
