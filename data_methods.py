import plotly.express as px
import pandas as pd
# from sklearn.preprocessing import StandardScaler
from collections import Counter

def convert_data_to_num(df,etiquet_new_column,etiquet):
    valores_df=df[etiquet].value.counts()
    df[etiquet_new_column]=df[etiquet]
    for index,label in enumerate(valores_df.index):
        for cont in range(0,len(df[etiquet]),1):
            df.loc[cont,etiquet_new_column]=int(index)
    return df

def histograma(df_t2,title_pd):
    cont_df=df_t2.value_counts()
    fig = px.histogram(df_t2,  nbins=len(cont_df.index), title=f'Histograma de {title_pd}')
    # Convierte la figura de Plotly en un formato adecuado para su representación en la plantilla HTML
    histogram = fig.to_html(full_html=False)
    return histogram

def obtener_data_pastel(df):
    # Contar las ocurrencias de cada categoría
    data_counts = Counter(df)
    vec=pd.DataFrame()
    # Obtener las categorías y sus conteos
    vec["keys"] = list(data_counts.keys())
    vec["values"] = list(data_counts.values())
    return vec

def pastel(df_t,title_pd):
    df_t2=obtener_data_pastel(df_t.copy())
    fig = px.pie(df_t2, values="values", names=df_t2["keys"] ,title=f'Grafico pastel de {title_pd}')

    # Convierte la figura de Plotly en un formato adecuado para su representación en la plantilla HTML
    pastel = fig.to_html(full_html=False)
    return pastel

def grafico_caja(df_t):
    fig= px.box(y=df_t)
    grafix_caja=fig.to_html(full_html=False)
    return grafix_caja