def procura_caixa(caixa_principal):
    vazia = 0
    pilha_caixa = main.box.cria_pilha_busca()
    while pilha_caixa is not vazia:
        caixa =  pilha_caixa.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha_caixa.append(item)
            elif item.e_uma_chave():
                print ("Achei a chave!")