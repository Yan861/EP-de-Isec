import numpy as np
import itertools as it
from math import ceil
import WordSegmenter

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#traduzir de letra para numero
def traduzir(palavra):
    traducao =[]
    lista= list(palavra)
    for item in lista: 
        traducao.append(alfabeto.index(item))
    return traducao

#traduzir de numero pra letra
def traduzirNumero(numeros):
    traducao = []
    for numero in numeros:
        traducao.append(alfabeto[numero])
    return traducao
def forcaBruta(dicionario,n=None):
    possibilidades = it.combinations_with_replacement(alfabeto,n)
    
    chaves=[]
    for possibilidade in possibilidades:
        aux=''.join(possibilidade)
        if(WordSegmenter.segmentar_string_sem_espaco(aux,dicionario)):
            chaves.append(possibilidade)
    return chaves
# cifra de vigenere

def inversoAditivo(list):
    listaInversa=[]
    for element in list:
        listaInversa.append((26-element)%26)
    return listaInversa
# cifra de hill
def determinanteMatriz(list):
    matriz = np.array(list)
    return np.linalg.det(matriz)

def inversoMultiplicativo(number: int):
    result =0
    for i in range(26):
        result=(number*i)%26
        if(result ==1): return i
    return -1

def matrizCortada(matriz, i,j):
    m = np.array(matriz)
    r = []

    for line in range(len(matriz)):
        aux =[]
        if(line != i):
            for column in range(len(matriz)):
                if(column !=j): aux.append(m[line][column])
            r.append(aux)
    return r

def fabricaChavesMatriz(n, list):
    result = []
    for chave in list:
        matrizAux = np.zeros((n,n))
        it =0
        #fazendo a matriz
        for i in range(len(matrizAux)):
            for j in range(len(matrizAux)):
                matrizAux[i][j]=chave[it]
                it+=1
        #testando se a matriz é invertivel, se for adicionamos as chaves possiveis
        if(determinanteMatriz(matrizAux)!=0):
            result.append(matrizAux)
    
    return result
#deus me perdoe pelo que eu to fazendo nesse metodo
def inverterMatriz(list):
    matriz = np.array(list)

    det = determinanteMatriz(matriz)
    inv =inversoMultiplicativo(det)
    
    result = np.zeros(matriz.shape)
    if(inv==-1): return result
    for line in range(len(list)):
        for column in range(len(list)):
            aux = matrizCortada(matriz,line,column)
            detAux= determinanteMatriz(aux)

            result[line][column] = (int)(detAux*inv)%26 

    
    return result


def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )
def multiplicarMatriz(matriz1, matriz2):
    result = np.matmul(matriz1, matriz2)
    for i in range(len(result)):
        for j in range(len(result)):
            result[i][j]=result[i][j]%26
    return result
#teste 


