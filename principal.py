import classe_grafo

while True:
    opcao = int(input("Escolha entre uma das opçoes!"+
                      "\n[1] - Ler arquivo."+
                      "\n[2] - Digitar dados."+
                      "\n[3] - Imprimir informaçoes gerais sobre o grafo."+
                      "\n[4] - É regular?"+
                      "\n[5] - É completo?"+
                      "\n[6] - É conexo?"+
                      "\n[7] - Busca em largura!"+
                      "\n[8] - Busca em profundidade!"+
                      "\n[9] - Menor caminho!"
                      "\n[0] - Sair.\n"))
    if opcao >= 0 and opcao <= 9:
        if opcao == 1:
            arquivo = input("Digite o nome do arquivo!\n")
            grafo = classe_grafo.Grafo.ler_grafo(arquivo+".txt")
        elif opcao == 2:
            grafo = classe_grafo.Grafo.definir_grafo()
        elif opcao == 3:
            grafo.informacoes()
        elif opcao == 4:
            print("Regular: ", grafo.ehRegular())
        elif opcao == 5:
            print("Completo: ", grafo.ehCompleto())
        elif opcao == 6:
            print("Conexo: ", grafo.ehConexo())
        elif opcao == 7:
            print("Busca em largura.")
            vo = grafo.vertice_origem()
            print(grafo.busca_em_largura(vo))
        elif opcao == 8:
            print("Busca em profundidade.")
            vo = grafo.vertice_origem()
            print(grafo.busca_em_profundidade(vo))
        elif opcao == 9:
            print("Menor caminho - Método de Dijkstra.")
            vo = grafo.vertice_origem()
            grafo.dijkstra(vo)
        else:
            print("Fechando o sistema!")
            break
    else:
        print("Opção inválida! Por favor, tente novamente!")
