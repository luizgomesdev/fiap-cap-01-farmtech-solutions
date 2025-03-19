"""
Módulo para cálculo de área plantada
"""
from src.models.cafe import Cafe
from src.models.soja import Soja

def menu_calculo_area():
    """
    Menu para cálculo de área
    """
    while True:
        print("\n" + "-"*40)
        print("CÁLCULO DE ÁREA PLANTADA".center(40))
        print("-"*40)
        print("[1] Calcular Área para Café (Ruas)")
        print("[2] Calcular Área para Soja (Talhões)")
        print("[0] Voltar ao Menu Principal")
        print("-"*40)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 0:
                return
            elif opcao == 1:
                calcular_area_cafe()
            elif opcao == 2:
                calcular_area_soja()
            else:
                print("\n❌ Opção inválida! Por favor, tente novamente.")
        except ValueError:
            print("\n❌ Entrada inválida! Digite apenas números.")

def calcular_area_cafe():
    """
    Calcula a área plantada de café baseada em ruas retangulares
    """
    print("\n" + "-"*40)
    print("CÁLCULO DE ÁREA PARA CAFÉ".center(40))
    print("-"*40)
    print("Fórmula: Área = Comprimento da rua × Largura da rua × Número de ruas")
    print("-"*40)
    
    try:
        comprimento = float(input("\nComprimento de cada rua (metros): "))
        largura = float(input("Largura de cada rua (metros): "))
        num_ruas = int(input("Número de ruas: "))
        
        if comprimento <= 0 or largura <= 0 or num_ruas <= 0:
            print("\n❌ Os valores devem ser maiores que zero!")
            return
            
        cafe = Cafe()
        area_total = cafe.calcular_area(comprimento, largura, num_ruas)
        
        print("\n" + "-"*40)
        print("RESULTADOS".center(40))
        print("-"*40)
        print(f"Área total calculada: {area_total:.2f} m²")
        print(f"Comprimento de cada rua: {comprimento:.2f} m")
        print(f"Largura de cada rua: {largura:.2f} m")
        print(f"Número de ruas: {num_ruas}")
        print("-"*40)
        
        input("\nPressione ENTER para continuar...")
        
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")

def calcular_area_soja():
    """
    Calcula a área plantada de soja baseada em talhões quadrados
    """
    print("\n" + "-"*40)
    print("CÁLCULO DE ÁREA PARA SOJA".center(40))
    print("-"*40)
    print("Fórmula: Área = Lado × Lado × Número de talhões")
    print("-"*40)
    
    try:
        lado = float(input("\nTamanho do lado do talhão (metros): "))
        num_talhoes = int(input("Número de talhões [padrão: 1]: ") or 1)
        
        if lado <= 0 or num_talhoes <= 0:
            print("\n❌ Os valores devem ser maiores que zero!")
            return
            
        soja = Soja()
        area_total = soja.calcular_area(lado, num_talhoes)
        
        print("\n" + "-"*40)
        print("RESULTADOS".center(40))
        print("-"*40)
        print(f"Área total calculada: {area_total:.2f} m²")
        print(f"Tamanho de cada talhão: {lado:.2f} m × {lado:.2f} m")
        print(f"Área por talhão: {lado*lado:.2f} m²")
        print(f"Número de talhões: {num_talhoes}")
        print("-"*40)
        
        input("\nPressione ENTER para continuar...")
        
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")
