import pandas as pd
import plotly.express as px
import numpy as np
from flask import Flask, request, make_response, redirect, Blueprint

post = Flask(__name__)
post_bp = Blueprint('post', __name__)

csv = pd.read_csv('static/csv/opt_gsh.csv')
owners = csv[['propietario', 'importe']]

def ovsw():
    fig = px.bar(csv, x="propietario", y="importe")
    fig.write_html("static/html/figure.html")
        
list_owner = csv['propietario'].unique()

@post.route('/generar-grafico', methods=['POST'])
def owner_select():
    valor_seleccionado = request.form['opciones']
    table_owners(valor_seleccionado)
    return redirect('/')

def table_owners(selected_owner):
    owner_data = owners.groupby('propietario').sum().reset_index()
    owner_data = owner_data[owner_data['propietario'] == selected_owner]
    owner_bar = px.bar(owner_data, x="propietario", y="importe")
    owner_bar_html = owner_bar.to_html(full_html=False)
    return owner_bar_html

if __name__ == '__main__':
    post.run(debug=True)