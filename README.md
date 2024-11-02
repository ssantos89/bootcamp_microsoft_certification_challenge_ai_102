# Repositório Bootcamp Microsoft Certified: Projetos de Análise e Tradução com Azure AI

Este repositório contém dois projetos independentes, cada um com seu próprio propósito e funcionalidades específicas, utilizando serviços de Inteligência Artificial da Azure. Abaixo está uma descrição resumida dos diretórios e dos projetos que você encontrará ao navegar pelo repositório.

## Estrutura do Repositório

### 1. Diretório `analise_de_documentos_anti_fraude_com_azure_ai`

**Descrição**  
Este projeto implementa uma aplicação para análise de documentos com foco na detecção de fraudes em cartões de crédito. Ele permite que o usuário faça upload de uma imagem de cartão de crédito, que é então armazenada no Azure Blob Storage. Em seguida, utiliza o Azure Document Intelligence para extrair e validar informações, como nome do titular, número do cartão e data de validade.

**Principais Funcionalidades**
- Upload de imagens de cartões de crédito para análise.
- Armazenamento seguro no Azure Blob Storage.
- Análise das informações dos cartões para detectar possíveis fraudes.
- Interface interativa com Streamlit para facilitar o uso e visualização dos resultados.

**Arquivos Importantes**
- `app.py`: Interface principal do projeto.
- `services/`: Diretório com os serviços de armazenamento e análise.
- `.env`: Arquivo para configuração de variáveis de ambiente.
- `requirements.txt`: Dependências necessárias para executar o projeto.

### 2. Diretório `tradutor_de_artigos_tecnicos_com_azure_ai`

**Descrição**  
Este projeto contém scripts para tradução automática de textos, úteis para traduzir artigos e documentos técnicos para outros idiomas. O projeto inclui dois scripts principais, um para tradução de textos extraídos de URLs e outro para tradução de documentos `.docx`.

**Principais Funcionalidades**
- Tradução de conteúdo de artigos da web, extraindo o texto de URLs.
- Tradução de documentos de texto no formato `.docx`.
- Utilização do Azure OpenAI para tradução de conteúdo textual em diferentes idiomas.

**Scripts Principais**
- `ai-translator-with-article.py`: Script para extração e tradução de textos de URLs.
- `ai-translator-with-documents.py`: Script para tradução de documentos `.docx`.
- `requirements.txt`: Lista de dependências para execução dos scripts de tradução.

## Como Navegar pelo Repositório

- **Para Análise de Documentos Anti-Fraude**: Navegue até o diretório `analise_de_documentos_anti_fraude_com_azure_ai`, onde você encontrará a aplicação para detecção de fraudes com instruções completas de uso no arquivo `README.md` desse diretório.
- **Para Tradução de Artigos e Documentos**: Acesse o diretório `tradutor_de_artigos_tecnicos_com_azure_ai`, que contém os scripts de tradução com explicações detalhadas em seu próprio `README.md`.

## Pré-Requisitos

Ambos os projetos utilizam serviços da Azure e requerem configuração de credenciais e endpoints no arquivo `.env`. Além disso, cada projeto possui seu próprio `requirements.txt` para instalação de dependências específicas.

## Observação

Para utilizar os projetos corretamente, é essencial seguir as instruções de configuração e execução fornecidas em cada `README.md` dos diretórios específicos. Certifique-se de configurar suas variáveis de ambiente e ter uma conta Azure ativa para acessar os serviços de IA necessários.

---

Este README fornece uma visão geral dos projetos incluídos no repositório e ajuda a orientar os usuários sobre o conteúdo e como navegar entre os diretórios.
