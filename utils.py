import numpy as np

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#cifra monoalfabetica
def mono(k,c):
    c=m*k
    m=c*k-1
    
#cifra de vigenere


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

            result[line][column] = (int)(detAux*inv)%26 #agora ta no grau

    
    return result

#teste 
minha_matriz = np.array([[17,17,5],[21, 18,21],[2,2,19]])


print(inverterMatriz(minha_matriz))