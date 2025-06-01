# Projeto_Messias

# 💡 Projeto Messias

![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue?utm_source=chatgpt.com)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![Gemini](https://img.shields.io/badge/Gemini-1.5_Flash-lightgrey?logo=google)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)

Aplicação web desenvolvida com **Python** e **Flask**, com o objetivo de apresentar um **glossário interativo**, além de uma funcionalidade de **resposta automática via IA** utilizando o modelo **Gemini 1.5 Flash**, da Google.

---

## 📁 Estrutura do Site

- **`/` Página Principal**  
  Apresenta uma mensagem de boas-vindas com botões de navegação para as outras seções.

- **`/equipe` Equipe**  
  Mostra as informações dos integrantes do projeto.

- **`/glossario` Glossário**  
  Lista todos os termos armazenados no arquivo `bd_glossario.csv`.

- **`/novo_termo` Novo Termo**  
  Página com formulário para adicionar um novo termo e sua definição.

- **`/criar_termo` Criar Termo**  
  Rota POST para processar o formulário e gravar os dados no arquivo CSV.

- **`/duvidas` Dúvidas**  
  Interface onde o usuário pode fazer perguntas e receber respostas da IA Gemini.

- **`/ask_gemini` API do Gemini**  
  Rota POST que recebe a pergunta em JSON, envia ao Gemini e retorna a resposta.

---

## 📦 Tecnologias Utilizadas

- **Back-end:**
  - Python
  - Flask (`render_template`, `request`, `redirect`, `url_for`, `jsonify`)
  - CSV (para leitura e escrita de dados)
  - `dotenv` (para variáveis de ambiente)
  - `google-generativeai` (API do Gemini)

- **Front-end:**
  - HTML (templates do Flask usando Jinja2)

---

## 🤖 Integração com o Gemini

A aplicação se conecta à API da Google para usar o modelo de linguagem **Gemini 1.5 Flash**. Essa integração permite responder a perguntas enviadas pelo usuário de forma inteligente.

### Configuração:

1. **Instale a biblioteca:**
   ```bash
   pip install google-generativeai
   ```

2. **Crie o arquivo `.env`:**
   ```
   GOOGLE_API_KEY=sua_chave_api_aqui
   ```

3. **No código:**
   - Carregamento da chave:
     ```python
     from dotenv import load_dotenv
     load_dotenv()
     genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
     ```

   - Inicialização do modelo uma única vez:
     ```python
     model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
     ```

   - Rota de API para receber perguntas e retornar respostas:
     ```python
     @app.route('/ask_gemini', methods=['POST'])
     def ask_gemini():
         data = request.get_json()
         pergunta = data.get('question')
         resposta = model.generate_content(pergunta)
         return jsonify({"answer": resposta.text})
     ```

---

## 💾 Armazenamento com CSV

Todos os termos do glossário são armazenados em um arquivo local chamado `bd_glossario.csv`.

- **Leitura:** ao acessar a rota `/glossario`, o sistema carrega os dados do arquivo.
- **Escrita:** ao enviar um novo termo via formulário, ele é salvo com `csv.writer`.
- **Criação automática:** caso o arquivo não exista, ele será criado automaticamente na primeira execução.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-messias.git
   cd projeto-messias
   ```

2. Instale as dependências:
   ```bash
   pip install flask python-dotenv google-generativeai
   ```

3. Crie um arquivo `.env` e adicione sua chave da API:
   ```
   GOOGLE_API_KEY=sua_chave_api
   ```

4. Execute o servidor:
   ```bash
   python app.py
   ```

5. Acesse no navegador:
   ```
   http://localhost:5000
   ```

---

## 👥 Equipe

- Eulyna Cristina  
- Lenilson Pereira  
- Kevin Simpson

---

## 📄 Licença

Este projeto é de uso **educacional** e está sob a licença MIT.  
Você pode usá-lo livremente para fins de aprendizado e projetos acadêmicos.

---

## 📬 Contato

Caso tenha dúvidas ou sugestões, entre em contato com a equipe ou abra uma *issue* aqui no GitHub.