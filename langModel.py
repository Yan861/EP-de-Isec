import re

def criar_dicionario_de_texto(caminho_do_arquivo):
    """
    Cria um dicionário (conjunto de palavras) a partir de um arquivo de texto.

    Args:
        caminho_do_arquivo (str): O caminho para o arquivo de texto.

    Returns:
        set: Um conjunto de palavras únicas extraídas do texto, em minúsculas.
             Retorna um set vazio se o arquivo não puder ser lido.
    """
    palavras_do_corpus = set()
    try:
        with open(caminho_do_arquivo, 'r', encoding='iso-8859-1') as f:
            texto = f.read()

            # 1. Converter para minúsculas
            texto = texto.lower()

            # 2. Remover pontuação e caracteres especiais.
            #    O regex '[^\w\s]' busca por qualquer coisa que NÃO seja (^)
            #    um caractere de palavra (\w) ou um espaço em branco (\s).
            #    Ele substitui essas ocorrências por um espaço.
            texto_limpo = re.sub(r'[^\w\s]', ' ', texto)

            # 3. Dividir o texto em palavras e adicionar ao conjunto.
            #    Removemos strings vazias que podem surgir do split (ex: múltiplos espaços)
            palavras = [palavra for palavra in texto_limpo.split() if palavra]

            for palavra in palavras:
                palavras_do_corpus.add(palavra)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_do_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

    return palavras_do_corpus

# --- Exemplo de Uso ---

# Defina o caminho para o seu arquivo de texto
nome_do_arquivo_corpus = 'textos_conhecidos/textos/avesso_da_pele.txt'

# 1. Crie o dicionário de palavras a partir do arquivo
meu_dicionario_gerado = criar_dicionario_de_texto(nome_do_arquivo_corpus)

if meu_dicionario_gerado: # Verifica se o dicionário não está vazio (indicando erro de leitura)
    print("Dicionário de palavras gerado:")
    print(sorted(list(meu_dicionario_gerado))) # Imprime em ordem alfabética para facilitar a visualização

    # 2. Reutilize a função do modelo de linguagem do exemplo anterior
    def criar_modelo_linguagem_basico(palavras_conhecidas):
        """
        Cria uma função que atua como um modelo de linguagem básico.
        (Copiado do exemplo anterior para demonstração completa)
        """
        dicionario_conhecido = {palavra.lower() for palavra in palavras_conhecidas}

        def reconhecer_e_validar(texto):
            palavras_no_texto = re.sub(r'[^\w\s]', ' ', texto.lower()).split()
            palavras_desconhecidas = []

            for palavra in palavras_no_texto:
                if palavra and palavra not in dicionario_conhecido: # Garante que a palavra não é vazia
                    palavras_desconhecidas.append(palavra)

            if palavras_desconhecidas:
                return f"Erro: Palavras desconhecidas encontradas: {', '.join(palavras_desconhecidas)}"
            else:
                return "Todas as palavras são reconhecidas."

        return reconhecer_e_validar

    # 3. Crie a instância do modelo de linguagem com o novo dicionário
    modelo_com_corpus = criar_modelo_linguagem_basico(meu_dicionario_gerado)

    # 4. Teste o modelo
    print("\n--- Testando o modelo com o dicionário gerado ---")
    frase_teste_1 = "vai parar de morrer"
    frase_teste_2 = "O cachorro azul latiu para o carro."
    frase_teste_3 = "Um novo termo que não existe no texto inicial."

    print(f"Frase 1: '{frase_teste_1}'")
    print(modelo_com_corpus(frase_teste_1))
    print("-" * 30)

    print(f"Frase 2: '{frase_teste_2}'")
    print(modelo_com_corpus(frase_teste_2))
    print("-" * 30)

    print(f"Frase 3: '{frase_teste_3}'")
    print(modelo_com_corpus(frase_teste_3))
    print("-" * 30)
else:
    print("Não foi possível gerar o dicionário. Verifique o caminho do arquivo ou o conteúdo.")
