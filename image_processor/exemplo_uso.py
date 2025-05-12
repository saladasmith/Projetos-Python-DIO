from image_processor.processador import ProcessadorImagens

processador = ProcessadorImagens()
imagem = processador.carregar_imagem("foto.jpg")
imagem_pb = processador.converter_para_preto_e_branco(imagem)
processador.salvar_imagem(imagem_pb, "resultado.jpg")# Exemplo de uso do meu pacote de processamento de imagens
# Feito por um aluno iniciante

from image_processor.processador import ProcessadorImagens

# Cria uma instância do processador
meu_processador = ProcessadorImagens()

# Carrega uma imagem (substitua pelo caminho da sua imagem)
caminho_imagem = "minha_imagem.jpg"
minha_imagem = meu_processador.carregar_imagem(caminho_imagem)

if minha_imagem:
    # Mostra informações da imagem
    print(f"Tamanho original: {minha_imagem.size}")
    
    # Redimensiona a imagem
    largura_nova = 300
    imagem_redimensionada = meu_processador.redimensionar(minha_imagem, largura=largura_nova)
    print(f"Novo tamanho: {imagem_redimensionada.size}")
    
    # Converte para preto e branco
    imagem_pb = meu_processador.converter_para_preto_e_branco(imagem_redimensionada)
    
    # Salva a imagem processada
    meu_processador.salvar_imagem(imagem_pb, "resultados/imagem_processada.jpg")
    
    # Gira a imagem
    imagem_girada = meu_processador.girar_imagem(imagem_redimensionada, 45)
    meu_processador.salvar_imagem(imagem_girada, "resultados/imagem_girada.jpg")
    
    print("Processamento concluído! Verifique a pasta 'resultados' para ver as imagens processadas.")
else:
    print("Não foi possível carregar a imagem. Verifique o caminho e tente novamente.")
