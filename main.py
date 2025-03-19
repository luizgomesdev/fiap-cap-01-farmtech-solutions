#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FarmTech Solutions - Aplicação principal
Projeto de Agricultura Digital para gerenciamento de culturas e insumos
"""

import sys
import os

# Adiciona o diretório src ao PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Importa os módulos necessários
from utils.menu import exibir_menu_principal

def main():
    """
    Função principal que inicia a aplicação
    """
    print("\n" + "="*60)
    print(" 🌱 FarmTech Solutions - Agricultura Digital 🚜 ".center(60))
    print("="*60 + "\n")
    
    print("Bem-vindo ao sistema de gerenciamento de culturas e insumos.")
    print("Este sistema ajuda no cálculo de áreas plantadas e manejo de insumos.")
    print("Desenvolvido para fazendas em Minas Gerais, com foco em café e soja.\n")
    
    # Inicia o menu principal
    exibir_menu_principal()
    
    print("\nObrigado por usar o FarmTech Solutions!")

if __name__ == "__main__":
    main()
