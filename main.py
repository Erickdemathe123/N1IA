from flask import Flask, request, render_template

app = Flask(__name__)


# Rota para a página inicial (home)
@app.route('/')
def home():
    return render_template('home.html')


# Rota para a página de pesquisa (formulário)
@app.route('/pesquisa')
def pesquisa():
    return render_template('index.html')


@app.route('/processar', methods=['POST'])
def processar():
    # Captura os dados do formulário
    temperatura = float(request.form['temperatura'])
    umidade = float(request.form['umidade'])
    tipo_solo = request.form['tipo_solo']
    exposicao_solar = request.form['exposicao_solar']
    mes = request.form['mes']

    # Organiza os dados em um dicionário
    dados = {
        'temperatura': temperatura,
        'umidade': umidade,
        'tipo_solo': tipo_solo,
        'exposicao_solar': exposicao_solar,
        'mes': mes
    }

    # Aplica as regras para gerar recomendações
    recomendacoes = aplicar_regras(dados)

    # Renderiza o template com as recomendações
    return render_template('index.html', recomendacoes=recomendacoes)


def aplicar_regras(dados):
    recomendacoes = []

    # Regras para temperatura
    if dados['temperatura'] > 30:
        recomendacoes.append("Regar com mais frequência devido à alta temperatura.")
    elif dados['temperatura'] < 15:
        recomendacoes.append("Reduzir a frequência de rega devido à baixa temperatura.")

    # Regras para umidade
    if dados['umidade'] < 40:
        recomendacoes.append("Aumentar a umidade do ambiente.")

    # Regras para exposição solar
    if dados['exposicao_solar'] == "alta":
        recomendacoes.append("Proteger a planta da exposição excessiva ao sol.")
    elif dados['exposicao_solar'] == "baixa":
        recomendacoes.append("Garantir maior exposição ao sol.")

    # Regras para tipo de solo
    if dados['tipo_solo'] == "arenoso":
        recomendacoes.append("Solo arenoso drena rapidamente, regue com maior frequência.")
    elif dados['tipo_solo'] == "argiloso":
        recomendacoes.append("Solo argiloso retém água, evite regar em excesso.")
    elif dados['tipo_solo'] == "humoso":
        recomendacoes.append("Solo humoso é bem balanceado, continue monitorando.")
    elif dados['tipo_solo'] == "siltoso":
        recomendacoes.append("Solo siltoso retém umidade, tenha cuidado com a irrigação.")
    elif dados['tipo_solo'] == "calcário":
        recomendacoes.append("Solo calcário tende a ser alcalino, adicione compostos orgânicos.")

    # Sugestão de plantio com base no mês
    mes = dados.get('mes', '').lower()
    if mes in ["setembro", "outubro", "novembro"]:
        recomendacoes.append("Esta é uma ótima época para plantar flores e hortaliças.")
    elif mes in ["dezembro", "janeiro", "fevereiro"]:
        recomendacoes.append("Época quente, ideal para plantas tropicais.")
    elif mes in ["março", "abril", "maio"]:
        recomendacoes.append("Época amena, ideal para plantar árvores frutíferas.")
    elif mes in ["junho", "julho", "agosto"]:
        recomendacoes.append("Mês frio, bom para plantas de inverno e flores resistentes.")

    return recomendacoes


if __name__ == '__main__':
    app.run(debug=True)
