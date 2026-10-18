TEMPO_TESTE_MIN = 12

# Zonas: (percentual mínimo, percentual máximo) da capacidade máxima
ZONAS = {
    "A1": (60, 70),
    "A2": (70, 80),
    "A3": (80, 90),
}


def formatar_tempo(segundos):
    minutos = int(segundos // 60)
    seg = round(segundos % 60)
    if seg == 60:  # evita resultados como 1:60
        minutos += 1
        seg = 0
    return f"{minutos}:{seg:02d}"


def ler_distancia():
    while True:
        entrada = input("Quantos metros o aluno nadou em 12 minutos? ").replace(",", ".")
        try:
            distancia = float(entrada)
        except ValueError:
            print("Valor inválido. Digite apenas números.")
            continue
        if distancia <= 0:
            print("A distância precisa ser maior que zero.")
            continue
        return distancia


# Entrada de dados
distancia_total = ler_distancia()

# Ritmo máximo (100% da capacidade) em segundos por 100 m
tempo_total_seg = TEMPO_TESTE_MIN * 60
ritmo_maximo = tempo_total_seg / distancia_total * 100

# Resultados
print(f"\nRitmo máximo (teste de 12 min): {formatar_tempo(ritmo_maximo)} por 100 m\n")

for zona, (perc_min, perc_max) in ZONAS.items():
    ritmo_rapido = ritmo_maximo / (perc_max / 100)
    ritmo_lento = ritmo_maximo / (perc_min / 100)
    print(f"Em {zona}, seu ritmo médio a cada 100 m é "
          f"de {formatar_tempo(ritmo_rapido)} a {formatar_tempo(ritmo_lento)}")