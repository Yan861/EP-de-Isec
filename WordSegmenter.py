import re

def segmentar_string_sem_espaco(texto_sem_espaco, dicionario_conhecido):
    """
    Tenta segmentar uma string sem espaços em palavras conhecidas.
    Esta é uma implementação básica e pode não ser a mais eficiente ou robusta.
    """
    texto_sem_espaco = texto_sem_espaco.lower()
    segmentos_possiveis = []
    
    # Função recursiva para encontrar segmentos
    def encontrar_segmentos(indice_atual, caminho_atual):
        if indice_atual == len(texto_sem_espaco):
            segmentos_possiveis.append(caminho_atual)
            return

        for i in range(indice_atual + 1, len(texto_sem_espaco) + 1):
            palavra_candidata = texto_sem_espaco[indice_atual:i]
            if palavra_candidata in dicionario_conhecido:
                encontrar_segmentos(i, caminho_atual + [palavra_candidata])

    encontrar_segmentos(0, [])
    
    # Se houver múltiplos segmentos, escolher o mais longo ou com mais palavras
    if not segmentos_possiveis:
        return None # Não foi possível segmentar
    
    # Exemplo simples: escolher a segmentação com mais palavras
    melhor_segmento = []
    max_palavras = 0
    for segmento in segmentos_possiveis:
        if len(segmento) > max_palavras:
            max_palavras = len(segmento)
            melhor_segmento = segmento
            
    return " ".join(melhor_segmento) if melhor_segmento else None

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
                palavras_do_corpus.add(palavra)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        return set()
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return set()
    return palavras_do_corpus

# Caminho para o seu arquivo de corpus
caminho_do_meu_corpus = 'textos_conhecidos/textos/avesso_da_pele.txt'

# Gerar o dicionário de palavras
dicionario_treinado = criar_dicionario_de_texto(caminho_do_meu_corpus)

if dicionario_treinado:
    print("Dicionário de palavras gerado a partir do corpus:")
    print(sorted(list(dicionario_treinado)))
else:
    print("Não foi possível gerar o dicionário. Verifique o arquivo.")

# --- Exemplo de Uso ---
minhas_palavras = {
    "o", "a", "cachorro", "gato", "azul", "verde", "casa", "pequeno", "está", "na",
    "árvore", "flor", "linda", "um", "uma"
}

# 1. Preparar o dicionário (igual ao exemplo anterior)
dicionario_para_segmentacao = {palavra.lower() for palavra in minhas_palavras}

# 2. String sem espaços
string_sem_espaco_1 = "vaiparardemorrer"
string_sem_espaco_2 = "agataestanaarvore"
string_sem_espaco_3 = "eulindasfloras" # "floras" não está no dicionário
string_sem_espaco_4 = "estestringeteste"

print(f"Segmentando '{string_sem_espaco_1}':")
segmentado = segmentar_string_sem_espaco(string_sem_espaco_1, dicionario_treinado)
if segmentado:
    print(f"Resultado: '{segmentado}'")
else:
    print("Não foi possível segmentar completamente.")
print("-" * 30)

print(f"Segmentando '{string_sem_espaco_2}':")
segmentado = segmentar_string_sem_espaco(string_sem_espaco_2, dicionario_treinado)
if segmentado:
    print(f"Resultado: '{segmentado}'")
else:
    print("Não foi possível segmentar completamente.")
print("-" * 30)

print(f"Segmentando '{string_sem_espaco_3}':")
segmentado = segmentar_string_sem_espaco(string_sem_espaco_3, dicionario_treinado)
if segmentado:
    print(f"Resultado: '{segmentado}'")
else:
    print("Não foi possível segmentar completamente. (Esperado, 'eulindasfloras' não pode ser totalmente dividido)")
print("-" * 30)

print(f"Segmentando '{string_sem_espaco_4}':")
segmentado = segmentar_string_sem_espaco(string_sem_espaco_4, dicionario_treinado)
if segmentado:
    print(f"Resultado: '{segmentado}'")
else:
    print("Não foi possível segmentar completamente. (Esperado, 'estestringeteste' não é totalmente divisível pelo dicionário)")
print("-" * 30)