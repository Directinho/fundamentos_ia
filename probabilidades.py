probabilidades = {
    "HistoricoCompras": {0: 0.7, 1: 0.3},
    "tempoNoSite": {0: 0.6, 1: 0.4},
    "ClicouEmPromocao": {0: 0.8, 1: 0.2},
    "Compra": {
        (0, 0, 0): 0.1,
        (0, 0, 1): 0.3,
        (0, 1, 0): 0.2,
        (0, 1, 1): 0.6,
        (1, 0, 0): 0.4,
        (1, 0, 1): 0.8,
        (1, 1, 0): 0.8,
        (1, 1, 1): 0.9
    }
}

def calcular_probabilidade_compra(evidencias):
    historico = evidencias.get('HistoricoCompras')
    tempo = evidencias['tempoNoSite']
    promocao = evidencias['ClicouEmPromocao']

    prob_compra = probabilidades['Compra'][(historico, tempo, promocao)]
    prob_nao_compra = 1 - prob_compra 

    return {"Compras": prob_compra, "NaoCompras": prob_nao_compra}

evidencias = {'HistoricoCompras': 1, 'tempoNoSite': 0, 'ClicouEmPromocao': 1}

resultados = calcular_probabilidade_compra(evidencias)
print("Probabilidade de Compra:")
for resultado, probabilidade in resultados.items():
    print(f"{resultado}: {probabilidade:.2f}")