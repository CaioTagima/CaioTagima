print("Calculadora usando Python")
print("Digite os dois números e logo após a operação que deseja executar:")
print("(+) soma (-) subtração (*) multiplicação (/) divisão")

while True:
    prinumero = input("Digite o primeiro número: ")
    segnumero = input("Digite o segundo número: ")
    operacao = input("Digite a operação que deseja executar: ")
    
    operadores_permitidos = "+-*/"
    numeros_validos = None

    try:
        prinumero_float = float(prinumero)
        segnumero_float = float(segnumero)
        numeros_validos = True
    except ValueError:
        print("Número inválido! Tente novamente.")
        continue

    if operacao not in operadores_permitidos or len(operacao) > 1:
        print("Operador inválido! Tente novamente.")
        continue

    if operacao == "+":
        resultado = prinumero_float + segnumero_float
    elif operacao == "-":
        resultado = prinumero_float - segnumero_float
    elif operacao == "*":
        resultado = prinumero_float * segnumero_float
    elif operacao == "/":
        if segnumero_float == 0:
            print("Erro! Divisão por zero não é permitida.")
            continue
        resultado = prinumero_float / segnumero_float
    
    print(f"O resultado é: {resultado}")

    sair = input("Quer sair? (s)im ou (n)ão: ").lower()
    if sair.startswith("s"):
        break

