import utils
import WordSegmenter
alfabeto = utils.alfabeto
#cifra monoalfabetica
def mono(c,dicionario_treinado):
    chaveCerta =''
    textoAberto=''

    cifradoNumerico=utils.traduzir(c)
    chaves = utils.it.permutations(range(26))
    print(len(chaves))
    for chave in chaves:
        textoAberto=''
        for element in cifradoNumerico:
            textoAberto+=chave[element] #operação monoalfabetica
        segmentado = WordSegmenter.segmentar_string_sem_espaco(utils.traduzirNumero(textoAberto), dicionario_treinado)
        if(segmentado): #condição de parada
            chaveCerta=''.join(utils.traduzirNumero(chave))
            break
    return chaveCerta, textoAberto

#cifra de vigenere
#n é o tamanho da chave
def vigenere(n,c,dicionario_treinado):
    chaveCerta =''
    textoAberto=''

    cifradoNumerico=utils.traduzir(c)
    chaves = utils.forcaBruta(n)
    print(len(chaves))
    for chave in chaves:
        textoAberto=''
        i=0
        for element in cifradoNumerico:
            textoAberto+=(chave[i]+cifradoNumerico[i])%26
            i+=1
        segmentado = WordSegmenter.segmentar_string_sem_espaco(utils.traduzirNumero(textoAberto), dicionario_treinado)
        if(segmentado): #condição de parada
            chaveCerta=''.join(utils.traduzirNumero(utils.inversoAditivo(chave)))
            break
    return chaveCerta, textoAberto

def hill(n,c,dicionario_treinado):
    chaveCerta =''
    textoAberto=''

    print("rodando...")
    cifradoNumerico = utils.traduzir(c)
    matrizesCifradas=[]
    matrizesAux=utils.chunk_into_n(cifradoNumerico,n*n)
    for i in range(len(matrizesAux)):
        arr = utils.np.array(matrizesAux[i])
        matrix = arr.reshape(n, n)
        matrizesCifradas.append(matrix)

    print("rodando...")
    chavesaux= utils.forcaBruta(n*n)
    print("rodando...")
    chaves = utils.fabricaChavesMatriz(n,chavesaux)
    print(len(chaves))
    for chave in chaves:
        textoAberto=''
        resultado =[]
        for i in range(2):
            resultado.append(utils.multiplicarMatriz(chave,matrizesCifradas[i]))
        textoAberto=utils.np.concatenate((resultado[0],resultado[1], resultado[2]), axis=None)
        segmentado = WordSegmenter.segmentar_string_sem_espaco(utils.traduzirNumero(textoAberto), dicionario_treinado)
        if(segmentado):
            chaveCerta=''.join(utils.traduzirNumero(utils.inverterMatriz(chave)))
            break
    return chaveCerta, textoAberto

def main():

    

    # Defina o caminho para o seu arquivo de texto
    caminho_do_meu_corpus = 'textos_conhecidos/textos/avesso_da_pele.txt'

    # Gerar o dicionário de palavras
    dicionario_treinado = WordSegmenter.criar_dicionario_de_texto(caminho_do_meu_corpus)

    #textos conhecidos

    #monoalfabetica
    file = open("textos_conhecidos\Cifrado\Mono\Grupo09_texto_cifrado.txt", "r")
    chave , texto =mono(file.read(),dicionario_treinado)
    file.close()
    file = open("textos_conhecidos\Aberto\Mono\Grupo09_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()
    
    #vigenere
    file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_20_texto_cifrado.txt", "r")
    chave , texto = vigenere(20,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_20_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_30_texto_cifrado.txt", "r")
    chave , texto =vigenere(30,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_30_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_40_texto_cifrado.txt", "r")
    chave , texto =vigenere(40,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_40_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_60_texto_cifrado.txt", "r")
    chave , texto = vigenere(60,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_60_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    #hill
    file = open("textos_conhecidos\Cifrado\Hill\Grupo09_2_texto_cifrado.txt", "r")
    chave , texto = hill(2,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_conhecidos\Aberto\Hill\Grupo09_2_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    file = open("textos_conhecidos\Cifrado\Hill\Grupo09_3_texto_cifrado.txt", "r")
    chave , texto = hill(3,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_conhecidos\Aberto\Hill\Grupo09_3_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    # file = open("textos_conhecidos\Cifrado\Hill\Grupo09_4_texto_cifrado.txt", "r")
    # chave , texto = hill(4,file.read(),dicionario_treinado)
    #file.close()
    #file = open("textos_conhecidos\Aberto\Hill\Grupo09_4_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)
    #file.close()

    # file = open("textos_conhecidos\Cifrado\Hill\Grupo09_5_texto_cifrado.txt", "r")
    # chave , texto = hill(5,file.read(),dicionario_treinado)
    #file.close()
    #file = open("textos_conhecidos\Aberto\Hill\Grupo09_5_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)
    #file.close()

    #textos desconhecidos

    #monoalfabetica
    file = open("textos_desconhecidos\Cifrado\Mono\Grupo09_texto_cifrado.txt", "r")
    chave , texto =mono(file.read(),dicionario_treinado)
    file.close()
    file = open("textos_desconhecidos\Aberto\Mono\Grupo09_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    #vigenere
    file = open("textos_desconhecidos\Cifrado\Vigenere\Grupo09_20_texto_cifrado.txt", "r")
    chave , texto = vigenere(20,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_desconhecidos\Aberto\Vigenere\Grupo09_20_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()
    
    file = open("textos_desconhecidos\Cifrado\Vigenere\Grupo09_30_texto_cifrado.txt", "r")
    chave , texto =vigenere(30,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_desconhecidos\Aberto\Vigenere\Grupo09_30_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    file = open("textos_desconhecidos\Cifrado\Vigenere\Grupo09_40_texto_cifrado.txt", "r")
    chave , texto =vigenere(40,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_desconhecidos\Aberto\Vigenere\Grupo09_40_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    file = open("textos_desconhecidos\Cifrado\Vigenere\Grupo09_60_texto_cifrado.txt", "r")
    chave , texto = vigenere(60,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_60_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()
    
    #hill
    file = open("textos_desconhecidos\Cifrado\Hill\Grupo09_2_texto_cifrado.txt", "r")
    chave , texto = hill(2,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_desconhecidos\Aberto\Hill\Grupo09_2_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()

    file = open("textos_desconhecidos\Cifrado\Hill\Grupo09_3_texto_cifrado.txt", "r")
    chave , texto = hill(3,file.read(),dicionario_treinado)
    file.close()
    file = open("textos_desconhecidos\Aberto\Hill\Grupo09_3_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    file.close()
    
main()