# Desafio 05

string = input("Digite qualquer texto: ")

armazenar_string = list(string)

# precisei criar uma variavel para puxar o tamanho da lista, pois nao consegui implementar dentro do for (tentei utilizar for i in range(len(armazenar_string)): 
tamanho_lista = len(armazenar_string)

for i in range(tamanho_lista // 2):
    # troca os caracteres
    temp = armazenar_string[i]
    armazenar_string[i] = armazenar_string[tamanho_lista - 1 - i]
    armazenar_string[tamanho_lista - 1 - i] = temp

string_invertida = ''.join(armazenar_string)

print(f"{string_invertida}")
