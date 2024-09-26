## 2 - Repetindo Textos ✏️

#Descrição:
#Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 
#
#O que aprenderemos?
#
#* Manipulação de Strings (string)
#* Números Inteiros (int)
#* Múltiplas repetições
#* Entrada de dados
#* Aproveitar as sugestões do Github Copilot

text = input("Digite um texto a ser repetido: ")
num = int(input("Digite o número de vezes a ser repetido: "))

# Cria uma lista com o texto repetido o número de vezes desejado
lista_repeticoes = [text] * num

# Junta os elementos da lista utilizando um espaço como separador
resultado = " ".join(lista_repeticoes)

print(resultado)