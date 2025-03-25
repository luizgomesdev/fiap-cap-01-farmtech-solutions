"""
Módulo para gerenciamento de culturas
"""

from src.models.cultura import Cultura
from src.models.cafe import Cafe
from src.models.soja import Soja
import os
import datetime
import csv

# Lista para armazenar as culturas em memória
culturas = [Cafe(), Soja()]


def menu_culturas():
    """
    Menu para gestão de culturas
    """
    while True:
        print("\n" + "-" * 40)
        print("GESTÃO DE CULTURAS".center(40))
        print("-" * 40)
        print("[1] Cadastrar Nova Cultura")
        print("[2] Listar Culturas")
        print("[3] Atualizar Cultura")
        print("[4] Remover Cultura")
        print("[5] Ver Insumos de Cultura")
        print("[6] Exportar Insumos de Cultura")
        print("[0] Voltar ao Menu Principal")
        print("-" * 40)

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
            elif opcao == 5:
                ver_insumos_cultura()
            elif opcao == 6:
                exportar_insumos_cultura()
            else:
                print("\n❌ Opção inválida! Por favor, tente novamente.")
        except ValueError:
            print("\n❌ Entrada inválida! Digite apenas números.")


def cadastrar_cultura():
    """
    Cadastra uma nova cultura no sistema
    """
    print("\n" + "-" * 40)
    print("CADASTRO DE CULTURA".center(40))
    print("-" * 40)

    nome = input("Nome da cultura: ")

    # Verifica se a cultura já existe
    for cultura in culturas:
        if cultura.nome.lower() == nome.lower():
            print(f"\n❌ A cultura '{nome}' já está cadastrada!")
            return

    # Cria uma cultura genérica
    nova_cultura = Cultura(nome)

    # Adiciona a nova cultura
    culturas.append(nova_cultura)
    print(f"\n✅ Cultura '{nome}' cadastrada com sucesso!")
    print("Você pode calcular a área no menu 'Cálculo de Área Plantada'.")


def listar_culturas():
    """
    Lista todas as culturas cadastradas
    """
    print("\n" + "-" * 60)
    print("CULTURAS CADASTRADAS".center(60))
    print("-" * 60)

    if not culturas:
        print("\n⚠️ Não há culturas cadastradas!")
        return

    for i, cultura in enumerate(culturas):
        print(f"[{i+1}] {cultura}")

    print("-" * 60)
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
        indice = (
            int(
                input(
                    "\nDigite o número da cultura que deseja atualizar (0 para cancelar): "
                )
            )
            - 1
        )

        if indice == -1:
            print("\nOperação cancelada.")
            return

        if 0 <= indice < len(culturas):
            cultura = culturas[indice]

            print(f"\nAtualizando cultura: {cultura.nome}")

            novo_nome = input(
                f"Novo nome (atual: {cultura.nome}) [deixe em branco para manter]: "
            )
            if novo_nome:
                cultura.nome = novo_nome

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
        indice = (
            int(
                input(
                    "\nDigite o número da cultura que deseja remover (0 para cancelar): "
                )
            )
            - 1
        )

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


