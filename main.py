print("Projeto Calculadora")

a = float(input("Digite o primairo número: "))
b = float(input("Digite o segundo número: "))

print("Escolha a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Número da operação: ")

if operacao == "1":
    print("Resultado da soma: ", a + b)
elif operacao == "2":
    print("Resultado da subtração: ", a - b)
elif operacao == "3":
    print("Resultado da multiplicação: ", a * b)
elif operacao == "4":
    print("Resultado da divisão: ", a / b)