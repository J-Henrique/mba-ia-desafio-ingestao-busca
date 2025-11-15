# Desafio MBA Engenharia de Software com IA - Full Cycle

Este repositório contém o primeiro desafio proposto para o MBA em Engenharia de Software com IA da Full Cycle. O projeto
implementa um sistema de Retrieval-Augmented Generation (RAG) que permite fazer perguntas sobre o conteúdo de um documento
PDF.

## Descrição

O sistema lê um documento PDF, o processa em partes menores (chunks), gera vetores de embeddings para cada parte e os
armazena em um banco de dados vetorial (PostgreSQL com pgvector). Em seguida, uma interface de chat permite que o
usuário faça perguntas. O sistema busca os trechos mais relevantes do documento no banco de dados para construir um
contexto e envia a pergunta junto com este contexto para um modelo de linguagem (LLM), que gera uma resposta baseada
estritamente no conteúdo do PDF.

## Configuração

1. **Crie um arquivo `.env`** na raiz do projeto:
   ```env
   # Configurações do Banco de Dados PostgreSQL
   DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/db_name"
   PG_VECTOR_COLLECTION_NAME="my_collection"

   # Caminho para o arquivo PDF a ser ingerido
   PDF_PATH="docs/seu-documento.pdf"

   # Chave da API da OpenAI
   OPENAI_API_KEY="sk-..."

   # Modelo de embedding da OpenAI
   OPENAI_EMBEDDING_MODEL="text-embedding-3-small"
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Estrutura do Projeto

O projeto é dividido em três módulos principais na pasta `src/`:

- `ingest.py`: Responsável por carregar o documento PDF, dividi-lo em chunks, gerar os embeddings e armazená-los no
  banco de dados vetorial PostgreSQL (pgvector).
- `search.py`: Realiza a busca por similaridade no banco de dados. Dado uma pergunta, ele encontra os chunks de texto
  mais relevantes e os formata em um prompt para o LLM.
- `chat.py`: Fornece a interface de linha de comando para o usuário. Ele recebe a pergunta, utiliza o `search.py` para
  obter o prompt e chama o LLM para gerar e exibir a resposta.

## Funcionamento

1. **Subir o container Docker:** Inicie o banco de dados PostgreSQL com a extensão `pgvector` usando Docker Compose.
   ```bash
   docker-compose up -d
   ```

2. **Executar a ingestão de dados:** Este comando irá processar o PDF e popular o banco de dados.
   ```bash
   python src/ingest.py
   ```

3. **Executar o chat:** Inicie a interface de chat para começar a fazer perguntas.
   ```bash
   python src/chat.py
   ```