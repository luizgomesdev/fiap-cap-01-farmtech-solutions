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
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação Python:
   ```bash
   python main.py
   ```
5. Para análise estatística, execute o script R:
   ```bash
   Rscript scripts/analysis.R
   ```

---

## 📩 **Contato e Contribuição**
Este projeto é desenvolvido como parte de um estudo de **Agricultura Digital**.  
Contribuições são bem-vindas!  

👨‍💻 Equipe de Desenvolvimento:  
- **Nome 1** (Líder de Projeto)  
- **Nome 2** (Desenvolvedor Python)  
- **Nome 3** (Analista de Dados em R)  
- **Nome 4** (Documentação e Versionamento)  

📬 Entre em contato: `seuemail@example.com`

---

📌 **FarmTech Solutions - Tecnologia para o Agronegócio!** 🌱🚜
