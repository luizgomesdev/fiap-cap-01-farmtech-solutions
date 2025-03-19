"""
Módulo para gerenciamento de culturas
"""
from src.models.cultura import Cultura
from src.models.cafe import Cafe
from src.models.soja import Soja

# Lista para armazenar as culturas em memória
culturas = [
    Cafe(),
    Soja()
]

def menu_culturas():
    """
    Menu para gestão de culturas
    """
    while True:
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
                cadastrar_cultura()
            elif opcao == 2:
                listar_culturas()
            elif opcao == 3:
                atualizar_cultura()
            elif opcao == 4:
                remover_cultura()
            else:
                print("\n❌ Opção inválida! Por favor, tente novamente.")
        except ValueError:
            print("\n❌ Entrada inválida! Digite apenas números.")

def cadastrar_cultura():
    """
    Cadastra uma nova cultura no sistema
    """
    print("\n" + "-"*40)
    print("CADASTRO DE CULTURA".center(40))
    print("-"*40)
    
    nome = input("Nome da cultura: ")
    
    print("\nTipos de plantio disponíveis:")
    print("[1] Ruas (para café)")
    print("[2] Talhões (para soja)")
    
    try:
        tipo_opcao = int(input("\nEscolha o tipo de plantio: "))
        if tipo_opcao == 1:
            tipo_plantio = "Ruas"
            nova_cultura = Cafe(nome)
        elif tipo_opcao == 2:
            tipo_plantio = "Talhões"
            nova_cultura = Soja(nome)
        else:
            print("\n❌ Opção inválida! Cadastro cancelado.")
            return
        
        # Verifica se a cultura já existe
        for cultura in culturas:
            if cultura.nome.lower() == nome.lower():
                print(f"\n❌ A cultura '{nome}' já está cadastrada!")
                return
        
        # Adiciona a nova cultura
        culturas.append(nova_cultura)
        print(f"\n✅ Cultura '{nome}' cadastrada com sucesso!")
        
    except ValueError:
        print("\n❌ Entrada inválida! Cadastro cancelado.")

def listar_culturas():
    """
    Lista todas as culturas cadastradas
    """
    print("\n" + "-"*60)
    print("CULTURAS CADASTRADAS".center(60))
    print("-"*60)
    
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas!")
        return
    
    for i, cultura in enumerate(culturas):
        print(f"[{i+1}] {cultura}")
    
    print("-"*60)
    input("\nPressione ENTER para continuar...")

def atualizar_cultura():
    """
    Atualiza informações de uma cultura existente
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas para atualizar!")
        return
        
    listar_culturas()
    
    try:
        indice = int(input("\nDigite o número da cultura que deseja atualizar (0 para cancelar): ")) - 1
        
        if indice == -1:
            print("\nOperação cancelada.")
            return
            
        if 0 <= indice < len(culturas):
            cultura = culturas[indice]
            
            print(f"\nAtualizando cultura: {cultura.nome}")
            
            novo_nome = input(f"Novo nome (atual: {cultura.nome}) [deixe em branco para manter]: ")
            if novo_nome:
                cultura.nome = novo_nome
                
            print("\nTipos de plantio disponíveis:")
            print(f"[1] Ruas (atual: {'X' if cultura.tipo_plantio == 'Ruas' else ' '})")
            print(f"[2] Talhões (atual: {'X' if cultura.tipo_plantio == 'Talhões' else ' '})")
            
            tipo_opcao = input("\nEscolha o tipo de plantio [deixe em branco para manter]: ")
            if tipo_opcao:
                tipo_opcao = int(tipo_opcao)
                if tipo_opcao == 1:
                    cultura.tipo_plantio = "Ruas"
                elif tipo_opcao == 2:
                    cultura.tipo_plantio = "Talhões"
                    
            print(f"\n✅ Cultura atualizada com sucesso: {cultura}")
        else:
            print("\n❌ Índice inválido!")
    except ValueError:
        print("\n❌ Entrada inválida! Atualização cancelada.")

def remover_cultura():
    """
    Remove uma cultura cadastrada
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas para remover!")
        return
        
    listar_culturas()
    
    try:
        indice = int(input("\nDigite o número da cultura que deseja remover (0 para cancelar): ")) - 1
        
        if indice == -1:
            print("\nOperação cancelada.")
            return
            
        if 0 <= indice < len(culturas):
            cultura_removida = culturas.pop(indice)
            print(f"\n✅ Cultura '{cultura_removida.nome}' removida com sucesso!")
        else:
            print("\n❌ Índice inválido!")
    except ValueError:
        print("\n❌ Entrada inválida! Remoção cancelada.")
