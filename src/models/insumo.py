"""
Modelo para representação de insumos agrícolas
"""

class Insumo:
    """
    Classe para representação de insumos agrícolas como fertilizantes,
    defensivos, água, etc.
    """
    def __init__(self, nome, tipo, quantidade_por_m2, unidade):
        """
        Inicializa um novo insumo
        
        Args:
            nome (str): Nome do insumo (ex: "Fertilizante NPK")
            tipo (str): Tipo do insumo (ex: "Fertilizante", "Defensivo", "Água")
            quantidade_por_m2 (float): Quantidade necessária por metro quadrado
            unidade (str): Unidade de medida (ex: "kg", "L", "mL")
        """
        self.nome = nome
        self.tipo = tipo
        self.quantidade_por_m2 = quantidade_por_m2
        self.unidade = unidade
    
    def calcular_quantidade_total(self, area_m2):
        """
        Calcula a quantidade total do insumo necessária para uma área específica
        
        Args:
            area_m2 (float): Área em metros quadrados
            
        Returns:
            float: Quantidade total necessária
        """
        return self.quantidade_por_m2 * area_m2
    
    def __eq__(self, other):
        """
        Verifica se dois insumos são iguais comparando nome e tipo
        
        Args:
            other: Outro objeto para comparação
            
        Returns:
            bool: True se os insumos são considerados iguais
        """
        if not isinstance(other, Insumo):
            return False
        return (self.nome.lower() == other.nome.lower() and 
                self.tipo.lower() == other.tipo.lower())
    
    def __hash__(self):
        """
        Gera um hash único para o insumo baseado em nome e tipo
        
        Returns:
            int: Valor hash do insumo
        """
        return hash((self.nome.lower(), self.tipo.lower()))
    
    def __str__(self):
        """
        Representação em string do insumo
        
        Returns:
            str: Descrição do insumo
        """
        return f"{self.nome} ({self.tipo}) - {self.quantidade_por_m2} {self.unidade}/m²"
