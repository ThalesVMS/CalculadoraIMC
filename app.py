from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_imc(peso, altura):
    imc = peso / altura**2
    return imc


def classificar_imc(imc):
    if imc < 17:
        return "Muito abaixo do peso"
    elif 17 <= imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Acima do peso"
    elif 30 <= imc < 35:
        return "Obesidade I"
    elif 35 <= imc < 40:
        return "Obesidade II (severa)"
    else:
        return "Obesidade III (mórbida)"


def calcular_peso_ideal(sexo, altura):
    if sexo.lower() == 'masculino':
        return (72.7 * altura) - 58
    elif sexo.lower() == 'feminino':
        return (62.1 * altura) - 44.7
    else:
        return "Sexo não reconhecido"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        sexo = request.form['sexo']

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        peso_ideal = calcular_peso_ideal(sexo, altura)

        return render_template('resultado.html', nome=nome, imc=imc, classificacao=classificacao, peso_ideal=peso_ideal)

    return render_template('formulario.html')


if __name__ == '__main__':
    app.run(debug=True)
