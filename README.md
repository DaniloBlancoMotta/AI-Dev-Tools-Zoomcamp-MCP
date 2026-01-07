# FastMCP Search Server 🚀

Infraestrutura de **Acesso + Contexto** baseada no protocolo MCP. 
Este servidor fornece ferramentas locais para Agentes de IA, sem depender de APIs externas para processamento de dados.

## 🛠 Tools
- `search_docs`: Busca semântica local via TF-IDF (minsearch).
- `scrape_page`: Markdown limpo de qualquer URL via Jina Reader.
- `hash_text`: Integridade de dados via SHA-256 local.
- `add`: Precisão matemática garantida pelo servidor.

## 🏗 Fluxo
1. **User Request** -> Client (MCP Host)
2. **Client Interface** <-> **FastMCP Server** (Local Tools)
3. **Context Injection** -> Resposta precisa e validada.

## 💻 Tech
- FastMCP | minsearch | Scikit-learn | Jina Reader

---
*Desenvolvido como parte do AI Dev Bootcamp por um Engenheiro de IA e Cientista de Dados.*
