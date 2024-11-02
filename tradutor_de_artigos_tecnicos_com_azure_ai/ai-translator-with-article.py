import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        texto = soup.get_text(separator=' ')
        # Limpar texto
        linhas = (line.strip() for line in texto.splitlines())
        parts = (phrase.strip() for line in linhas for phrase in line.split("  "))
        texto_limpo = '\n'.join(part for part in parts if part)
        return texto_limpo
    else:
        print(f'Failed to fetch the URL. Status code: {response.status_code}')
        return None

extract_text_from_url('your_article_link')

from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint='your_endpoint_name',
    api_key='your_api_key',
    api_version='your_api_version',
    deployment_name='your_model_name',
    max_retries=0
)

def translate_article(text, lang):
    messages = [
        ('system', 'Você atua como tradutor de textos'),
        ('user', f'Traduza o {text} para o idioma {lang} e responda em markdown')
    ]

    response = client.invoke(messages)
    print(response.content)
    return response.content

# translate_article('Lets see if the deployment was succeded.', 'portugues')

url = 'your_article_link'
text = extract_text_from_url(url)
article = translate_article(text, 'pt-br')

print(article)
