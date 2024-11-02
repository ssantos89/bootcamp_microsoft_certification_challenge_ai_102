# AI Translator

Este repositório contém dois scripts para tradução automática de textos. Eles utilizam diferentes fontes de entrada e APIs para traduzir conteúdos para outros idiomas. Esses scripts podem ser úteis para tarefas de tradução de artigos ou documentos, aproveitando serviços de tradução baseados em IA.

## Scripts

### 1. `ai-translator-with-article.py`

**Descrição**  
Este script é projetado para extrair e traduzir textos de artigos acessíveis via URL. Ele faz uso da biblioteca BeautifulSoup para extrair o conteúdo textual de uma página web e do modelo Azure OpenAI para traduzir o texto para o idioma desejado.

**Principais Funcionalidades**
- **Extração de Texto de Artigos**: A função `extract_text_from_url(url)` busca e extrai o conteúdo textual de uma URL fornecida, removendo scripts e estilos para garantir que apenas o texto relevante seja extraído.
- **Tradução de Texto**: A função `translate_article(text, lang)` utiliza o modelo `AzureChatOpenAI` da OpenAI para traduzir o texto extraído. Ela envia o conteúdo ao modelo para tradução e retorna o resultado em formato Markdown.

**Configurações Necessárias**
- **Parâmetros de Conexão**: É necessário fornecer os detalhes da conexão com o Azure, incluindo `azure_endpoint`, `api_key`, `api_version` e `deployment_name`.

**Uso do Script**
1. Defina o link do artigo (`your_article_link`).
2. Extraia o texto do artigo utilizando `extract_text_from_url(url)`.
3. Traduza o texto chamando `translate_article(text, 'pt-br')`.

### 2. `ai-translator-with-documents.py`

**Descrição**  
Este script permite traduzir documentos de texto no formato `.docx`. Ele usa a API de tradução da Azure para converter o texto do documento para o idioma desejado.

**Principais Funcionalidades**
- **Tradução de Texto Simples**: A função `translator_text(text, target_language)` envia o texto para a API de tradução e retorna o resultado traduzido para o idioma definido.
- **Tradução de Documentos**: A função `translate_document(path)` processa o conteúdo de um arquivo `.docx`, traduz cada parágrafo e cria um novo arquivo `.docx` com o texto traduzido.

**Configurações Necessárias**
- **API Key e Endpoint**: É necessário fornecer a `subscription_key`, o `endpoint` da API e a localização do endpoint (`location`).
- **Idioma de Destino**: O idioma para o qual o texto será traduzido deve ser definido em `language_destination`.

**Uso do Script**
1. Especifique o caminho do documento (`your_path_file`).
2. Traduza o documento com `translate_document(path)`, que salvará o arquivo traduzido com um sufixo no idioma de destino no mesmo diretório.

## Dependências

Ambos os scripts requerem as seguintes bibliotecas:
- **requests**: Para fazer requisições HTTP.
- **BeautifulSoup** (disponível no pacote `bs4`): Para extração de texto em páginas HTML (usado apenas no `ai-translator-with-article.py`).
- **python-docx**: Para manipulação de documentos `.docx` (usado apenas no `ai-translator-with-documents.py`).

Instale as dependências com:
```bash
pip install requests beautifulsoup4 python-docx
