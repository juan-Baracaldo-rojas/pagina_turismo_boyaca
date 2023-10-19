from flask import Flask, render_template, make_response
import pandas as pd
from collections import Counter
import plotly.express as px
from io import BytesIO


app = Flask(__name__)
df=pd.read_csv("./static/data/Base_de_Prestadores_de_Servicios_Tur_sticos__SITUR__-_DEPARTAMENTO_DE_BOYAC_.csv")
# df=pd.read_csv("/home/juan/Documentos/POSGRADO/administracion de bases de datos/aplicacion_web_proyecto/codigo/app/static/datos_agrupados_proyecto.csv")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)