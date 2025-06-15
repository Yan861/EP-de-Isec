import re
import unidecode

def segmentar_string_sem_espaco(texto_sem_espaco, dicionario_conhecido):
    """
    Segmenta a string sem espaços usando Programação Dinâmica.
    Retorna uma lista de segmentos válidos ou None se não for possível segmentar.
    """
    if isinstance(texto_sem_espaco, list):
        # Junta a lista em uma string
        texto_sem_espaco = ''.join(texto_sem_espaco)

    texto_sem_espaco = texto_sem_espaco.lower()
    n = len(texto_sem_espaco)

    # dp[i] guarda a segmentação válida da string até o índice i
    dp = [None] * (n + 1)
    dp[0] = []  # Base da recursão: uma lista vazia para o início da segmentação

    for i in range(1, n + 1):
        for j in range(i):
            palavra = texto_sem_espaco[j:i]
            if palavra in dicionario_conhecido and dp[j] is not None:
                dp[i] = dp[j] + [palavra]
                break  # Se encontrou uma segmentação válida, pode parar

    return dp[n]  # Retorna a segmentação final se possível

def criar_dicionario_de_texto(caminho_do_arquivo):
    palavras_do_corpus = set()
    try:
        with open(caminho_do_arquivo, 'r', encoding='iso-8859-1') as f:
            texto = f.read()
            texto = texto.lower()
            # Remove pontuação e caracteres não alfanuméricos, substituindo por espaço
            texto_limpo = re.sub(r'[^\w\s]', ' ', texto)
            palavras = [palavra for palavra in texto_limpo.split() if palavra]
            for palavra in palavras:
                palavras_do_corpus.add(unidecode.unidecode(palavra))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        return set()
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return set()
    return palavras_do_corpus

