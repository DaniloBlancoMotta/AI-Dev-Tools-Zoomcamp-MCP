# FastMCP Documentation Search Server 🚀

Este projeto é um servidor MCP (Model Context Protocol) construído com **FastMCP** que inclui uma ferramenta de busca inteligente para a documentação do repositório FastMCP.

## 📋 Funcionalidades

- **`search_docs(query)`**: Ferramenta de busca que utiliza TF-IDF (via `minsearch`) para encontrar os 5 documentos mais relevantes dentro da documentação do FastMCP (`.md` e `.mdx`).
- **`add(a, b)`**: Ferramenta simples para somar dois números.
- **`hash_text(text)`**: Gera um hash SHA-256 de um texto.
- **`scrape_page(url)`**: Extrai o conteúdo de uma página web utilizando o Jina Reader.

## 🛠️ Tecnologias Utilizadas

- **FastMCP**: Framework para criação rápida de servidores MCP.
- **minsearch**: Mecanismo de busca minimalista baseado em TF-IDF.
- **Scikit-learn & Pandas**: Para processamento de texto e vetores.
- **Requests & Zipfile**: Para manipulação de dados externos e arquivos.

## 🚀 Como Executar

### Pré-requisitos
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recomendado)

### Instalação
1. Certifique-se de que as dependências estão instaladas:
   ```bash
   uv sync
   ```

### Execução Local
Para rodar o servidor em modo de desenvolvimento:
```bash
uv run python main.py
```

### Uso no Claude Desktop
Adicione a seguinte configuração ao seu arquivo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "fastmcp-search": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/Users/UNIVERSO/OneDrive/Desktop/AI Dev Bootcamp/MCP lesson3/mcp-server",
        "run",
        "python",
        "main.py"
      ]
    }
  }
}
```

## 🔍 Como funciona a busca
O servidor indexa automaticamente o arquivo `fastmcp.zip`. Ele percorre todos os arquivos Markdown, remove os prefixos de diretório raiz para limpeza dos nomes e cria um índice vetorial em memória para consultas rápidas de alta relevância.

---
---
*Desenvolvido como parte do AI Dev Bootcamp.*

---

# FastMCP Documentation Search Server 🚀

This project is an MCP (Model Context Protocol) server built with **FastMCP** that includes an intelligent search tool for the FastMCP repository documentation.

## 📋 Features

- **`search_docs(query)`**: Search tool that uses TF-IDF (via `minsearch`) to find the 5 most relevant documents within the FastMCP documentation (`.md` and `.mdx`).
- **`add(a, b)`**: Simple tool to add two numbers.
- **`hash_text(text)`**: Generates a SHA-256 hash of a string.
- **`scrape_page(url)`**: Extracts content from a web page using Jina Reader.

## 🛠️ Tech Stack

- **FastMCP**: Framework for fast MCP server creation.
- **minsearch**: Minimalist search engine based on TF-IDF.
- **Scikit-learn & Pandas**: For text processing and vectorization.
- **Requests & Zipfile**: For handling external data and archives.

## 🚀 Getting Started

### Prerequisites
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended)

### Installation
1. Ensure dependencies are installed:
   ```bash
   uv sync
   ```

### Running Locally
To run the server in development mode:
```bash
uv run python main.py
```

### Usage in Claude Desktop
Add the following configuration to your `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
    "fastmcp-search": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/Users/UNIVERSO/OneDrive/Desktop/AI Dev Bootcamp/MCP lesson3/mcp-server",
        "run",
        "python",
        "main.py"
      ]
    }
  }
}
```

## 🔍 How Search Works
The server automatically indexes the `fastmcp.zip` file. It iterates through all Markdown files, removes root directory prefixes for path cleaning, and creates an in-memory vector index for high-relevance fast queries.

---
*Developed as part of the AI Dev Bootcamp.*
