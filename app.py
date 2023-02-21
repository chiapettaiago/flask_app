from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Verifique as credenciais do usuário
    if username == 'Iago' and password == 'eduardaamor15':
        # Se as credenciais forem válidas, redirecione para a página de dashboard
        return redirect(url_for('dashboard'))
    else:
        # Se não, exiba uma mensagem de erro e redirecione para a página de login
        return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
