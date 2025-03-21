"""
Modelo para representação de culturas agrícolas
"""

class Cultura:
    """
    Classe base para todas as culturas agrícolas
    """
    def __init__(self, nome, tipo_plantio="Não definido"):
        """
        Inicializa uma nova cultura
        
        Args:
            nome (str): Nome da cultura (ex: "Café", "Soja")
            tipo_plantio (str, optional): Tipo de plantio informativo. Padrão é "Não definido".
        """
        self.nome = nome
        self.tipo_plantio = tipo_plantio  # Usado apenas para informação
        self.area_m2 = 0
        self.insumos = []
        
        # Dados para cálculo por ruas
        self.comprimento_rua = 0
        self.largura_rua = 0
        self.numero_ruas = 0
        
        # Dados para cálculo por talhões
        self.lado_talhao = 0
        self.numero_talhoes = 0
    
    def calcular_area(self):
        """
        Método genérico para cálculo de área.
        Retorna a área atual ou 0 se não calculada.
        
        Returns:
            float: Área calculada em metros quadrados
        """
        return self.area_m2
    
    def calcular_area_ruas(self, comprimento_rua, largura_rua, numero_ruas):
        """
        Calcula a área plantada usando a fórmula:
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
        self.tipo_plantio = "Ruas"  # Atualizado para informação
        self.area_m2 = comprimento_rua * largura_rua * numero_ruas
        return self.area_m2
    
    def calcular_area_talhoes(self, lado_talhao, numero_talhoes=1):
        """
        Calcula a área plantada usando a fórmula:
        Área = Lado × Lado × Número de talhões
        
        Args:
            lado_talhao (float): Tamanho do lado do talhão em metros
            numero_talhoes (int, optional): Número de talhões. Padrão é 1.
            
        Returns:
            float: Área calculada em metros quadrados
        """
        self.lado_talhao = lado_talhao
        self.numero_talhoes = numero_talhoes
        self.tipo_plantio = "Talhões"  # Atualizado para informação
        self.area_m2 = lado_talhao * lado_talhao * numero_talhoes
        return self.area_m2
    
    def adicionar_insumo(self, insumo):
        """
        Adiciona um insumo à cultura
        
        Args:
            insumo (Insumo): Objeto insumo a ser adicionado
        """
        # Verificar se o insumo já existe na cultura
        for i in self.insumos:
            if i.nome == insumo.nome and i.tipo == insumo.tipo:
                # Insumo já existe, não adiciona duplicado
                return
        
        # Adiciona o insumo se não for duplicado
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
        area_info = ""
        if self.area_m2 > 0:
            area_info = f" | Área: {self.area_m2} m²"
            if self.comprimento_rua > 0:
                area_info += f" | {self.numero_ruas} ruas de {self.comprimento_rua}m x {self.largura_rua}m"
            elif self.lado_talhao > 0:
                area_info += f" | {self.numero_talhoes} talhão(ões) de {self.lado_talhao}m × {self.lado_talhao}m"
        
        insumos_info = ""
        if self.insumos:
            insumos_info = f" | Insumos: {len(self.insumos)}"
        
        return f"Cultura: {self.nome}{area_info}{insumos_info}"
    
    def formatar_insumos(self):
        """
        Formata os insumos da cultura para exibição
        
        Returns:
            str: String formatada com os insumos e suas quantidades
        """
        if not self.insumos:
            return "Nenhum insumo cadastrado para esta cultura."
        
        if self.area_m2 <= 0:
            return "Área não definida. Impossível calcular insumos."
        
        resultado = []
        resultado.append(f"INSUMOS PARA {self.nome.upper()} ({self.area_m2:.2f} m²)")
        resultado.append("-" * 50)
        resultado.append(f"{'Insumo':<20} {'Tipo':<15} {'Total':<15}")
        resultado.append("-" * 50)
        
        for insumo in self.insumos:
            total = insumo.calcular_quantidade_total(self.area_m2)
            resultado.append(f"{insumo.nome:<20} {insumo.tipo:<15} {total:.2f} {insumo.unidade}")
        
        return "\n".join(resultado)
