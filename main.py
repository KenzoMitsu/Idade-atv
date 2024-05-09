from flask import Flask, render_template, request

app = Flask(__name__) # Inicializa a aplicação Flask

@app.route('/') # Define a rota do programa para a página inicial (main.py)
def index():
    return render_template('index.html') # Renderiza o template denominado 'index.html' para a página inicial

@app.route('/resultado', methods=['POST']) #Define o método de exportação do conteúdo do main.py para o index.html
def resultado():
    idade = int(request.form["numero"]) #Converte o valor de um campo do formulário em um número inteiro

    if idade <= 5:
        verificar = "Bebê"
    elif idade > 5 and idade <= 15:
        verificar = "Criança"
    elif idade > 15 and idade <= 18:
        verificar = "Marmanjos hora de trabalhar"
    elif idade > 18 and idade <= 60:
        verificar = "Acorda pra vida, que você tem boleto pra pagar"
    else:
        verificar = "Daqui pra frente e só pra traz"

    return render_template('index.html', resultado=verificar) #Retorna as informações enviadas pelo remetente de volta à ele, no caso o index.html

if __name__ == '__main__': #Condição de inicialização do programa
    app.run(debug=True) #Ação de inicialização do programa (app.run)