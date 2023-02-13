from flask import Flask, render_template
import pandas as pd
import numpy as np
from plotly import __version__

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')
@app.route('/about')
def about():
    return 'About Page'






# Leer el archivo CSV usando pandas
df = pd.read_csv('./static/csv/DataFrame.csv')
# Usando plotly para crear un gráfico de barras
fig = df.iplot(kind="bar", x="importe", y="propietario", title="Grafico de barras")
# Mostrando el gráfico
fig.show()
@app.route('/grafic')
def grafic():
    return fig.show()


if __name__ == '__main__':
    app.run(debug=True)