"""
Módulo para gerenciamento de insumos
"""
from src.models.insumo import Insumo
from src.utils.menus.culturas_menu import culturas

# Lista para armazenar os insumos em memória
insumos = [
    # Insumos para Café
    Insumo("NPK 20-5-20", "Fertilizante", 0.025, "kg"),
    Insumo("Calcário Dolomítico", "Fertilizante", 0.05, "kg"),
    Insumo("Fungicida Sistêmico", "Defensivo", 0.002, "L"),
    Insumo("Água de Irrigação", "Água/Irrigação", 3.5, "L"),
    
    # Insumos para Soja
    Insumo("NPK 4-30-10", "Fertilizante", 0.03, "kg"),
    Insumo("Inoculante Bradyrhizobium", "Biológico", 0.0015, "kg"),
    Insumo("Herbicida Glifosato", "Defensivo", 0.001, "L"),
    Insumo("Inseticida Piretróide", "Defensivo", 0.0008, "L"),
    Insumo("Micronutrientes", "Fertilizante", 0.01, "kg")
]

def menu_insumos():
    """
    Menu para manejo de insumos
    """
    while True:
        print("\n" + "-"*40)
        print("MANEJO DE INSUMOS".center(40))
        print("-"*40)
        print("[1] Cadastrar Insumo")
        print("[2] Calcular Quantidade de Insumos")
        print("[3] Listar Insumos Cadastrados")
        print("[4] Remover Insumo")
        print("[0] Voltar ao Menu Principal")
        print("-"*40)
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 0:
                return
            elif opcao == 1:
                cadastrar_insumo()
            elif opcao == 2:
                calcular_insumos()
            elif opcao == 3:
                listar_insumos()
            elif opcao == 4:
                remover_insumo()
            else:
                print("\n❌ Opção inválida! Por favor, tente novamente.")
        except ValueError:
            print("\n❌ Entrada inválida! Digite apenas números.")

def cadastrar_insumo():
    """
    Cadastra um novo insumo no sistema
    """
    print("\n" + "-"*40)
    print("CADASTRO DE INSUMO".center(40))
    print("-"*40)
    
    nome = input("Nome do insumo: ")
    
    print("\nTipos de insumo:")
    print("[1] Fertilizante")
    print("[2] Defensivo")
    print("[3] Água/Irrigação")
    print("[4] Outro")
    
    try:
        tipo_opcao = int(input("\nEscolha o tipo de insumo: "))
        if tipo_opcao == 1:
            tipo = "Fertilizante"
        elif tipo_opcao == 2:
            tipo = "Defensivo"
        elif tipo_opcao == 3:
            tipo = "Água/Irrigação"
        elif tipo_opcao == 4:
            tipo = input("Digite o tipo de insumo: ")
        else:
            print("\n❌ Opção inválida! Cadastro cancelado.")
            return
        
        quantidade_por_m2 = float(input("\nQuantidade por m² (ex: 0.5): "))
        
        print("\nUnidades disponíveis:")
        print("[1] kg (quilogramas)")
        print("[2] g (gramas)")
        print("[3] L (litros)")
        print("[4] mL (mililitros)")
        print("[5] Outra unidade")
        
        unidade_opcao = int(input("\nEscolha a unidade de medida: "))
        if unidade_opcao == 1:
            unidade = "kg"
        elif unidade_opcao == 2:
            unidade = "g"
        elif unidade_opcao == 3:
            unidade = "L"
        elif unidade_opcao == 4:
            unidade = "mL"
        elif unidade_opcao == 5:
            unidade = input("Digite a unidade de medida: ")
        else:
            print("\n❌ Opção inválida! Cadastro cancelado.")
            return
        
        # Verifica se o insumo já existe
        for insumo in insumos:
            if insumo.nome.lower() == nome.lower() and insumo.tipo.lower() == tipo.lower():
                print(f"\n❌ O insumo '{nome}' do tipo '{tipo}' já está cadastrado!")
                return
        
        # Cria e adiciona o novo insumo
        novo_insumo = Insumo(nome, tipo, quantidade_por_m2, unidade)
        insumos.append(novo_insumo)
        print(f"\n✅ Insumo '{nome}' cadastrado com sucesso!")
        
    except ValueError:
        print("\n❌ Entrada inválida! Cadastro cancelado.")

def listar_insumos():
    """
    Lista todos os insumos cadastrados
    """
    print("\n" + "-"*60)
    print("INSUMOS CADASTRADOS".center(60))
    print("-"*60)
    
    if not insumos:
        print("\n⚠️ Não há insumos cadastrados!")
        return
    
    print(f"{'#':<3} {'Nome':<20} {'Tipo':<15} {'Qtd/m²':<10} {'Unidade':<10}")
    print("-"*60)
    
    for i, insumo in enumerate(insumos):
        print(f"{i+1:<3} {insumo.nome:<20} {insumo.tipo:<15} {insumo.quantidade_por_m2:<10.4f} {insumo.unidade:<10}")
    
    print("-"*60)
    input("\nPressione ENTER para continuar...")

