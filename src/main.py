import os
from PIL import Image, ImageFilter, ImageEnhance

class ImagemProcessadora:
    def __init__(self):
        self.imagens = {}

    def carregar_imagem(self, nome_arquivo):
        try:
            return Image.open(nome_arquivo)
        except Exception as e:
            print(f"Imagem não encontrada: {e}")
            return None

    def aplicar_filtro_cinza(self, imagem):
        return imagem.convert('L')

    def aplicar_filtro_invertido(self, imagem):
        return imagem.point(lambda x: 255 - x)

    def aplicar_filtro_desenho(self, imagem):
        return imagem.filter(ImageFilter.FIND_EDGES)

    def redimensionar_imagem(self, imagem, largura, altura):
        return imagem.resize((largura, altura))

    def salvar_imagem(self, imagem, nome_arquivo):
        try:
            imagem.save(nome_arquivo)
            print(f"Imagem salva com sucesso: {nome_arquivo}")
        except Exception as e:
            print(f"Falha ao salvar imagem: {e}")

if __name__ == "__main__":
    processadora = ImagemProcessadora()
    
    # Carregar imagem
    nome_arquivo = "imagem.jpg"
    imagem = processadora.carregar_imagem(nome_arquivo)
    
    if imagem is not None:
        # Aplicar filtro cinza
        imagem_cinza = processadora.aplicar_filtro_cinza(imagem.copy())
        processadora.salvar_imagem(imagem_cinza, "imagem_cinza.jpg")
        
        # Aplicar filtro invertido
        imagem_invertida = processadora.aplicar_filtro_invertido(imagem.copy())
        processadora.salvar_imagem(imagem_invertida, "imagem_invertida.jpg")
        
        # Redimensionar a imagem
        largura = 500
        altura = 375
        imagem_redimensionada = processadora.redimensionar_imagem(imagem.copy(), largura, altura)
        processadora.salvar_imagem(imagem_redimensionada, "imagem_redimensionada.jpg")