import csv
from flask import Flask, render_template, request, url_for, redirect, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# --- Configuração do Gemini (INÍCIO) ---
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura sua chave de API do Gemini usando variável de ambiente
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Inicializa o modelo Gemini UMA ÚNICA VEZ ao iniciar o servidor
try:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    print("Modelo Gemini 1.5 Flash carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o modelo Gemini: {e}")
    model = None
# --- Configuração do Gemini (FIM) ---

@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/glossario')
def glossario():
    glossario_de_termos = []
    try:
        with open('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for t in reader:
                glossario_de_termos.append(t)
    except FileNotFoundError:
        print("Arquivo 'bd_glossario.csv' não encontrado. Criando um novo.")
        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as csvfile:
            pass
    return render_template('glossario.html', glossario=glossario_de_termos)

@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

# --- Rotas do Gemini (INÍCIO) ---
@app.route('/duvidas')
def duvidas():
    return render_template('duvidas.html')

@app.route('/ask_gemini', methods=['POST'])
def ask_gemini():
    if model is None:
        return jsonify({"error": "Modelo Gemini não carregado. Verifique a chave de API e o acesso ao modelo."}), 500

    data = request.get_json()
    pergunta = data.get('question')

    if not pergunta:
        return jsonify({"error": "Nenhuma pergunta fornecida."}), 400

    try:
        resposta = model.generate_content(pergunta)
        return jsonify({"answer": resposta.text})
    except Exception as e:
        print(f"Erro ao gerar conteúdo com Gemini: {e}")
        return jsonify({"error": f"Ocorreu um erro ao processar sua solicitação: {str(e)}"}), 500
# --- Rotas do Gemini (FIM) ---

if __name__ == '__main__':
    app.run(debug=True)
