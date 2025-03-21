"""
Módulo para cálculo de área plantada
"""
from src.models.cafe import Cafe
from src.models.soja import Soja
from src.utils.menus.culturas_menu import culturas

def menu_calculo_area():
    """
    Menu para cálculo de área
    """
    while True:
        print("\n" + "-"*40)
        print("CÁLCULO DE ÁREA PLANTADA".center(40))
        print("-"*40)
        print("[1] Calcular Área por Ruas (Retangulares)")
        print("[2] Calcular Área por Talhões (Quadrados)")
        print("[0] Voltar ao Menu Principal")
        print("-"*40)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 0:
                return
            elif opcao == 1:
                calcular_area_ruas()
            elif opcao == 2:
                calcular_area_talhoes()
            else:
                print("\n❌ Opção inválida! Por favor, tente novamente.")
        except ValueError:
            print("\n❌ Entrada inválida! Digite apenas números.")

def calcular_area_ruas():
    """
    Calcula a área plantada baseada em ruas retangulares para qualquer tipo de cultura
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas. Por favor, cadastre uma cultura primeiro.")
        return
    
    print("\n" + "-"*40)
    print("CÁLCULO DE ÁREA POR RUAS".center(40))
    print("-"*40)
    
    # Listar todas as culturas disponíveis
    print("Culturas disponíveis:")
    for i, cultura in enumerate(culturas):
        print(f"[{i+1}] {cultura.nome}")
    
    try:
        indice = int(input("\nEscolha a cultura (0 para cancelar): ")) - 1
        
        if indice == -1:
            print("\nOperação cancelada.")
            return
        
        if 0 <= indice < len(culturas):
            cultura = culturas[indice]
            
            print("-"*40)
            print(f"Calculando área para: {cultura.nome}")
            print("Fórmula: Área = Comprimento da rua × Largura da rua × Número de ruas")
            print("-"*40)
            
            comprimento = float(input("\nComprimento de cada rua (metros): "))
            largura = float(input("Largura de cada rua (metros): "))
            num_ruas = int(input("Número de ruas: "))
            
            if comprimento <= 0 or largura <= 0 or num_ruas <= 0:
                print("\n❌ Os valores devem ser maiores que zero!")
                return
                
            area_total = cultura.calcular_area_ruas(comprimento, largura, num_ruas)
            
            print("\n" + "-"*40)
            print("RESULTADOS".center(40))
            print("-"*40)
            print(f"Área total calculada: {area_total:.2f} m²")
            print(f"Comprimento de cada rua: {comprimento:.2f} m")
            print(f"Largura de cada rua: {largura:.2f} m")
            print(f"Número de ruas: {num_ruas}")
            print("-"*40)
            
            print(f"\n✅ Área atualizada para a cultura '{cultura.nome}'!")
        else:
            print("\n❌ Índice inválido!")
            
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")
        
    input("\nPressione ENTER para continuar...")

def calcular_area_talhoes():
    """
    Calcula a área plantada baseada em talhões quadrados para qualquer tipo de cultura
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas. Por favor, cadastre uma cultura primeiro.")
        return
    
    print("\n" + "-"*40)
    print("CÁLCULO DE ÁREA POR TALHÕES".center(40))
    print("-"*40)
    
    # Listar todas as culturas disponíveis
    print("Culturas disponíveis:")
    for i, cultura in enumerate(culturas):
        print(f"[{i+1}] {cultura.nome}")
    
    try:
        indice = int(input("\nEscolha a cultura (0 para cancelar): ")) - 1
        
        if indice == -1:
            print("\nOperação cancelada.")
            return
        
        if 0 <= indice < len(culturas):
            cultura = culturas[indice]
            
            print("-"*40)
            print(f"Calculando área para: {cultura.nome}")
            print("Fórmula: Área = Lado × Lado × Número de talhões")
            print("-"*40)
            
            lado = float(input("\nTamanho do lado do talhão (metros): "))
            num_talhoes = int(input("Número de talhões [padrão: 1]: ") or 1)
            
            if lado <= 0 or num_talhoes <= 0:
                print("\n❌ Os valores devem ser maiores que zero!")
                return
                
            area_total = cultura.calcular_area_talhoes(lado, num_talhoes)
            
            print("\n" + "-"*40)
            print("RESULTADOS".center(40))
            print("-"*40)
            print(f"Área total calculada: {area_total:.2f} m²")
            print(f"Tamanho de cada talhão: {lado:.2f} m × {lado:.2f} m")
            print(f"Área por talhão: {lado*lado:.2f} m²")
            print(f"Número de talhões: {num_talhoes}")
            print("-"*40)
            
            print(f"\n✅ Área atualizada para a cultura '{cultura.nome}'!")
        else:
            print("\n❌ Índice inválido!")
            
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")
        
    input("\nPressione ENTER para continuar...")
