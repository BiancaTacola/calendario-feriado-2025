import matplotlib.pyplot as plt
import holidays
import matplotlib
from collections import Counter
from datetime import date, timedelta
from dateutil.easter import easter

# Configuração para rodar em ambientes sem interface gráfica
matplotlib.use('Agg')


def calcular_feriados_moveis(year):
    """
    Calcula os feriados móveis do Brasil para o ano especificado.

    Args:
        year (int): Ano para calcular os feriados móveis.

    Returns:
        dict: Um dicionário com os feriados móveis.
    """
    feriados_moveis = {}
    pascoa = easter(year)
    carnaval = pascoa - timedelta(days=47)  # Carnaval: 47 dias antes da Páscoa
    # Sexta-feira Santa: 2 dias antes da Páscoa
    sexta_santa = pascoa - timedelta(days=2)
    # Corpus Christi: 60 dias após a Páscoa
    corpus_christi = pascoa + timedelta(days=60)

    feriados_moveis[carnaval] = "Carnaval"
    feriados_moveis[sexta_santa] = "Sexta-feira Santa"
    feriados_moveis[corpus_christi] = "Corpus Christi"

    return feriados_moveis


def plot_holidays(year, output_file):
    """
    Gera um gráfico mostrando o número de feriados por mês para o ano especificado.

    Args:
        year (int): Ano para calcular os feriados.
        output_file (str): Caminho para salvar o gráfico gerado.
    """
    # Obtém os feriados do Brasil para o ano especificado
    feriados = holidays.Brazil(years=year)

    # Adiciona os feriados móveis
    feriados.update(calcular_feriados_moveis(year))

    # Conta os feriados por mês
    feriados_por_mes = Counter(dt.month for dt in feriados.keys())

    # Nome dos meses
    nomes_meses = [date(year, i, 1).strftime('%b') for i in range(1, 13)]

    # Cria um gráfico de linha
    fig, ax = plt.subplots()
    ax.plot(nomes_meses, [feriados_por_mes.get(i, 0) for i in range(1, 13)],
            marker='o', color='red', linestyle='-')

    # Adiciona rótulos e título ao gráfico
    ax.set_xlabel('Mês')
    ax.set_ylabel('Número de Feriados')
    ax.set_title(f'Feriados por Mês no Ano {year}')

    # Ajusta o tamanho da fonte dos meses no eixo x
    plt.xticks(fontsize=8)

    # Salva o gráfico como uma imagem
    plt.savefig(output_file)
    print(f"Gráfico salvo em: {output_file}")

    # Exibe o gráfico (opcional)
    plt.show()


# Ano desejado
ano_desejado = 2025
# Caminho para salvar o gráfico
caminho_arquivo = 'calendario_2025.png'

# Gera o gráfico
plot_holidays(ano_desejado, caminho_arquivo)
