import plotly.express as px
import pandas as pd


def generate_plot():
    csv = pd.read_csv('static/csv/DataFrame.csv')

    # Leemos el archivo CSV en un DataFrame de Pandas
    df = csv

    # Generamos un gráfico de barras a partir del DataFrame
    fig = px.bar(df, x="propietario", y="importe")

    # Guardamos la figura en un archivo HTML
    fig.write_html("static/html/figure.html")