"""
Módulo para cálculo de área plantada
"""
from src.models.cafe import Cafe
from src.models.soja import Soja
from src.utils.menus.culturas_menu import culturas

def menu_calculo_area():
    """
    Menu para cálculo de área
    """
    while True:
        print("\n" + "-"*40)
        print("CÁLCULO DE ÁREA PLANTADA".center(40))
        print("-"*40)
        print("[1] Calcular Área por Ruas (Retangulares)")
        print("[2] Calcular Área por Talhões (Quadrados)")
        print("[0] Voltar ao Menu Principal")
        print("-"*40)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 0:
                return
            elif opcao == 1:
                calcular_area_ruas()
            elif opcao == 2:
                calcular_area_talhoes()
            else:
                print("\n❌ Opção inválida! Por favor, tente novamente.")
        except ValueError:
            print("\n❌ Entrada inválida! Digite apenas números.")

def calcular_area_ruas():
    """
    Calcula a área plantada baseada em ruas retangulares para qualquer tipo de cultura
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas. Por favor, cadastre uma cultura primeiro.")
        return
    
    print("\n" + "-"*40)
    print("CÁLCULO DE ÁREA POR RUAS".center(40))
    print("-"*40)
    
    # Listar todas as culturas disponíveis
    print("Culturas disponíveis:")
    for i, cultura in enumerate(culturas):
        print(f"[{i+1}] {cultura.nome}")
    
    try:
        indice = int(input("\nEscolha a cultura (0 para cancelar): ")) - 1
        
        if indice == -1:
            print("\nOperação cancelada.")
            return
        
        if 0 <= indice < len(culturas):
            cultura = culturas[indice]
            
            print("-"*40)
            print(f"Calculando área para: {cultura.nome}")
            print("Fórmula: Área = Comprimento da rua × Largura da rua × Número de ruas")
            print("-"*40)
            
            comprimento = float(input("\nComprimento de cada rua (metros): "))
            largura = float(input("Largura de cada rua (metros): "))
            num_ruas = int(input("Número de ruas: "))
            
            if comprimento <= 0 or largura <= 0 or num_ruas <= 0:
                print("\n❌ Os valores devem ser maiores que zero!")
                return
                
            area_total = cultura.calcular_area_ruas(comprimento, largura, num_ruas)
            
            print("\n" + "-"*40)
            print("RESULTADOS".center(40))
            print("-"*40)
            print(f"Área total calculada: {area_total:.2f} m²")
            print(f"Comprimento de cada rua: {comprimento:.2f} m")
            print(f"Largura de cada rua: {largura:.2f} m")
            print(f"Número de ruas: {num_ruas}")
            print("-"*40)
            
            print(f"\n✅ Área atualizada para a cultura '{cultura.nome}'!")
        else:
            print("\n❌ Índice inválido!")
            
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")
        
    input("\nPressione ENTER para continuar...")

def calcular_area_talhoes():
    """
    Calcula a área plantada baseada em talhões quadrados para qualquer tipo de cultura
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas. Por favor, cadastre uma cultura primeiro.")
        return
    
    print("\n" + "-"*40)
    print("CÁLCULO DE ÁREA POR TALHÕES".center(40))
    print("-"*40)
    
    # Listar todas as culturas disponíveis
    print("Culturas disponíveis:")
    for i, cultura in enumerate(culturas):
        print(f"[{i+1}] {cultura.nome}")
    
    try:
        indice = int(input("\nEscolha a cultura (0 para cancelar): ")) - 1
        
        if indice == -1:
            print("\nOperação cancelada.")
            return
        
        if 0 <= indice < len(culturas):
            cultura = culturas[indice]
            
            print("-"*40)
            print(f"Calculando área para: {cultura.nome}")
            print("Fórmula: Área = Lado × Lado × Número de talhões")
            print("-"*40)
            
            lado = float(input("\nTamanho do lado do talhão (metros): "))
            num_talhoes = int(input("Número de talhões [padrão: 1]: ") or 1)
            
            if lado <= 0 or num_talhoes <= 0:
                print("\n❌ Os valores devem ser maiores que zero!")
                return
                
            area_total = cultura.calcular_area_talhoes(lado, num_talhoes)
            
            print("\n" + "-"*40)
            print("RESULTADOS".center(40))
            print("-"*40)
            print(f"Área total calculada: {area_total:.2f} m²")
            print(f"Tamanho de cada talhão: {lado:.2f} m × {lado:.2f} m")
            print(f"Área por talhão: {lado*lado:.2f} m²")
            print(f"Número de talhões: {num_talhoes}")
            print("-"*40)
            
            print(f"\n✅ Área atualizada para a cultura '{cultura.nome}'!")
        else:
            print("\n❌ Índice inválido!")
            
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")
        
    input("\nPressione ENTER para continuar...")
