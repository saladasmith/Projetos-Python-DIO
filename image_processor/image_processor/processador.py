from PIL import Image
import os

class ProcessadorImagens:
    """
    Uma classe simples para processar imagens.
    Feito por um aluno iniciante em Python.
    """
    
    def carregar_imagem(self, caminho):
        """Carrega uma imagem do disco."""
        try:
            img = Image.open(caminho)
            print(f"Imagem carregada: {caminho}")
            return img
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            return None
    
    def salvar_imagem(self, imagem, caminho):
        """Salva a imagem no disco."""
        try:
            # Cria o diretório se não existir
            os.makedirs(os.path.dirname(caminho), exist_ok=True)
            
            imagem.save(caminho)
            print(f"Imagem salva em: {caminho}")
            return True
        except Exception as e:
            print(f"Erro ao salvar a imagem: {e}")
            return False
    
    def redimensionar(self, imagem, largura=None, altura=None):
        """Redimensiona a imagem."""
        if largura is None and altura is None:
            print("Por favor, especifique pelo menos largura ou altura.")
            return imagem
            
        # Calcula a proporção se apenas um dos valores for fornecido
        if largura and not altura:
            proporcao = largura / imagem.width
            altura = int(imagem.height * proporcao)
        elif altura and not largura:
            proporcao = altura / imagem.height
            largura = int(imagem.width * proporcao)
            
        return imagem.resize((largura, altura), Image.Resampling.LANCZOS)
    
    def converter_para_preto_e_branco(self, imagem):
        """Converte a imagem para preto e branco."""
        return imagem.convert('L')
    
    def girar_imagem(self, imagem, angulo):
        """Gira a imagem pelo ângulo especificado em graus."""
        return imagem.rotate(angulo, expand=True)
    
    def espelhar_imagem(self, imagem, horizontal=True):
        """Espelha a imagem horizontal ou verticalmente."""
        if horizontal:
            return imagem.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            return imagem.transpose(Image.FLIP_TOP_BOTTOM)
    
    def recortar_imagem(self, imagem, esquerda, superior, direita, inferior):
        """Recorta uma região retangular da imagem."""
        return imagem.crop((esquerda, superior, direita, inferior))
