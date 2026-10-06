import heapq

class Produto:
    def __init__(self, nome, categoria, conversao_probabilidade):
        self.nome = nome
        self.categoria = categoria
        self.conversao_probabilidade = conversao_probabilidade

    def __repr__(self):
        return f"{self.nome} ({self.categoria})"

    def __lt__(self, outro):
        return self.nome < outro.nome


class AStarRecommendation:
    def __init__(self, produtos, heuristica):
        self.produtos = produtos
        self.heuristica = heuristica
        self.grafo = self.criar_grafo()

    def criar_grafo(self):
        grafo = {}
        for produto in self.produtos:
            grafo[produto] = [p for p in self.produtos if p != produto]
        return grafo

    def a_star(self, inicio, objetivo):
        fila_prioridade = []
        
        # Padrão consistente: (f, g, elemento)
        g_inicial = 0
        f_inicial = g_inicial + self.heuristica(inicio)
        heapq.heappush(fila_prioridade, (f_inicial, g_inicial, inicio))
        
        visitados = set()
        caminhos = {}

        while fila_prioridade:
            _, g, atual = heapq.heappop(fila_prioridade)
            
            if atual in visitados:
                continue
            visitados.add(atual)
            
            if atual == objetivo:
                break
                
            for vizinho in self.grafo[atual]:
                if vizinho not in visitados:
                    h = self.heuristica(vizinho)
                    novo_g = g + 1
                    novo_f = novo_g + h
                    heapq.heappush(fila_prioridade, (novo_f, novo_g, vizinho))
                    
                    if vizinho not in caminhos:
                        caminhos[vizinho] = atual

        caminho = []
        produto = objetivo
        while produto in caminhos:
            caminho.insert(0, produto)
            produto = caminhos[produto]
        
        if caminho or inicio == objetivo:
            caminho.insert(0, inicio)
            
        return caminho


def heuristica(produto):
    return -produto.conversao_probabilidade

produtos = [
    Produto("Xbox One", "Console", 0.8),
    Produto("PlayStation 4", "Console", 0.7),
    Produto("Nintendo Switch", "Portatil", 0.9),
    Produto("Nintendo 3DS", "Portatil", 0.6),
]

recomendador = AStarRecommendation(produtos, heuristica)

inicio = produtos[0]
objetivo = produtos[2]

caminho_recomendado = recomendador.a_star(inicio, objetivo)

print("Caminho recomendado:")
for p in caminho_recomendado:
    print(p)