from flask import Flask, render_template, request, make_response, redirect
from graficos import generate_plot
from ovsw import post_bp,list_owner

app = Flask(__name__)
app.register_blueprint(post_bp)

@app.route('/')
def button():
    return render_template('layout.html', list_owner=list_owner)


@app.route('/ovsw')
def ovsw_render():
    return render_template('grafic.html')

if __name__ == '__main__':
    app.run(debug=True)
