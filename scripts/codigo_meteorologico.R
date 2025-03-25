# Define lib local
.libPaths("~/R/libs")
dir.create("~/R/libs", showWarnings = FALSE, recursive = TRUE)

# Verifica e instala pacotes automaticamente
pacotes <- c("httr", "jsonlite")

instalar_se_faltar <- function(p) {
  if (!require(p, character.only = TRUE)) {
    install.packages(p, dependencies = TRUE)
    library(p, character.only = TRUE)
  }
}

invisible(sapply(pacotes, instalar_se_faltar))

# Coordenadas da fazenda (exemplo: Araxá - MG)
latitude <- -19.5902
longitude <- -46.9438

# URL da API (dados diários do tempo atual)
url <- paste0("https://api.open-meteo.com/v1/forecast?",
              "latitude=", latitude,
              "&longitude=", longitude,
              "&current=temperature_2m,relative_humidity_2m,precipitation,rain,wind_speed_10m")

# Requisição GET
resposta <- httr::GET(url)

# Verifica se deu certo
if (httr::status_code(resposta) == 200) {
  dados_json <- httr::content(resposta, "text")
  dados_lista <- jsonlite::fromJSON(dados_json)
  
  # Extrai os dados atuais
  clima_atual <- dados_lista$current
  
  cat("----- CLIMA ATUAL EM ARAXÁ/MG -----\n")
  cat("Temperatura: ", clima_atual$temperature_2m, "°C\n")
  cat("Umidade: ", clima_atual$relative_humidity_2m, "%\n")
  cat("Precipitação: ", clima_atual$precipitation, "mm\n")
  cat("Chuva: ", clima_atual$rain, "mm\n")
  cat("Vento: ", clima_atual$wind_speed_10m, "km/h\n")
} else {
  cat("Erro ao acessar a API. Código:", httr::status_code(resposta), "\n")
}
