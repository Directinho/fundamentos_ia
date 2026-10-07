import numpy as np
from scipy.stats import norm
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

model = BayesianNetwork([
    ('HistoricoCompras', 'Compra'),
    ('tempoNoSite', 'Compra'),
    ('ClicouEmPromocao', 'Compra')
])

cpd_historico = TabularCPD(variable='HistoricoCompras', variable_card=2, values=[[0.7], [0.3]])
cpd_tempo = TabularCPD(variable='tempoNoSite', variable_card=2, values=[[0.6], [0.4]])
cpd_promocao = TabularCPD(variable='ClicouEmPromocao', variable_card=2, values=[[0.8], [0.2]])

cpd_compra = TabularCPD(
    variable='Compra',
    variable_card=2,
    values=[
        [0.9, 0.6, 0.7, 0.1, 0.8, 0.3, 0.4, 0.05],
        [0.1, 0.4, 0.3, 0.9, 0.2, 0.7, 0.6, 0.95]
    ],
    evidence=['HistoricoCompras', 'tempoNoSite', 'ClicouEmPromocao'],
    evidence_card=[2, 2, 2]
)

model.add_cpds(cpd_historico, cpd_tempo, cpd_promocao, cpd_compra)

assert model.check_model(), "O modelo não é válido"

from pgmpy.inference import VariableElimination

inference = VariableElimination(model)
result = inference.query(variables=['Compra'], evidence={'HistoricoCompras': 1, 'tempoNoSite': 0, 'ClicouEmPromocao': 1})

print("Probabilidade de Compra:")
print(result)

media_tempo = 5
desvio_padrao_tempo = 2
tempo_observado = 6
prob_tempo = norm.cdf(tempo_observado, loc=media_tempo, scale=desvio_padrao_tempo)
print(f"Probabilidade de o cliente passar menos de {tempo_observado} minutos no site: {prob_tempo:.2f}")