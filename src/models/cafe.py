"""
Modelo para representação da cultura de Café
"""
from src.models.cultura import Cultura

class Cafe(Cultura):
    """
    Classe para representação da cultura de Café, com cálculo de área específico
    baseado em ruas retangulares
    """
    def __init__(self, nome="Café"):
        """
        Inicializa uma cultura de Café
        
        Args:
            nome (str, optional): Nome da cultura. Padrão é "Café".
        """
        super().__init__(nome, "Ruas")
        self.comprimento_rua = 0
        self.largura_rua = 0
        self.numero_ruas = 0
    
    def calcular_area(self, comprimento_rua, largura_rua, numero_ruas):
        """
        Calcula a área plantada de café usando a fórmula:
        Área = Comprimento da rua × Largura da rua × Número de ruas
        
        Args:
            comprimento_rua (float): Comprimento de cada rua em metros
            largura_rua (float): Largura de cada rua em metros
            numero_ruas (int): Número de ruas
            
        Returns:
            float: Área calculada em metros quadrados
        """
        self.comprimento_rua = comprimento_rua
        self.largura_rua = largura_rua
        self.numero_ruas = numero_ruas
        self.area_m2 = comprimento_rua * largura_rua * numero_ruas
        return self.area_m2
    
    def __str__(self):
        """
        Representação em string da cultura de Café
        
        Returns:
            str: Descrição da cultura de Café
        """
        base_str = super().__str__()
        if self.comprimento_rua > 0:
            return f"{base_str} | {self.numero_ruas} ruas de {self.comprimento_rua}m x {self.largura_rua}m"
        return base_str
