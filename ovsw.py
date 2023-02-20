import pandas as pd
import numpy as np
import plotly.express as px
from flask import Flask, request, Blueprint, render_template

post_bp = Blueprint('post', __name__)

csv = pd.read_csv('static/csv/opt_gsh.csv')
owners = csv[['propietario', 'importe']]

list_owner = csv['propietario'].unique()

@post_bp.route('/grafic_owner', methods=['POST'])
def grafic_owner():
    owner_select = request.form['opciones']
    target_amount = request.form['target_amount']
    arr = np.array([target_amount])
    df = pd.DataFrame({'propietario': ['Objetivo'],'importe': arr})
    owner_data = owners.groupby('propietario').sum().reset_index()
    owner_data = owner_data[owner_data['propietario'] == owner_select]
    table = pd.concat([owner_data, df])
    owner_bar = px.bar(table, x="propietario", y="importe")
    owner_bar.write_html('static/html/figure2.html')
    return render_template('grafic.html', list_owner=list_owner)
