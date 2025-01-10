#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def pertence_fibonacci(n):
    if n < 0:
        return False

    fib1, fib2 = 0, 1
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2

    return fib2 == n

def deseja_continuar():
    while True:
        resposta = input("Deseja verificar outro número? (s/n): ").strip().lower()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'não', 'nao']:
            return False
        else:
            print("Resposta inválida. Por favor, responda com 's' para sim ou 'n' para não.")


def main():
    print("Programa para Verificar se um Número Pertence à Sequência de Fibonacci")
    print("-" * 70)

    while True:
        #Recebe a entrada do user
        entrada = input("Digite um número para verificar: ")

        try:
            numero = int(entrada)
            if pertence_fibonacci(numero):
                print(f"O número {numero} pertence à sequência de Fibonacci.\n")
            else:
                print(f"O número {numero} não pertence à sequência de Fibonacci.\n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.\n")
            continue

        #Pergunta ao user se deseja continuar
        if not deseja_continuar():
            print("Programa encerrado. Até mais!")
            break
        else:
            print("-" * 70)

if __name__ == "__main__":
    main()