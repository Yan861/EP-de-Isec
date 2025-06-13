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

def hill(n,c,wordSegmenter):
    chaveCerta =''
    textoAberto=''

    print("rodando...")
    cifradoNumerico = utils.traduzir(c)
    chavesaux= utils.forcaBruta(n*n)
    chaves = utils.fabricaChavesMatriz(n,chavesaux)
    print(len(chaves))
    
    return chaveCerta, textoAberto

def main():

    

    # Defina o caminho para o seu arquivo de texto
    caminho_do_meu_corpus = 'textos_conhecidos/textos/avesso_da_pele.txt'

    # Gerar o dicionário de palavras
    dicionario_treinado = WordSegmenter.criar_dicionario_de_texto(caminho_do_meu_corpus)

    
    #monoalfabetica
    #file = open("textos_conhecidos\Cifrado\Mono\Grupo09_texto_cifrado.txt", "r")
    #chave , texto =mono(file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Mono\Grupo09_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)
    
    #vigenere
    #file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_20_texto_cifrado.txt", "r")
    #chave , texto = vigenere(20,file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_20_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)

    #file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_30_texto_cifrado.txt", "r")
    #chave , texto =vigenere(30,file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_30_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)

    #file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_40_texto_cifrado.txt", "r")
    #chave , texto =vigenere(40,file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_40_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)

    #file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_60_texto_cifrado.txt", "r")
    #chave , texto = vigenere(60,file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_60_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)

    #hill
    # file = open("textos_conhecidos\Cifrado\Hill\Grupo09_2_texto_cifrado.txt", "r")
    # chave , texto = hill(2,file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Hill\Grupo09_2_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)

    # file = open("textos_conhecidos\Cifrado\Hill\Grupo09_3_texto_cifrado.txt", "r")
    # chave , texto = hill(3,file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Hill\Grupo09_3_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)

    file = open("textos_conhecidos\Cifrado\Hill\Grupo09_4_texto_cifrado.txt", "r")
    chave , texto = hill(4,file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Hill\Grupo09_4_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)

    # file = open("textos_conhecidos\Cifrado\Hill\Grupo09_5_texto_cifrado.txt", "r")
    # chave , texto = hill(5,file.read(),dicionario_treinado)
    #file = open("textos_conhecidos\Aberto\Hill\Grupo09_5_texto_aberto.txt", "w")
    #file.write("chave: "+chave+"\ntexto:"+texto)

    file.close()
    #teste
    
main()