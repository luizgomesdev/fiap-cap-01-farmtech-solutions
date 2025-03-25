# Define o diretório de trabalho com caminho absoluto
setwd("/home/ubuntu/Developer/fiap-cap-01-farmtech-solutions")

# Define o diretório onde estão os relatórios
diretorio_relatorios <- file.path("/home/ubuntu/Developer/fiap-cap-01-farmtech-solutions", "relatorios")

# Verifica se o diretório de relatórios existe
if (!dir.exists(diretorio_relatorios)) {
  dir.create(diretorio_relatorios, recursive = TRUE)
  cat("Diretório de relatórios criado em:", diretorio_relatorios, "\n")
}

# Lista todos os arquivos CSV no diretório de relatórios
arquivos_csv <- list.files(path = diretorio_relatorios, pattern = "insumos_.*\\.csv$", full.names = TRUE)

if (length(arquivos_csv) == 0) {
  stop("Nenhum arquivo de insumos encontrado no diretório de relatórios.")
}

# Obtém o arquivo mais recente (usado por padrão)
arquivo_mais_recente <- arquivos_csv[which.max(file.info(arquivos_csv)$mtime)]
cat("Usando arquivo:", basename(arquivo_mais_recente), "\n")

# Lê os dados do arquivo CSV, que está separado por ponto e vírgula
dados <- read.csv(file = arquivo_mais_recente, header = TRUE, sep = ';', stringsAsFactors = FALSE)

# Divide o dataframe original em uma lista de dataframes, agrupando por "Nome" do insumo
# Cada item da lista 'lista_tabelas' conterá apenas os dados de um insumo específico
lista_tabelas <- split(dados, dados$Nome)
# Exibe no console as tabelas separadas por insumo (para verificação)
print(lista_tabelas)
# Aplica uma função a cada tabela da lista para calcular a média e o desvio padrão
resultados <- lapply(lista_tabelas, function(df){
  # Calcula a média da coluna Quantidade_por_m2, ignorando valores ausentes (NA)
  media <- mean(df$Quantidade_por_m2, na.rm = TRUE)
  # Calcula o desvio padrão da mesma coluna
  desvio_padrao <- sd(df$Quantidade_por_m2, na.rm = TRUE)
  # Retorna os resultados como um dataframe com o nome do insumo, a média e o desvio padrão
  return(data.frame(Nome = unique(df$Nome), Media = media, Desvio_Padrao = desvio_padrao))
})
# Junta todos os dataframes individuais (um para cada insumo) em um único dataframe final
resultados_df <- do.call(rbind, resultados)
# Exporta os resultados finais para um arquivo CSV chamado 'resultados.csv'
# O parâmetro row.names = FALSE evita que o número da linha apareça como uma coluna extra no CSV
write.csv(resultados_df, 'resultados.csv', row.names = FALSE)
