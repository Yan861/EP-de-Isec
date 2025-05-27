import utils

alfabeto = utils.alfabeto
#cifra monoalfabetica
def mono(c):
    chaveCerta =''
    textoAberto=''

    cifradoNumerico=utils.traduzir(c)
    chaves = utils.forcaBruta()
    
    return chaveCerta, textoAberto

#cifra de vigenere
#n é o tamanho da chave
def vigenere(n,c):
    chaveCerta =''
    textoAberto=''

    cifradoNumerico=utils.traduzir(c)
    chaves = utils.forcaBruta(n)
    
    return chaveCerta, textoAberto

def hill(n,c):
    chaveCerta =''
    textoAberto=''

    print("rodando...")
    cifradoNumerico = utils.traduzir(c)
    chavesaux= utils.forcaBruta(n*n)
    print("rodando...")
    chaves = utils.fabricaChavesMatriz(n,chavesaux)
    
    return chaveCerta, textoAberto

def main():
    #monoalfabetica
    file = open("textos_conhecidos\Cifrado\Mono\Grupo09_texto_cifrado.txt", "r")
    chave , texto =mono(file.read())
    file = open("textos_conhecidos\Aberto\Mono\Grupo09_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)
    #vigenere
    file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_20_texto_cifrado.txt", "r")
    chave , texto = vigenere(20,file.read())
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_20_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)

    file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_30_texto_cifrado.txt", "r")
    chave , texto =vigenere(30,file.read())
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_30_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)

    file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_40_texto_cifrado.txt", "r")
    chave , texto =vigenere(40,file.read())
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_40_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)

    file = open("textos_conhecidos\Cifrado\Vigenere\Grupo09_60_texto_cifrado.txt", "r")
    chave , texto = vigenere(60,file.read())
    file = open("textos_conhecidos\Aberto\Vigenere\Grupo09_60_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)

    #hill
    file = open("textos_conhecidos\Cifrado\Hill\Grupo09_2_texto_cifrado.txt", "r")
    chave , texto = hill(2,file.read())
    file = open("textos_conhecidos\Aberto\Hill\Grupo09_2_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)

    file = open("textos_conhecidos\Cifrado\Hill\Grupo09_3_texto_cifrado.txt", "r")
    chave , texto = hill(3,file.read())
    file = open("textos_conhecidos\Aberto\Hill\Grupo09_3_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)

    file = open("textos_conhecidos\Cifrado\Hill\Grupo09_4_texto_cifrado.txt", "r")
    chave , texto = hill(4,file.read())
    file = open("textos_conhecidos\Aberto\Hill\Grupo09_4_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)

    file = open("textos_conhecidos\Cifrado\Hill\Grupo09_5_texto_cifrado.txt", "r")
    chave , texto = hill(5,file.read())
    file = open("textos_conhecidos\Aberto\Hill\Grupo09_5_texto_aberto.txt", "w")
    file.write("chave: "+chave+"\ntexto:"+texto)

    file.close()
    #teste
    hill(2,"aaabba")

