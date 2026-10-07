class BaseDeConhecimento:
    def __init__(self):
        self.fatos = []
        self.regras = []
    def adicionar_fato(self, fato):
        self.fatos.append(fato)
    def adicionar_regra(self, condicao, conclusao):
        self.regras.append((condicao, conclusao))

class SistemaEspecialista:
    def __init__(self, base_conhecimento):
        self.base_conhecimento = base_conhecimento

    def inferir(self):
        novos_fatos = True
        while novos_fatos:
            novos_fatos = False
            for condicao, conclusao in self.base_conhecimento.regras:
                if all(fato in self.base_conhecimento.fatos for fato in condicao):
                    if conclusao not in self.base_conhecimento.fatos:
                        self.base_conhecimento.fatos.append(conclusao)
                        novos_fatos = True

base = BaseDeConhecimento()

base.adicionar_fato("Febre Alta")
base.adicionar_fato("Tosse")

base.adicionar_regra(["Febre Alta", "Tosse"], "Possível Infecção Respiratória")
base.adicionar_regra(["infecção respiratória", "Dificuldade para Respirar"], "Possível pneumonia")

sistema = SistemaEspecialista(base)
sistema.inferir()

print("Fatos inferidos:")
print(base.fatos)