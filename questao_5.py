# Definindo a string que será invertida
string = "Guilherme"

# Criando uma lista vazia para armazenar os caracteres invertidos
caracteres_invertidos = []

# Percorrendo a string de trás para frente e adicionando cada caractere à lista
for i in range(len(string)-1, -1, -1):
    caracteres_invertidos.append(string[i])

# Juntando os caracteres invertidos em uma nova string
string_invertida = ''.join(caracteres_invertidos)

# Imprimindo a string invertida
print(string_invertida)