def remover_insumo():
    """
    Remove um insumo cadastrado
    """
    if not insumos:
        print("\n⚠️ Não há insumos cadastrados para remover!")
        return
        
    listar_insumos()
    
    try:
        indice = int(input("\nDigite o número do insumo que deseja remover (0 para cancelar): ")) - 1
        
        if indice == -1:
            print("\nOperação cancelada.")
            return
            
        if 0 <= indice < len(insumos):
            insumo_removido = insumos.pop(indice)
            print(f"\n✅ Insumo '{insumo_removido.nome}' removido com sucesso!")
        else:
            print("\n❌ Índice inválido!")
    except ValueError:
        print("\n❌ Entrada inválida! Remoção cancelada.")

def calcular_insumos():
    """
    Calcula a quantidade de insumos necessários para uma cultura
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas! Cadastre uma cultura primeiro.")
        return
    
    if not insumos:
        print("\n⚠️ Não há insumos cadastrados! Cadastre um insumo primeiro.")
        return
    
    print("\n" + "-"*60)
    print("CÁLCULO DE INSUMOS".center(60))
    print("-"*60)
    
    print("Culturas disponíveis:")
    for i, cultura in enumerate(culturas):
        print(f"[{i+1}] {cultura}")
    
    try:
        cultura_indice = int(input("\nEscolha a cultura para o cálculo (0 para cancelar): ")) - 1
        
        if cultura_indice == -1:
            print("\nOperação cancelada.")
            return
            
        if 0 <= cultura_indice < len(culturas):
            cultura_selecionada = culturas[cultura_indice]
            
            # Verificar se a cultura tem área definida
            if cultura_selecionada.area_m2 <= 0:
                print(f"\n⚠️ A cultura '{cultura_selecionada.nome}' não possui área definida!")
                
                if isinstance(cultura_selecionada, type) and hasattr(cultura_selecionada, 'calcular_area'):
                    print("\nVocê precisa calcular a área da cultura primeiro.")
                    print("Vá ao menu 'Cálculo de Área Plantada' para definir a área.")
                    return
                else:
                    area = float(input("\nDigite a área em m² para esta cultura: "))
                    if area <= 0:
                        print("\n❌ A área deve ser maior que zero!")
                        return
                    cultura_selecionada.area_m2 = area
            
            print("\nInsumos disponíveis:")
            for i, insumo in enumerate(insumos):
                print(f"[{i+1}] {insumo}")
            
            insumo_indices = input("\nEscolha os insumos para calcular (números separados por vírgula, 0 para todos): ")
            
            insumos_selecionados = []
            
            if insumo_indices == "0":
                insumos_selecionados = insumos.copy()  # Use a copy to avoid reference issues
            else:
                try:
                    for indice in insumo_indices.split(","):
                        idx = int(indice.strip()) - 1
                        if 0 <= idx < len(insumos):
                            insumos_selecionados.append(insumos[idx])
                        else:
                            print(f"\n⚠️ Índice {idx + 1} inválido, ignorando...")
                except ValueError:
                    print("\n⚠️ Entrada inválida. Usando todos os insumos disponíveis.")
                    insumos_selecionados = insumos.copy()  # Use a copy to avoid reference issues
            
            if not insumos_selecionados:
                print("\n❌ Nenhum insumo válido selecionado!")
                return
            
            # Adicionar os insumos selecionados à cultura (sem perguntar)
            insumos_adicionados = 0
            for insumo in insumos_selecionados:
                # Verificar se o insumo já existe na cultura
                if not any(i.nome == insumo.nome and i.tipo == insumo.tipo for i in cultura_selecionada.insumos):
                    cultura_selecionada.adicionar_insumo(insumo)
                    insumos_adicionados += 1
            
            # Calcular e exibir resultados
            print("\n" + "-"*60)
            print(f"RESULTADOS PARA: {cultura_selecionada.nome}".center(60))
            print("-"*60)
            print(f"Área total: {cultura_selecionada.area_m2:.2f} m²")
            print("-"*60)
            print(f"{'Insumo':<20} {'Tipo':<15} {'Qtd por m²':<12} {'Total':<15}")
            print("-"*60)
            
            for insumo in insumos_selecionados:
                total = insumo.calcular_quantidade_total(cultura_selecionada.area_m2)
                print(f"{insumo.nome:<20} {insumo.tipo:<15} {insumo.quantidade_por_m2:.4f} {insumo.unidade:<2} {total:.2f} {insumo.unidade:<10}")
            
            print("-"*60)
            if insumos_adicionados > 0:
                print(f"\n✅ {insumos_adicionados} novos insumos adicionados à cultura '{cultura_selecionada.nome}'!")
            else:
                print(f"\n⚠️ Todos os insumos selecionados já estavam cadastrados na cultura.")
            
            print(f"Total de insumos na cultura: {len(cultura_selecionada.insumos)}")
            input("\nPressione ENTER para continuar...")
        else:
            print("\n❌ Índice inválido!")
    except ValueError:
        print("\n❌ Entrada inválida! Operação cancelada.")
