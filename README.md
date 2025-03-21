# 🌱 FarmTech Solutions - Agricultura Digital

## 📖 Sobre o Projeto
Este projeto tem como objetivo desenvolver uma aplicação em Python para auxiliar fazendas na transição para a **Agricultura Digital**, otimizando o manejo de insumos e cálculos de áreas plantadas. O sistema também inclui análise estatística em R para melhorar a tomada de decisão.

---

## 📜 **Regras de Negócio**
A aplicação atende fazendas em **Minas Gerais**, considerando as culturas **café** ☕ e **soja** 🌾, que são relevantes na região.  

### 1️⃣ **Gestão de Culturas**
- O sistema deve permitir o cadastro de culturas agrícolas.  
- Devem ser suportadas **duas culturas principais**: **Café** e **Soja**.  
- Cada cultura deve armazenar:
  - Nome da cultura;
  - Tipo de plantio (exemplo: ruas ou talhões);
  - Área plantada;
  - Insumos utilizados (fertilizantes, defensivos, água, etc.);
  - Quantidade de insumos aplicados por metro quadrado.

### 2️⃣ **Cálculo de Área Plantada**
- Para **café**, a área será calculada considerando **ruas retangulares**:  
  - Fórmula: `Área = Comprimento da rua × Largura da rua × Número de ruas`.  
- Para **soja**, a área será baseada em **talhões quadrados**:  
  - Fórmula: `Área = Lado × Lado`.  

### 3️⃣ **Cálculo do Manejo de Insumos**
- O usuário seleciona uma cultura e insere os insumos necessários.  
- O cálculo de insumos é baseado na **quantidade necessária por metro quadrado**:
  - Exemplo: Para café, a aplicação de **500 mL/m² de defensivo agrícola** em uma lavoura com **10.000 m²** exigirá **5.000 L** no total.
- O sistema permitirá cálculos para diferentes tipos de aplicação, como:
  - Pulverização de defensivos;
  - Aplicação de fertilizantes sólidos e líquidos;
  - Cálculo de volume de irrigação.

### 4️⃣ **Operações CRUD (Criar, Ler, Atualizar, Deletar)**
- A aplicação precisa permitir:
  - **Cadastro** de culturas e insumos.
  - **Consulta** das culturas cadastradas e cálculo dos insumos necessários.
  - **Edição** das informações armazenadas.
  - **Exclusão** de culturas quando necessário.

### 5️⃣ **Análise Estatística em R**
- A aplicação exportará os dados para um **arquivo CSV**.
- Um script em **R** processará os dados e calculará:
  - **Média** e **desvio padrão** da área plantada e do consumo de insumos.

---

## 👨‍💻 **Como Executar o Projeto**
### 🔹 Pré-requisitos
- Python 3.x  
- R instalado  
- Bibliotecas Python: `pandas` e `numpy`  
- Editor de código (VSCode, PyCharm, Jupyter, etc.)

### 🔹 Rodando o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/luizgomesdev/fiap-cap-01-farmtech-solutions
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd fiap-cap-01-farmtech-solutions
   ```
3. Instale as dependências (não são necessárias dependências externas para a funcionalidade básica):
   ```bash
   # Nenhuma dependência externa é necessária para a execução básica
   ```
4. Execute a aplicação Python:
   ```bash
   python main.py
   ```

## 📋 **Estrutura e Funcionamento do Sistema**

### 🔹 **Arquitetura do Projeto**
O sistema está organizado em módulos com responsabilidades específicas:

- **Módulo de Culturas**: Gerencia o cadastro, listagem, atualização e remoção de culturas (Café e Soja)
- **Módulo de Áreas**: Calcula áreas de plantio usando diferentes métodos (ruas retangulares ou talhões)
- **Módulo de Insumos**: Gerencia o cadastro de insumos e calcula as quantidades necessárias

### 🔹 **Fluxo de Trabalho**
1. **Cadastro de Culturas**: Primeiro, cadastre uma cultura (Café e Soja já vêm pré-cadastradas)
2. **Cálculo de Área**: Defina a área da cultura usando cálculos por ruas ou talhões
3. **Cadastro de Insumos**: Registre os insumos necessários (fertilizantes, defensivos, etc.)
4. **Cálculo de Quantidades**: O sistema calcula automaticamente as quantidades de insumos necessárias com base na área
5. **Exportação de Dados**: Exporte os dados dos cálculos para arquivos CSV em `/relatorios`

### 🔹 **Recursos Principais**
- **Menu Interativo**: Interface via terminal de fácil navegação
- **Cálculos Automáticos**: Baseados em fórmulas específicas para cada cultura
- **Exportação de Dados**: Relatórios em formato CSV para análise posterior
- **Validações**: Sistema robusto que previne entradas inválidas

### 🔹 **Exemplo de Uso**
1. No menu principal, escolha "Gestão de Culturas" para ver as culturas disponíveis
2. Selecione "Cálculo de Área Plantada" e defina a área para uma cultura
3. Em "Manejo de Insumos", calcule as quantidades necessárias
4. Volte ao menu de culturas e use "Exportar Insumos de Cultura" para gerar um relatório

## 📩 **Contato e Contribuição**
Este projeto é desenvolvido como estudo de **Agricultura Digital** para o curso de pós-graduação da FIAP.

👨‍💻 Equipe de Desenvolvimento:
- **Nicolas Lemos Ribeiro** | RM 553273
- **Luiz Felipe Alves Gomes** | RM 565151
- **Ricardo de Paiva Melo** | RM 565522
- **Desirée Alberti Batista** | RM 562893

📬 Repositório: `https://github.com/luizgomesdev/fiap-cap-01-farmtech-solutions`

---

📌 **FarmTech Solutions - Tecnologia para o Agronegócio!** 🌱🚜
