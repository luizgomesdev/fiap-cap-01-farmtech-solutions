"""
Modelo para representação da cultura de Soja
"""
from src.models.cultura import Cultura

class Soja(Cultura):
    """
    Classe para representação da cultura de Soja, com cálculo de área específico
    baseado em talhões quadrados
    """
    def __init__(self, nome="Soja"):
        """
        Inicializa uma cultura de Soja
        
        Args:
            nome (str, optional): Nome da cultura. Padrão é "Soja".
        """
        super().__init__(nome, "Talhões")
        self.lado_talhao = 0
        self.numero_talhoes = 0
    
    def calcular_area(self, lado_talhao, numero_talhoes=1):
        """
        Calcula a área plantada de soja usando a fórmula:
        Área = Lado × Lado × Número de talhões
        
        Args:
            lado_talhao (float): Tamanho do lado do talhão em metros
            numero_talhoes (int, optional): Número de talhões. Padrão é 1.
            
        Returns:
            float: Área calculada em metros quadrados
        """
        self.lado_talhao = lado_talhao
        self.numero_talhoes = numero_talhoes
        self.area_m2 = lado_talhao * lado_talhao * numero_talhoes
        return self.area_m2
    
    def __str__(self):
        """
        Representação em string da cultura de Soja
        
        Returns:
            str: Descrição da cultura de Soja
        """
        base_str = super().__str__()
        if self.lado_talhao > 0:
            return f"{base_str} | {self.numero_talhoes} talhão(ões) de {self.lado_talhao}m × {self.lado_talhao}m"
        return base_str
