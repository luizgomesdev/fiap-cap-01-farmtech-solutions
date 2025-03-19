"""
Módulo para gerenciamento do menu interativo da aplicação
"""
from src.utils.menus.culturas_menu import menu_culturas
from src.utils.menus.areas_menu import menu_calculo_area
from src.utils.menus.insumos_menu import menu_insumos
from src.utils.menus.sobre_menu import exibir_sobre, exportar_dados

def exibir_menu_principal():
    """
    Exibe o menu principal da aplicação e gerencia a interação do usuário
    """
    while True:
        print("\n" + "-"*40)
        print("MENU PRINCIPAL".center(40))
        print("-"*40)
        print("[1] Gestão de Culturas")
        print("[2] Cálculo de Área Plantada")
        print("[3] Manejo de Insumos")
        print("[4] Exportar Dados para Análise")
        print("[5] Sobre o Sistema")
        print("[0] Sair")
        print("-"*40)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 0:
                print("\nSaindo do sistema...")
                break
            elif opcao == 1:
                menu_culturas()
            elif opcao == 2:
                menu_calculo_area()
            elif opcao == 3:
                menu_insumos()
            elif opcao == 4:
                exportar_dados()
            elif opcao == 5:
                exibir_sobre()
            else:
                print("\n❌ Opção inválida! Por favor, tente novamente.")
        except ValueError:
            print("\n❌ Entrada inválida! Digite apenas números.")
