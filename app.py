from flask import Flask, render_template, make_response
import pandas as pd
from data_methods import histograma,pastel

import plotly.express as px
from io import BytesIO


app = Flask(__name__)
df=pd.read_csv("./static/data/Base_de_Prestadores_de_Servicios_Tur_sticos__SITUR__-_DEPARTAMENTO_DE_BOYAC_.csv")
# df=pd.read_csv("/home/juan/Documentos/POSGRADO/administracion de bases de datos/aplicacion_web_proyecto/codigo/app/static/datos_agrupados_proyecto.csv")
df_definitivo=df[['Numero del RNT','Municipio', 'Departamento', 'Nombre Comercial', 'Categoria', 'Subcategoria', 'Direccion Comercial','Correo Electronico', 'Habitaciones', 'Camas', 'Empleados']]
# print(df_definitivo.columns)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tablas")
def tablas():
    return  render_template("tablas.html", dataframe=df_definitivo, h1_page=" general" )




@app.route("/graficos")
def graficos():
    df_t2=df_definitivo["Departamento"]
    title_pd="general"
    histogram=histograma(df_t2,title_pd)
    grafico_pastel=pastel(df_t2,title_pd)
    return render_template("graficas.html",h1_page=title_pd,histogram=histogram,grafico_pastel=grafico_pastel)

if __name__ == '__main__':
    app.run(debug=True)