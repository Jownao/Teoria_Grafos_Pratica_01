# Teoria dos Grafos Prática 01
 Trabalho prático referente a matéria de "Teoria dos Grafos" ministrada pelo professor Adolfo Pinto
 

|   Integrantes  |Johnny William                 |Paulo Vitor                  |
|----------------|-------------------------------|-----------------------------|

## Representação do Grafo
A representação do grafo em Python utilizando a biblioteca [NetworkX](https://networkx.org/) está contida no arquivo [grafo.py](https://github.com/Jownao/Teoria_Grafos_Pratica_01/blob/main/grafo.py).


## Inicialização do sistema.

Executando o arquivo [principal.py](https://github.com/Jownao/Teoria_Grafos_Pratica_01/blob/main/principal.py) o sistema é iniciado e um menu com opções é apresentado.

A opção "[1] - Ler arquivo" permite que as informações sobre o grafo sejam passadas através de um arquivo "txt".

O arquivo deve estar no mesmo diretório que o arquivo "principal" e não precisa ser digitada a extensão do mesmo, somente seu nome.

O arquivo deve apresentar a seguinte formatação:

A primeira linha é reservada para os vértices, com cada vértice sendo separado por vírgula.

Já a segunda linha fica com as arestas, onde os vértices adjacentes, e peso se o grafo for valorado, separados por traço e cada aresta separada por vírgula.

A opção "[2] - Digitar dados" permite que as informações sejam digitadas pelo usuário.

Onde os vértices devem ser separados por vírgula.

E para as arestas, os vértices adjacentes separados por traço juntamente com o peso, se possuir, e cada aresta separada por vírgula.

Exemplo de formatação:

Vertices:
```
v1, v2, v3
```
Arestas:
```
v1-v2, v1-v3, v2-v3
```
Arestas com peso:
```
v1-v2-10, v1-v3-15, v2-v3-5
```
