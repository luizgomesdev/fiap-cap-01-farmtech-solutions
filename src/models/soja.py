"""
Modelo para representação da cultura de Soja
"""
from src.models.cultura import Cultura

class Soja(Cultura):
    """
    Classe para representação da cultura de Soja
    """
    def __init__(self, nome="Soja"):
        """
        Inicializa uma cultura de Soja
        
        Args:
            nome (str, optional): Nome da cultura. Padrão é "Soja".
        """
        # Inicializa como cultura normal, sem tipo de plantio específico
        super().__init__(nome)
    
    def calcular_area(self, lado_talhao=None, numero_talhoes=None):
        """
        Método de compatibilidade para cálculo de área
        
        Args:
            lado_talhao (float, optional): Tamanho do lado do talhão em metros
            numero_talhoes (int, optional): Número de talhões
            
        Returns:
            float: Área calculada em metros quadrados
        """
        if lado_talhao is not None:
            # Garantir que numero_talhoes seja 1 se não for especificado
            if numero_talhoes is None:
                numero_talhoes = 1
            return self.calcular_area_talhoes(lado_talhao, numero_talhoes)
        return super().calcular_area()
