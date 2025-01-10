#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
import os

def carregar_dados(caminho_arquivo):
    """
    Carrega os dados de faturamento a partir de um arquivo JSON.

    Parâmetros:
    - caminho_arquivo (str): Caminho para o arquivo JSON.

    Retorna:
    - list: Lista de dicionários com os dados de faturamento.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não está no formato JSON válido.")
        return []

def calcular_estatisticas(dados):
    #Filtro p/ os dias com faturamento maior que 0
    faturamentos_validos = [dia['valor'] for dia in dados if dia['valor'] > 0]

    if not faturamentos_validos:
        print("Nenhum faturamento válido encontrado nos dados.")
        return

    #Cálculo do menor e maior faturamento
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)

    #Cálculo dA média mensal
    soma_faturamentos = sum(faturamentos_validos)
    media_faturamento = soma_faturamentos / len(faturamentos_validos)

    #Contagem dos dias com faturamento acima da média
    dias_acima_media = len([valor for valor in faturamentos_validos if valor > media_faturamento])

    #Print dos resultados
    print(f"Menor faturamento do mês: R${menor_faturamento:.2f}")
    print(f"Maior faturamento do mês: R${maior_faturamento:.2f}")
    print(f"Média de faturamento mensal: R${media_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

def main():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'data', 'dados.json')

    dados = carregar_dados(caminho_arquivo)

    if dados:
        #Calcula e exibe as estatísticas
        calcular_estatisticas(dados)

if __name__ == "__main__":
    main()