def ver_insumos_cultura():
    """
    Visualiza os insumos calculados para uma cultura
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas!")
        return

    listar_culturas()

    try:
        indice = (
            int(
                input(
                    "\nDigite o número da cultura para ver os insumos (0 para cancelar): "
                )
            )
            - 1
        )

        if indice == -1:
            print("\nOperação cancelada.")
            return

        if 0 <= indice < len(culturas):
            cultura = culturas[indice]

            print("\n" + "-" * 60)
            print(f"INSUMOS PARA: {cultura.nome}".center(60))
            print("-" * 60)

            if not cultura.insumos:
                print("\n⚠️ Não há insumos calculados para esta cultura.")
                print(
                    "Vá ao menu 'Manejo de Insumos' e escolha 'Calcular Quantidade de Insumos'."
                )
            else:
                # Mostrar informações básicas
                print(f"Cultura: {cultura.nome}")
                print(f"Área calculada: {cultura.area_m2:.2f} m²")

                # Agrupar insumos por tipo para melhor visualização
                insumos_por_tipo = {}
                for insumo in cultura.insumos:
                    if insumo.tipo not in insumos_por_tipo:
                        insumos_por_tipo[insumo.tipo] = []
                    insumos_por_tipo[insumo.tipo].append(insumo)

                print(f"\nTotal de insumos: {len(cultura.insumos)}")
                print("-" * 60)
                print(
                    f"{'Nome':<20} {'Tipo':<15} {'Qtd/m²':<10} {'Unid.':<5} {'Total':<10}"
                )
                print("-" * 60)

                # Imprimir insumos agrupados por tipo
                for tipo, lista_insumos in sorted(insumos_por_tipo.items()):
                    print(f"\n>> {tipo}:")
                    for insumo in lista_insumos:
                        total = insumo.calcular_quantidade_total(cultura.area_m2)
                        print(
                            f"{insumo.nome:<20} {insumo.tipo:<15} {insumo.quantidade_por_m2:<10.4f} {insumo.unidade:<5} {total:<10.2f}"
                        )

            print("\n" + "-" * 60)
        else:
            print("\n❌ Índice inválido!")
    except ValueError:
        print("\n❌ Entrada inválida!")

    input("\nPressione ENTER para continuar...")


def exportar_insumos_cultura():
    """
    Exporta os insumos de uma cultura específica para um arquivo CSV
    """
    if not culturas:
        print("\n⚠️ Não há culturas cadastradas!")
        return

    listar_culturas()

    try:
        indice = (
            int(
                input(
                    "\nDigite o número da cultura para exportar os insumos (0 para cancelar): "
                )
            )
            - 1
        )

        if indice == -1:
            print("\nOperação cancelada.")
            return

        if 0 <= indice < len(culturas):
            cultura = culturas[indice]

            if not cultura.insumos:
                print("\n⚠️ Esta cultura não tem insumos calculados!")
                print(
                    "Vá ao menu 'Manejo de Insumos' e escolha 'Calcular Quantidade de Insumos' primeiro."
                )
                return

            # Cria o diretório de relatórios se não existir
            diretorio = "relatorios"
            if not os.path.exists(diretorio):
                os.makedirs(diretorio)

            # Gera um nome de arquivo CSV com data/hora e nome da cultura
            nome_cultura = cultura.nome.lower().replace(" ", "_")
            data_hora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_arquivo = f"{diretorio}/insumos_{nome_cultura}_{data_hora}.csv"

            with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo_csv:
                # Criar o escritor CSV
                escritor_csv = csv.writer(
                    arquivo_csv, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL
                )

                # Escrever o cabeçalho das colunas
                escritor_csv.writerow(
                    [
                        "Nome",
                        "Tipo",
                        "Quantidade_por_m2",
                        "Unidade",
                        "Total",
                        "Area_m2",
                        "Cultura",
                    ]
                )

                # Escrever dados dos insumos (cada insumo em uma linha)
                for insumo in cultura.insumos:
                    total = insumo.calcular_quantidade_total(cultura.area_m2)

                    # Converter para string, garantindo que usa ponto como separador decimal
                    quantidade_str = f"{insumo.quantidade_por_m2:.4f}".replace(",", ".")
                    total_str = f"{total:.2f}".replace(",", ".")
                    area_str = f"{cultura.area_m2:.2f}".replace(",", ".")

                    escritor_csv.writerow(
                        [
                            insumo.nome,
                            insumo.tipo,
                            quantidade_str,
                            insumo.unidade,
                            total_str,
                            area_str,
                            cultura.nome,
                        ]
                    )

            print(
                f"\n✅ Insumos da cultura '{cultura.nome}' exportados com sucesso para CSV!"
            )
            print(f"Arquivo salvo em: {nome_arquivo}")

        else:
            print("\n❌ Índice inválido!")
    except ValueError:
        print("\n❌ Entrada inválida!")
    except Exception as e:
        print(f"\n❌ Erro ao exportar insumos: {e}")

    input("\nPressione ENTER para continuar...")
