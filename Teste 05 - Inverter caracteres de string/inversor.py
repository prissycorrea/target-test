
#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(original):
    string_invertida = ""

    #IterAção sobre a string original do último caractere ao primeiro
    for i in range(len(original) - 1, -1, -1):
        string_invertida += original[i]

    return string_invertida

def deseja_continuar():
    """
    Pergunta ao usuário se deseja continuar invertendo novas strings.

    Retorna:
    - bool: True se o usuário deseja continuar, False caso contrário.
    """
    while True:
        resposta = input("Deseja inverter outra string? (s/n): ").strip().lower()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'não', 'nao']:
            return False
        else:
            print("Resposta inválida. Por favor, responda com 's' para sim ou 'n' para não.")

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    print("Programa para Inverter Strings")
    print("-" * 30)

    while True:
        #Recebendo a string do usuário
        string_original = input("Digite a string que deseja inverter: ")

        if not string_original:
            print("A string não pode estar vazia. Tente novamente.\n")
            continue

        #Invertendo a string
        string_invertida = inverter_string(string_original)

        print(f"String invertida: {string_invertida}\n")

        #Pergunta ao user se deseja continuar
        if not deseja_continuar():
            print("Programa encerrado. Até mais!")
            break
        else:
            print("-" * 30)

if __name__ == "__main__":
    main()
