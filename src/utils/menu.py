"""
Módulo para gerenciamento do menu interativo da aplicação
"""

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

def menu_culturas():
    """
    Menu para gestão de culturas
    """
    print("\n" + "-"*40)
    print("GESTÃO DE CULTURAS".center(40))
    print("-"*40)
    print("[1] Cadastrar Nova Cultura")
    print("[2] Listar Culturas")
    print("[3] Atualizar Cultura")
    print("[4] Remover Cultura")
    print("[0] Voltar ao Menu Principal")
    print("-"*40)
    
    try:
        opcao = int(input("\nEscolha uma opção: "))
        
        if opcao == 0:
            return
        elif opcao == 1:
            print("\n➕ Função para cadastrar cultura será implementada.")
        elif opcao == 2:
            print("\n📋 Função para listar culturas será implementada.")
        elif opcao == 3:
            print("\n✏️ Função para atualizar cultura será implementada.")
        elif opcao == 4:
            print("\n❌ Função para remover cultura será implementada.")
        else:
            print("\n❌ Opção inválida! Por favor, tente novamente.")
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")

def menu_calculo_area():
    """
    Menu para cálculo de área
    """
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
            print("\n☕ Função para calcular área de café será implementada.")
        elif opcao == 2:
            print("\n🌾 Função para calcular área de soja será implementada.")
        else:
            print("\n❌ Opção inválida! Por favor, tente novamente.")
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")

def menu_insumos():
    """
    Menu para manejo de insumos
    """
    print("\n" + "-"*40)
    print("MANEJO DE INSUMOS".center(40))
    print("-"*40)
    print("[1] Cadastrar Insumo")
    print("[2] Calcular Quantidade de Insumos")
    print("[3] Listar Insumos Cadastrados")
    print("[0] Voltar ao Menu Principal")
    print("-"*40)
    
    try:
        opcao = int(input("\nEscolha uma opção: "))
        
        if opcao == 0:
            return
        elif opcao == 1:
            print("\n➕ Função para cadastrar insumo será implementada.")
        elif opcao == 2:
            print("\n🧮 Função para calcular quantidade de insumos será implementada.")
        elif opcao == 3:
            print("\n📋 Função para listar insumos será implementada.")
        else:
            print("\n❌ Opção inválida! Por favor, tente novamente.")
    except ValueError:
        print("\n❌ Entrada inválida! Digite apenas números.")

def exportar_dados():
    """
    Função para exportar dados para análise em R
    """
    print("\n📊 Função para exportar dados será implementada.")

def exibir_sobre():
    """
    Exibe informações sobre o sistema
    """
    print("\n" + "-"*60)
    print("SOBRE O SISTEMA".center(60))
    print("-"*60)
    print("FarmTech Solutions - Aplicação para Agricultura Digital")
    print("Versão: 1.0.0")
    print("Desenvolvido para fazendas em Minas Gerais")
    print("Suporte para culturas de café e soja")
    print("\nDesenvolvido por:")
    print("- Nome 1 (Líder de Projeto)")
    print("- Nome 2 (Desenvolvedor Python)")
    print("- Nome 3 (Analista de Dados em R)")
    print("- Nome 4 (Documentação e Versionamento)")
    print("-"*60)
