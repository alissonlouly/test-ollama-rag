# Aplicativo RAG Simples

## Visão Geral

Este projeto faz parte do meu aplicativo de Geração Aumentada por Recuperação (RAG) em autodesenvolvimento, que permite aos usuários fazer perguntas sobre o conteúdo de arquivos PDF colocados em uma pasta. O aplicativo usa técnicas para fornecer respostas precisas com base no conteúdo do documento. O aplicativo utiliza Ollama, Llama 3-8B, LangChain e FAISS para suas operações.

## Funcionalidades

- **Faça Perguntas Sobre PDFs:** Basta colocar um arquivo PDF na pasta `data` ou fazer o upload pela interface Web e começar a fazer perguntas sobre seu conteúdo.
- **Modelos LLM:** Utiliza Ollama e Llama 3-8B para gerar respostas.
- **Recuperação Eficiente de Documentos:** Usa LangChain e FAISS para recuperação e processamento eficientes de documentos (Somente PDF).
- **Tratamento de Duplicados:** O aplicativo verifica o banco de dados de vetores em busca de duplicados e evita adicioná-los se já existirem.

## Começando

### Pré-requisitos

- Python 3.8 ou superior
- Pacotes Python necessários (veja `requirements.txt`)
- Instalação do Ollama com o Llama 3 instalado

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/alissonlouly/test-ollama-rag.git
   cd teste-ollama-rag
   ```
2. Instale os pacotes necessários:
   ```bash
   pip install -r requirements.txt
   ```
3. Baixe o Ollama e instale o LLM usando o Ollama:
   ```bash
   ollama pull llama3
   ```

### Uso

1. Coloque seu(s) arquivo(s) PDF na pasta `data` ou faça o upload pela interface Web.
2. Execute o aplicativo:

   ```bash
   streamlit run [caminho_para_pasta_do_aplicativo]/webui.py
   ```

   Alternativamente, você pode abrir o arquivo `webui.bat`.
3. Digite suas perguntas quando solicitado. Digite 'exit' para sair do aplicativo.

## Funcionalidades Em Andamento

- [X] **Interface Web:** Uma interface de usuário baseada na Web para facilitar a interação.
- [X] **Memória de Conversa:** O aplicativo lembrará as interações anteriores durante a execução para melhor tratamento do contexto.
- [ ] **Suporte para Vários Tipos de Documentos:** Estender a funcionalidade para trabalhar com slides do Powerpoint, arquivos markdown, arquivos de texto e muito mais.

## Contribuindo

Contribuições são bem-vindas! Por favor, faça um fork do repositório e crie um pull request com suas alterações. Para alterações ou caso encontre algum erro, abra um issue primeiro para discutir o que você gostaria de mudar.
