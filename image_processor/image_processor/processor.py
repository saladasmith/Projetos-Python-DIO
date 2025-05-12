import cv2
import numpy as np
from PIL import Image, ImageFilter
from typing import Union, Tuple, Optional
import os

class ImageProcessor:
    """
    Classe para processamento de imagens com várias operações úteis.
    """
    
    @staticmethod
    def load_image(image_path: str) -> np.ndarray:
        """
        Carrega uma imagem do caminho especificado.
        
        Args:
            image_path (str): Caminho para o arquivo de imagem.
            
        Returns:
            np.ndarray: Imagem carregada como um array NumPy.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"O arquivo {image_path} não foi encontrado.")
            
        # Carrega a imagem usando OpenCV
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Não foi possível carregar a imagem de {image_path}")
            
        # Converte de BGR (padrão do OpenCV) para RGB
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    @staticmethod
    def save_image(image: np.ndarray, output_path: str) -> None:
        """
        Salva uma imagem no caminho especificado.
        
        Args:
            image (np.ndarray): Imagem a ser salva.
            output_path (str): Caminho onde a imagem será salva.
        """
        # Cria o diretório de saída se não existir
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Salva a imagem usando OpenCV
        cv2.imwrite(output_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    
    @staticmethod
    def to_grayscale(image: np.ndarray) -> np.ndarray:
        """
        Converte uma imagem colorida para tons de cinza.
        
        Args:
            image (np.ndarray): Imagem de entrada.
            
        Returns:
            np.ndarray: Imagem em tons de cinza.
        """
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    @staticmethod
    def resize(
        image: np.ndarray, 
        width: Optional[int] = None, 
        height: Optional[int] = None,
        scale: float = 1.0
    ) -> np.ndarray:
        """
        Redimensiona uma imagem.
        
        Args:
            image (np.ndarray): Imagem de entrada.
            width (int, optional): Nova largura desejada.
            height (int, optional): Nova altura desejada.
            scale (float, optional): Fator de escala. Se especificado, redimensiona a imagem por este fator.
            
        Returns:
            np.ndarray: Imagem redimensionada.
        """
        if scale != 1.0:
            return cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
            
        if width is None and height is None:
            return image.copy()
            
        if height is None:
            # Calcula a altura proporcional
            h, w = image.shape[:2]
            height = int((width / w) * h)
        elif width is None:
            # Calcula a largura proporcional
            h, w = image.shape[:2]
            width = int((height / h) * w)
            
        return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
    
    @staticmethod
    def rotate(image: np.ndarray, angle: float) -> np.ndarray:
        """
        Rotaciona uma imagem pelo ângulo especificado.
        
        Args:
            image (np.ndarray): Imagem de entrada.
            angle (float): Ângulo de rotação em graus.
            
        Returns:
            np.ndarray: Imagem rotacionada.
        """
        h, w = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(image, M, (w, h))
    
    @staticmethod
    def flip(image: np.ndarray, flip_code: int = 1) -> np.ndarray:
        """
        Inverte uma imagem horizontalmente, verticalmente ou ambos.
        
        Args:
            image (np.ndarray): Imagem de entrada.
            flip_code (int): 
                0 - Inverte verticalmente
                >0 - Inverte horizontalmente
                <0 - Inverte ambos os eixos
                
        Returns:
            np.ndarray: Imagem invertida.
        """
        return cv2.flip(image, flip_code)
    
    @staticmethod
    def apply_blur(image: np.ndarray, kernel_size: int = 5) -> np.ndarray:
        """
        Aplica um filtro de desfoque na imagem.
        
        Args:
            image (np.ndarray): Imagem de entrada.
            kernel_size (int): Tamanho do kernel para o desfoque (deve ser ímpar).
            
        Returns:
            np.ndarray: Imagem com desfoque aplicado.
        """
        if kernel_size % 2 == 0:
            kernel_size += 1  # Garante que o tamanho do kernel seja ímpar
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    
    @staticmethod
    def detect_edges(image: np.ndarray, threshold1: int = 100, threshold2: int = 200) -> np.ndarray:
        """
        Detecta bordas na imagem usando o algoritmo Canny.
        
        Args:
            image (np.ndarray): Imagem de entrada.
            threshold1 (int): Primeiro limiar para o procedimento de histerese.
            threshold2 (int): Segundo limiar para o procedimento de histerese.
            
        Returns:
            np.ndarray: Imagem com as bordas detectadas.
        """
        if len(image.shape) > 2:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image
        return cv2.Canny(gray, threshold1, threshold2)
    
    @staticmethod
    def adjust_brightness_contrast(
        image: np.ndarray, 
        alpha: float = 1.0, 
        beta: int = 0
    ) -> np.ndarray:
        """
        Ajusta o brilho e o contraste da imagem.
        
        Args:
            image (np.ndarray): Imagem de entrada.
            alpha (float): Fator de contraste (1.0 = sem alteração).
            beta (int): Valor a ser adicionado a cada pixel para ajuste de brilho.
            
        Returns:
            np.ndarray: Imagem com brilho e contraste ajustados.
        """
        return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
