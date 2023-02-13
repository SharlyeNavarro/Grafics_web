from flask import Flask, render_template, request, make_response, redirect
import plotly.express as px
from graficos import generate_plot


app = Flask(__name__)

todos = ["Todo 1", "todo 2", "todo 3"]

@app.route('/f')
def home():
    return render_template('index.html')


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/')
def ip():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        "user_ip": user_ip,
        "todos": todos,
    }

    return render_template('hello.html', **context)


@app.route('/button')
def button():
    return render_template('button.html')
    if request.args.get('grafic'):
        generate_plot()
    

@app.route('/grafic')
def grafic():
    generate_plot()
    return render_template('grafic.html')


if __name__ == '__main__':
    app.run(debug=True)