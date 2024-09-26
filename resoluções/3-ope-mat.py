## 3 - Operações Matemáticas Simples 📐

#Descrição:
#Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
#
#O que aprenderemos?
#
#* Operações Matemáticas Básicas
#* Entrada de dados
#* Utilização eficiente do Github Copilot

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
ope = input("Digite uma das operações matemáticas (+, -, *, /): ")

match ope:
    case "+":
        # Código para a opção 1
        res = num1 + num2
    case "-":
        # Código para a opção 2
        res = num1 - num2
    case "*":
        # Código para a opção 3
        res = num1 * num2
    case "/":
        # Código para a opção 4
        res = num1 / num2
    case _:
        # Código padrão
        print("Operação inválida")

print(res)