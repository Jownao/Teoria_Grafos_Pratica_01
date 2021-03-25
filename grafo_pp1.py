
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
  def __init__(self, digrafo, valorado, vertices, arestas, grafo):
    self.vertices = vertices
    self.arestas = arestas
    self.digrafo = digrafo
    self.valorado = valorado
    self.G = grafo
  
  @staticmethod
  def definir_grafo():
    digrafo = bool(int(input("O grafo é direcionado?\n[0] - NÃO\n[1] - SIM:\n")))
    print("_"*50)
    
    valorado = bool(int(input("O grafo é valorado?\n[0] - NÃO\n[1] - SIM:\n")))
    print("_"*50)
    
    print("Informe os vértices do grafo, separados por vírgula!\nEx: v1,v2,,...,vn\n")
    entrada_vertices = list(input().upper().split(','))
    vertices = []
    for vertice in entrada_vertices:
      vertices.append(vertice.strip())
    print("_"*50)
    
    if digrafo:
      print("A ordem de entrada dos vértices influência.")
    
    if valorado:
      print("Informe os par de vértices adjacentes e peso separados por traços e cada aresta deve ser separada por vírgula."
      "\nEx: v1-v2-1,v1-v3-2,..., vn-vm-n\n")
    else:
      print("Informe os par de vértices adjacentes separados por traços e cada aresta deve ser separada por vírgula."
      "\nEx: v1-v2,v1-v3,..., vn-vm\n")
    entrada_arestas = list(input().upper().split(","))
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
    print("_"*50)

    if not digrafo:
      G = nx.Graph()
    else:
      G = nx.DiGraph()
    G.add_nodes_from(vertices)
    G.add_edges_from(arestas)
    
    return Grafo(digrafo, valorado, vertices, arestas, G)
    
  def informacoes(self):
    print("informações sobre o grafo.")
    print("_"*25,"\nVértices.")
    for vertice in self.vertices:
      print(f"\'{vertice}\'",end=" ")
    print()
    print("_"*25,"\nArestas.")
    if not self.valorado:
      for v_ini, v_fim in self.arestas:
        print(f"\'{v_ini} - {v_fim}\'")
    else:
      for v_ini, v_fim, peso in self.arestas:
        print(f"\'{v_ini} - {v_fim} - {peso}\'")
    print()
    print("_"*25,f"\nDigrafo: {self.digrafo}")
    print("_"*25,f"\nValorado: {self.valorado}")
    print("_"*25,f"\nRegular: {self.ehRegular()}")
    print("_"*25,f"\nCompleto: {self.ehCompleto()}")
    print("_"*25,f"\nConexo: {self.ehConexo()}")
    print("_"*25)
    self.imprimir_grafo()
  
  def vertices_adjacentes(self):
    return [(vertice, list(adjacencias)) for vertice, adjacencias in self.G.adjacency()]
  
  def grau_vertices(self):
    return [(len(adjacencias)) for vertice, adjacencias in self.G.adjacency()]

  def ehRegular(self):
    graus = self.grau_vertices()
    regular = True
    for i in range(len(graus)):
      if graus[i] != graus[0]:
        regular = False
    return regular
  
  def ehCompleto(self):
    completo = True
    for grau in self.grau_vertices():
      if grau != len(self.vertices) - 1:
        completo = False
    return completo
  
  def ehConexo(self):
    conexo = True
    for vertice in self.vertices:
      if vertice not in self.busca_em_largura():
        conexo = False
    return conexo
  
  def busca_em_largura(self, vertice_origem="-"):
    if vertice_origem == "-":
      vertice = self.vertices[0]
    else:
      vertice = vertice_origem
    fila = []
    visitados = []
    fila.append(vertice)
    visitados.append(vertice)
    while len(fila) > 0:
      u = fila[0]
      for v, ad in self.vertices_adjacentes():
        for p in ad:
          if p not in visitados:
            fila.append(p)
            visitados.append(p)
      fila.pop()
    return visitados
  
  def busca_em_profundidade(self, vertice_origem="-"):
    if vertice_origem == "-":
      vertice = self.vertices[0]
    else:
      vertice = vertice_origem
    pilha = []
    visitados = []
    pilha.append(vertice)
    visitados.append(vertice)
    while len(pilha) > 0:
      posicao = len(pilha)-1
      u = pilha[posicao]
      for v, ad in self.vertices_adjacentes():
        for p in ad:
          if p not in visitados:
            pilha.append(p)
            visitados.append(p)
      pilha.pop(len(pilha)-1)
    return visitados

  def imprimir_grafo(self):
    plt.figure(1)
    nx.draw_networkx(self.G, pos=nx.spring_layout(self.G))
    plt.show()

"""#Testes."""

#vertices: a, b, c, d, e
#arestas: a-b, a-c , c-d, d-b
#-----------------------------
#vertices: v1, v2, v3
#arestas: v1-v2, v1-v3, v2-v3
#-----------------------------
#vertices: v1, v2, v3, v4, v5
#arestas: v1-v2, v2-v3, v3-v4, v4-v5, v5-v1, v2-v4
#-------------------------------------------------
#vertices: A, B, C, D, E, F, G, H, I, J, K, L
#arestas: A-B, A-C, B-C, B-E, B-F, C-D, C-F, D-G, E-F, E-I, E-J, F-G, F-J, F-K, G-H, G-L, H-L, I-J, J-K

grafo = Grafo.definir_grafo()

grafo.informacoes()

grafo.busca_em_profundidade()

grafo.busca_em_largura()