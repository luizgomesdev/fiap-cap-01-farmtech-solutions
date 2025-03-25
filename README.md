# 🌱 FarmTech Solutions - Agricultura Digital

## 📖 Sobre o Projeto
FarmTech Solutions é uma aplicação Python desenvolvida para ajudar produtores rurais na transição para a Agricultura Digital, com foco em duas culturas de grande importância em Minas Gerais: café ☕ e soja 🌾. O sistema permite gerenciar culturas, calcular áreas plantadas e otimizar o uso de insumos, além de integrar análise estatística via R.

---

## 📜 **Regras de Negócio**

### 1️⃣ **Gestão de Culturas**
- O sistema suporta o cadastro de culturas agrícolas, com foco inicial em **Café** e **Soja**
- Cada cultura armazena:
  - Nome da cultura
  - Tipo de plantio (ruas ou talhões)
  - Área plantada
  - Insumos utilizados
  - Quantidade de insumos por metro quadrado

### 2️⃣ **Cálculo de Área Plantada**
- **Café**: Cálculo por ruas retangulares
  - `Área = Comprimento × Largura × Número de ruas`
- **Soja**: Cálculo por talhões quadrados
  - `Área = Lado × Lado × Número de talhões`

### 3️⃣ **Manejo de Insumos**
- Cadastro e cálculo de diferentes tipos de insumos:
  - Fertilizantes (sólidos e líquidos)
  - Defensivos agrícolas
  - Irrigação
- Cálculo automático baseado na área: `Quantidade total = Quantidade por m² × Área total`

### 4️⃣ **Exportação e Análise**
- Exportação dos dados de insumos para CSV
- Análise estatística via script R, calculando médias e desvio padrão

---

## 🧩 **Estrutura do Projeto**

```
fiap-cap-01-farmtech-solutions/
├── main.py              # Ponto de entrada da aplicação
├── requirements.txt     # Dependências do projeto
├── src/                 # Código-fonte principal
│   ├── models/          # Modelos de dados
│   │   ├── cafe.py      # Modelo para cultura de café
│   │   ├── cultura.py   # Modelo base para culturas
│   │   ├── insumo.py    # Modelo para insumos
│   │   └── soja.py      # Modelo para cultura de soja
│   └── utils/           # Utilitários
│       └── menus/       # Interfaces de menu
│           ├── areas_menu.py     # Menu de cálculo de áreas
│           ├── culturas_menu.py  # Menu de gestão de culturas
│           └── insumos_menu.py   # Menu de manejo de insumos
├── scripts/             # Scripts complementares
│   ├── codigo_R.R       # Análise estatística em R
│   └── codigo_meteorologico.R  # Dados meteorológicos
└── relatorios/          # Diretório para relatórios exportados
```

## 🚀 **Como Executar**

### 🔹 Pré-requisitos
- Python 3.x
- R (para análise estatística)

### 🔹 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/luizgomesdev/fiap-cap-01-farmtech-solutions
   cd fiap-cap-01-farmtech-solutions
   ```

2. Execute a aplicação:
   ```bash
   python main.py
   ```

### 🔹 Para análise estatística
1. Exporte os dados de insumos no menu "Gestão de Culturas" > "Exportar Insumos de Cultura"
2. Execute o script R:
   ```bash
   Rscript scripts/codigo_R.R
   ```

## 📋 **Funcionalidades**

### 🔹 **Gestão de Culturas**
- Cadastro, edição e remoção de culturas
- Visualização de culturas e seus insumos
- Exportação de dados para análise

### 🔹 **Cálculo de Áreas**
- Dois métodos de cálculo disponíveis:
  - Ruas retangulares (ideal para café)
  - Talhões quadrados (ideal para soja)

### 🔹 **Manejo de Insumos**
- Cadastro de diversos tipos de insumos
- Cálculo automático das quantidades necessárias
- Visualização do total de insumos por cultura

## 🌦️ **Módulo Meteorológico**
Um recurso adicional é o script de dados meteorológicos que pode auxiliar no planejamento de atividades como aplicação de defensivos e irrigação. Este módulo obtém dados em tempo real para a região de Araxá-MG.

---

💻 **Repositório**: [github.com/luizgomesdev/fiap-cap-01-farmtech-solutions](https://github.com/luizgomesdev/fiap-cap-01-farmtech-solutions)

---

📌 **FarmTech Solutions - Tecnologia para o Agronegócio!** 🌱🚜
