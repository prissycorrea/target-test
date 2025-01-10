#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def pertence_fibonacci(n):
    if n < 0:
        return False

    fib1, fib2 = 0, 1
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2

    return fib2 == n

#Entrada do usuário para receber o número a ser verificado
try:
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número válido.")