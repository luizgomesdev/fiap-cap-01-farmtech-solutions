"""
Modelo para representação de culturas agrícolas
"""

class Cultura:
    """
    Classe base para todas as culturas agrícolas
    """
    def __init__(self, nome, tipo_plantio):
        """
        Inicializa uma nova cultura
        
        Args:
            nome (str): Nome da cultura (ex: "Café", "Soja")
            tipo_plantio (str): Tipo de plantio da cultura (ex: "Ruas", "Talhões")
        """
        self.nome = nome
        self.tipo_plantio = tipo_plantio
        self.area_m2 = 0
        self.insumos = []
    
    def calcular_area(self):
        """
        Método abstrato para cálculo de área.
        Deve ser implementado nas classes filhas.
        
        Returns:
            float: Área calculada em metros quadrados
        """
        raise NotImplementedError("Este método deve ser implementado nas subclasses")
    
    def adicionar_insumo(self, insumo):
        """
        Adiciona um insumo à cultura
        
        Args:
            insumo (Insumo): Objeto insumo a ser adicionado
        """
        self.insumos.append(insumo)
    
    def remover_insumo(self, indice):
        """
        Remove um insumo da cultura pelo índice
        
        Args:
            indice (int): Índice do insumo a ser removido
            
        Returns:
            bool: True se removido com sucesso, False caso contrário
        """
        if 0 <= indice < len(self.insumos):
            del self.insumos[indice]
            return True
        return False
    
    def calcular_total_insumos(self):
        """
        Calcula a quantidade total de cada insumo necessário para a área
        
        Returns:
            dict: Dicionário com o total de cada insumo
        """
        totais = {}
        for insumo in self.insumos:
            quantidade_total = insumo.calcular_quantidade_total(self.area_m2)
            totais[insumo.nome] = {
                'quantidade': quantidade_total,
                'unidade': insumo.unidade
            }
        return totais
    
    def __str__(self):
        """
        Representação em string da cultura
        
        Returns:
            str: Descrição da cultura
        """
        return f"Cultura: {self.nome} | Tipo: {self.tipo_plantio} | Área: {self.area_m2} m²"
