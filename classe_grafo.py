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
    
    def imprimir_grafo(self):
        plt.figure(1)
        nx.draw_networkx(self.G, pos=nx.spring_layout(self.G))
        plt.show()
    
    def informacoes(self):
        print("-"*25,"\nVértices.")
        for vertice in self.vertices:
            print(f"\'{vertice}\'",end=" ")
        print()
        print("-"*25,"\nArestas.")
        if not self.valorado:
            for v_ini, v_fim in self.arestas:
                print(f"\'{v_ini} - {v_fim}\'")
        else:
            for v_ini, v_fim, peso in self.arestas:
                print(f"\'{v_ini} - {v_fim}",end=" - ")
            for key in peso:
                print(f"{peso[key]}\'")
        print()
        print("-"*25,f"\nDigrafo: {self.digrafo}")
        print("-"*25,f"\nValorado: {self.valorado}")
        print("-"*25,f"\nRegular: {self.ehRegular()}")
        print("-"*25,f"\nCompleto: {self.ehCompleto()}")
        print("-"*25,f"\nConexo: {self.ehConexo()}")
        print("-"*25)
        self.imprimir_grafo()
    
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
    def ehConexo(self):
        caminhos = self.busca_em_largura()
        conexo = True
        if len(caminhos) > 1:
            conexo = False
        return conexo
    
    #Algoritmos de busca.
    #Em largura.
    def busca_em_largura(self, vertice_origem = None):
        if vertice_origem == None:
            vertice = self.vertices[0]
        else:
            vertice = vertice_origem
        adjacentes = [(vertice, list(adjacencias)) for vertice, adjacencias in self.G.adjacency()]
        caminho = []
        nao_visitados = self.vertices.copy()
        while nao_visitados:
            fila = []
            visitados = []
            visitados.append(vertice)
            fila.append(vertice)
            while fila:
                u = fila[0]
                fila.remove(u)
                for v, a in adjacentes:
                    if v == u and v in nao_visitados:
                        nao_visitados.remove(v)
                        for va in a:
                            if va not in visitados:
                                fila.append(va)
                                visitados.append(va)
            caminho.append(visitados)
            if len(fila) == 0 and len(nao_visitados) > 0:
                vertice = nao_visitados[0]
        return caminho
    
    #Em profundidade.
    def busca_em_profundidade(self, vertice_origem = None):
        if vertice_origem == None:
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
    
    #Menor caminho - Djikstra.
    def dijkstra(self, vo = None):
        vertices = [(v) for v in self.G.nodes]
        distancias = [float('inf') for v in self.G.nodes]
        s = [('') for v in self.G.nodes]
        path = [('') for v in self.G.nodes]
        nao_visitados = [(v) for v in self.G.nodes]
        if vo == None:
            vertice_origem = vertices[0]
        else:
            vertice_origem = vo
        posicao = vertices.index(vertice_origem)
        distancias[posicao] = 0
        s[posicao] = 'x'
        path[posicao] = '-'
        nao_visitados.remove(vertice_origem)
        vertice_atual = vertice_origem
        for v in vertices:
            a, p = self.adjacentes_pesos(v)
            if len(a[0]) == 0 and v in nao_visitados:
                nao_visitados.remove(v)
        adjacentes, pesos = self.adjacentes_pesos(vertice_atual)
        if len(adjacentes[0]) > 0:
            while nao_visitados:
                adjacentes, pesos = self.adjacentes_pesos(vertice_atual)
                adj = []
                p = []
                for i, v in enumerate(adjacentes):
                    for j, va in enumerate(v):
                        if va in nao_visitados:
                            adj.append(adjacentes[0][j])
                            p.append(pesos[0][j])
                for i, va in enumerate(adj):
                    if distancias[vertices.index(va)] > distancias[vertices.index(vertice_atual)] + p[i]:
                        distancias[vertices.index(va)] = distancias[vertices.index(vertice_atual)] + p[i]
                        path[vertices.index(va)] = vertice_atual
                distancia_minima = float("inf")
                for v in nao_visitados:
                    posicao = vertices.index(v)
                    if distancias[posicao] < distancia_minima:
                        distancia_minima = distancias[posicao]
                        vertice_atual = v        
                posicao = vertices.index(vertice_atual)
                s[posicao] = "X"
                nao_visitados.remove(vertice_atual)
        print(f"Vértice de origem: {vertice_origem}")
        print('|','-'*61,'|')
        print("| Vértice\t|\tS\t| Distância\t|\tPath\t|")
        for i in range(len(vertices)):
            print(f"|\t{vertices[i]}\t|\t{s[i]}\t|\t{distancias[i]}\t|\t{path[i]}\t|")
        print('|','-'*61,'|')
    
    def adjacentes_pesos(self, vertice):
        adjacentes = []
        pesos = []
        for v, a in self.G.adjacency():
            if v == vertice:
                adjacentes.append(list(a.keys()))
                if self.valorado:
                    pesos.append(list(a.values()))
                else:
                    pesos.append([1] * len(a))
        return adjacentes, pesos
    
    def vertice_origem(self):
        while True:
            opcao = int(input("Deseja buscar um vértice específico?\n[0] - Não\n[1] - Sim\n"))
            if opcao == 0 or opcao == 1:
                break
            else:
                print("Opção inválida, por favor, tente novamente!")
        if opcao:
            while True:
                vertice = input("Informe o vértice: ")
                if vertice in self.vertices:
                    break
                else:
                    print("O vértice informado não está presente no grafo, por favor, informe outro!")
        else:
            vertice = None
        return vertice
