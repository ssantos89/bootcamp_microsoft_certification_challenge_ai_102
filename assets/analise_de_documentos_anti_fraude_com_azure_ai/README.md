# Análise de Documentos Anti-Fraude com Azure AI

Este projeto implementa uma aplicação para análise de documentos que utiliza o serviço de AI da Azure para detectar possíveis fraudes em cartões de crédito. Ele permite que os usuários façam upload de uma imagem de cartão de crédito, armazene a imagem no Azure Blob Storage e, em seguida, analise o cartão utilizando o Azure Document Intelligence para validar as informações e identificar dados relevantes, como o nome do titular, número do cartão e data de validade.

## Funcionalidades

- **Upload de Imagem**: O usuário pode fazer o upload de uma imagem de um cartão de crédito.
- **Armazenamento no Azure Blob Storage**: A imagem é enviada e armazenada no Azure Blob Storage para processamento.
- **Análise do Cartão de Crédito**: Utiliza o Azure Document Intelligence para extrair e validar as informações contidas no cartão.
- **Exibição dos Resultados**: Exibe o resultado da análise, incluindo o nome do titular do cartão, banco emissor e data de validade. Informa se o cartão é válido ou não.

## Estrutura do Projeto

- `services/blob_service.py`: Lida com o envio das imagens para o Azure Blob Storage.
- `services/credit_card_service.py`: Realiza a análise do cartão de crédito usando o Azure Document Intelligence.
- `utils/config.py`: Carrega as variáveis de ambiente para configurar as credenciais e endpoints do Azure.
- `.env`: Arquivo que armazena as variáveis de ambiente, incluindo `ENDPOINT`, `SUBSCRIPTION_KEY`, `AZURE_STORAGE_CONNECTION_STRING`, e `CONTAINER_NAME`.
- `requirements.txt`: Lista as dependências necessárias para executar a aplicação.
- `app.py`: Interface principal da aplicação, criada com Streamlit, onde os usuários interagem e visualizam os resultados da análise.

## Configuração e Uso

### 1. Configurar as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```bash
ENDPOINT='your_endpoint_azure_ai_document_intelligence'
SUBSCRIPTION_KEY='your_api_key'
AZURE_STORAGE_CONNECTION_STRING='your_default_endpoint_protocol'
CONTAINER_NAME='your_container_name'
```

### 2. Instalar as Dependências

Execute o comando abaixo para instalar todas as dependências listadas no requirements.txt:

```bash
pip install -r requirements.txt
```

### 3. Executar a Aplicação

Inicie a aplicação com o Streamlit:

```bash
streamlit run app.py
```

### 4. Uso da Aplicação

1. Acesse a interface do Streamlit em seu navegador.

2. Faça o upload de uma imagem de um cartão de crédito (nos formatos `.png`, `.jpg` ou `.jpeg`).

3. A imagem será enviada para o Azure Blob Storage.

4. O serviço Azure Document Intelligence analisará a imagem para extrair informações do cartão.

5. A aplicação exibirá os detalhes extraídos, indicando se o cartão é válido ou não.

## Dependências

- `azure.core`: Pacote para autenticação na Azure.

- `azure-ai-documentintelligence`: Biblioteca para uso do serviço Document Intelligence da Azure.

- `streamlit`: Framework para criação de interfaces web simples e interativas.

- `azure-storage-blob`: Biblioteca para interação com o Azure Blob Storage.

- `python-dotenv`: Carrega variáveis de ambiente do arquivo .`env`.

## Observação

Certifique-se de configurar corretamente as credenciais e endpoints no arquivo `.env` antes de rodar a aplicação para evitar erros de conexão com os serviços da Azure.