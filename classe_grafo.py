import networkx as nx
import matplotlib.pyplot as plt

class Grafo():
    def __init__(self, vertices, arestas, digrafo, valorado, grafo):
        self.vertices = vertices
        self.arestas = arestas
        self.digrafo = digrafo
        self.valorado = valorado
        self.G = grafo
    
    @staticmethod
    def definir_grafo():
        while True:
            digrafo = int(input("O grafo é direcionado?\n[0] - NÃO\n[1] - SIM:\n"))
            if digrafo == 0 or digrafo == 1:
                digrafo = bool(digrafo)
                break
            else:
                print("*"*10+"Opção invalida! Por favor, digite novamente!"+"*"*10)
        while True:
            valorado = int(input("O grafo é valorado?\n[0] - NÃO\n[1] - SIM:\n"))
            if valorado == 0 or valorado == 1:
                valorado = bool(valorado)
                break
            else:
                print("*"*10+"Opção invalida! Por favor, digite novamente!"+"*"*10)
        print("Informe os vértices do grafo, separados por vírgula!\nEx: v1,v2,,...,vn\n")
        entrada_vertices = list(input().split(','))
        vertices = []
        for vertice in entrada_vertices:
            vertices.append(vertice.strip())
        if digrafo:
            print("A ordem de entrada dos vértices influencia.")
        if valorado:
            print("Informe os par de vértices adjacentes e peso separados por traços e cada aresta deve ser separada por vírgula."
            "\nEx: v1-v2-1,v1-v3-2,..., vn-vm-n\n")
        else:
            print("Informe os par de vértices adjacentes separados por traços e cada aresta deve ser separada por vírgula."
            "\nEx: v1-v2,v1-v3,..., vn-vm\n")
        entrada_arestas = list(input().split(","))
        lista_arestas = []
        arestas = []
        for elemento in entrada_arestas:
            lista_arestas.append(elemento.split("-"))
        if valorado:
            for i in range(len(lista_arestas)):
                peso = {"weight": lista_arestas[i][2]}
                aresta = lista_arestas[i][0].strip(), lista_arestas[i][1].strip(), peso
                arestas.append(aresta)
        else:
            for i in range(len(lista_arestas)):
                aresta = lista_arestas[i][0].strip(), lista_arestas[i][1].strip()
                arestas.append(aresta)
        if not digrafo:
            G = nx.Graph()
        else:
            G = nx.DiGraph()
        G.add_nodes_from(vertices)
        G.add_edges_from(arestas)
        return Grafo(vertices, arestas, digrafo, valorado, G)
    
    @staticmethod
    def ler_grafo(arquivo):
        while True:
            digrafo = int(input("O grafo é direcionado?\n[0] - NÃO\n[1] - SIM:\n"))
            if digrafo == 0 or digrafo == 1:
                digrafo = bool(digrafo)
                break
            else:
                print("*"*10+"Opção invalida! Por favor, digite novamente!"+"*"*10)
        while True:
            valorado = int(input("O grafo é valorado?\n[0] - NÃO\n[1] - SIM:\n"))
            if valorado == 0 or valorado == 1:
                valorado = bool(valorado)
                break
            else:
                print("*"*10+"Opção invalida! Por favor, digite novamente!"+"*"*10)
        vertices = []
        arestas = []
        lista_arestas = []
        grafo = open(arquivo, "r")
        for indice, linha in enumerate(grafo):
            if indice == 0:
                entrada = linha.split(',')
                for vertice in entrada:
                    vertices.append(vertice.strip())
            else:
                entrada = linha.split(',')
                for elemento in entrada:
                    lista_arestas.append(elemento.split("-"))
        grafo.close()
        if valorado:
            for i in range(len(lista_arestas)):
                peso = {"weight": lista_arestas[i][2]}
                aresta = lista_arestas[i][0].strip(), lista_arestas[i][1].strip(), peso
                arestas.append(aresta)
        else:
            for i in range(len(lista_arestas)):
                lista_arestas[i]
                aresta = lista_arestas[i][0].strip(), lista_arestas[i][1].strip()
                arestas.append(aresta)
        if not digrafo:
            G = nx.Graph()
        else:
            G = nx.DiGraph()
        G.add_nodes_from(vertices)
        G.add_edges_from(arestas)
        return Grafo(vertices, arestas, digrafo, valorado, G)
    
    #Métodos Básicos.
    #Regular.
    def ehRegular(self):
        regular = True
        graus = []
        for v, g in self.G.degree:
            graus.append(g)
            if g != graus[0]:
                regular = False
        return regular
    
    #Completo.
    def ehCompleto(self):
        completo = True
        for v, g in self.G.degree:
            if g != len(self.vertices) - 1:
                completo = False
        return completo
    
    #Conexo.
    
    
    #Algoritmos de busca.
    #Em largura.
    
    
    #Em profundidade.
    def busca_em_profundidade(self, vertice_origem="-"):
        if vertice_origem == "-":
            vertice = self.vertices[0]
        else:
            vertice = vertice_origem
        adjacentes = [(vertice, list(adjacencias)) for vertice, adjacencias in self.G.adjacency()]
        caminho = []
        nao_visitados = self.vertices.copy()
        while nao_visitados:
            pilha = []
            visitados = []
            visitados.append(vertice)
            pilha.append(vertice)
            while pilha:
                posicao = len(pilha) - 1
                u = pilha[posicao]
                for v, a in adjacentes:
                    if v == pilha[0] and v in nao_visitados:
                        nao_visitados.remove(v)
                        for va in a:
                            if va not in visitados:
                                pilha.append(va)
                                visitados.append(va)
                pilha.pop(0)
            caminho.append(visitados)
            if len(pilha) == 0 and len(nao_visitados) > 0:
                vertice = nao_visitados[0]
        return caminho