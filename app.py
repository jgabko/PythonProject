# 1. Importações Essenciais
from flask import Flask, render_template, request
from Model.personagem import *
from Model import regras

# 2. Inicialização do Aplicativo Flask
app = Flask(__name__)

# 3. Definição da Rota Principal
@app.route('/', methods=['GET', 'POST'])
def index():
    # Verifica se o formulário foi enviado (método POST)
    if request.method == 'POST':
        # 4. Coleta dos Dados do Formulário
        nome = request.form.get('nome')
        raca = request.form.get('raca')
        classe = request.form.get('classe')
        metodo_atributos = request.form.get('metodo_atributos')

        # 5. Lógica para Gerar Atributos (Usando o Model)
        # Chama a função correta do arquivo 'regras.py' com base na escolha do usuário
        if metodo_atributos == 'classico':
            atributos = regras.gerar_atributos_classico()
        elif metodo_atributos == 'heroico':
            atributos = regras.gerar_atributos_heroico()
        else: # O padrão será 'aventureiro'
            atributos = regras.gerar_atributos_aventureiro()

        # 6. Criação do Objeto Personagem (Usando o Model)
        # Instancia a classe Personagem com os dados coletados e gerados
        novo_personagem = Personagem(nome, raca, classe, atributos)

        # 7. Renderização da Resposta (Enviando para a View)
        # Envia o objeto 'novo_personagem' para o template 'personagens.html' para ser exibido
        return render_template('personagens.html', personagem=novo_personagem) # <-- FIX: Corrected template name

    # Se a página for apenas carregada (método GET)
    else:
        # 8. Preparação da Página Inicial
        # Busca as listas de raças e classes para preencher as opções no formulário
        racas = regras.obter_racas()
        classes = regras.obter_classes()
        # Renderiza o formulário inicial ('index.html') passando as listas
        return render_template('index.html', racas=racas, classes=classes)

# 9. Execução do Servidor
if __name__ == '__main__':
    # Roda o servidor em modo de depuração para facilitar o desenvolvimento
    app.run(debug=True)