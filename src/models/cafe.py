"""
Modelo para representação da cultura de Café
"""
from src.models.cultura import Cultura

class Cafe(Cultura):
    """
    Classe para representação da cultura de Café
    """
    def __init__(self, nome="Cafe"):
        """
        Inicializa uma cultura de Café
        
        Args:
            nome (str, optional): Nome da cultura. Padrão é "Café".
        """
        # Inicializa como cultura normal, sem tipo de plantio específico
        super().__init__(nome)
    
    def calcular_area(self, comprimento_rua=None, largura_rua=None, numero_ruas=None):
        """
        Método de compatibilidade para cálculo de área
        
        Args:
            comprimento_rua (float, optional): Comprimento de cada rua em metros
            largura_rua (float, optional): Largura de cada rua em metros
            numero_ruas (int, optional): Número de ruas
            
        Returns:
            float: Área calculada em metros quadrados
        """
        if comprimento_rua is not None and largura_rua is not None and numero_ruas is not None:
            return self.calcular_area_ruas(comprimento_rua, largura_rua, numero_ruas)
        return super().calcular_area()
