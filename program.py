import os 

dourado = "\033[33m"  
azul = "\033[34m"     

def linearMethod(valor):
    contador = 0
    total_soma = 0
    divisor_atual = 1

    while divisor_atual <= valor:
        resultado_divisao = valor // divisor_atual
        total_soma += resultado_divisao
        divisor_atual += 1
        contador += 1

    return total_soma, contador


def bestmethod(numero):
    soma = 0
    divisor = 1
    x = 0

    while numero // divisor > 0:
        resultado = numero // divisor
        soma += resultado
        prov = numero // resultado
        if prov != divisor:
            dif = prov - divisor
            soma += dif * resultado
            divisor = prov + 1
        else:
            divisor += 1
        x += 1

    return soma, x

def calcular():
    os.system('cls')
    while True:
        try:
            numero = int(input(f"\n{azul}Me dê um número e calcularei a {dourado}soma das divisões{azul}:\n"))
            break 
        except ValueError:
            print(f"\n{dourado}Por favor, insira um número válido.{azul}\n")

    soma_linear, iteracoes_linear = linearMethod(numero)
    soma_best, iteracoes_best = bestmethod(numero)

    diferenca_bruta = iteracoes_linear - iteracoes_best
    porcentagem_diferenca = (diferenca_bruta / iteracoes_linear) * 100

    os.system('cls')
    print(f"Número: {numero}\n")
    print(f"Soma das divisões{azul} de {dourado}{numero}{azul} é: {dourado}{soma_linear}{azul} pelo {dourado}LinearMethod{azul} com {dourado}{iteracoes_linear} iterações{azul}.\n")
    print(f"Soma das divisões de {dourado}{numero}{azul} é: {dourado}{soma_best}{azul} pelo {dourado}BestMethod{azul} com {dourado}{iteracoes_best} iterações!{azul}\n")
    print(f"A diferença é de {dourado}{diferenca_bruta}{azul} iterações, ou seja, o {dourado}BestMethod{azul} foi {dourado}{porcentagem_diferenca:.2f}% mais rápido!{azul}\n")

while True:
    calcular()
    repetir = input(f"{dourado}Deseja calcular novamente? (s/n): {azul}").lower()
    if repetir != 's':
        break

os.system('cls')
print(f"{azul}Obrigado por usar o programa! Espero que tenha gostado.{dourado}\n")
