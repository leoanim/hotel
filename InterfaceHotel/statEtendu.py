import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import os


def figure_et():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    df_total = pd.read_csv(os.path.join(current_dir, "statEtendu.csv"), sep=";")
    fig = px.line(df_total, x="date", y=["etendu", "max", "min"], markers=True, 
                  color_discrete_sequence=["#82DAD0", "#FFC300", "#DAF7A6"])
    return fig


def etendu_mois(df):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    et = []
    # Créer une copie du DataFrame pour éviter la modification en place
    df_copy = df.copy()
    # Filtrer les prix <= 20 sans modifier le DataFrame original
    df_copy = df_copy[df_copy['prices'] > 20]
    
    list_mois = df_copy['start_date'].unique()
    for i in range(len(list_mois)):
        list_mois[i] = datetime.datetime.strptime(list_mois[i], "%m-%d-%Y")
    list_mois = sorted(list_mois)
    for i in range(len(list_mois)):
        list_mois[i] = datetime.datetime.strftime(list_mois[i], "%m-%d-%Y")
    
    for i in list_mois:
        df_mois = df_copy[df_copy['start_date'] == i][['start_date', 'prices']]
        max_price = df_mois["prices"].max()
        min_price = df_mois["prices"].min()
        etendue = max_price - min_price
        et.append([i, etendue, max_price, min_price])
    
    df_etendu = pd.DataFrame(data=et, columns=['date', 'etendu', 'max', 'min'])
    df_etendu.to_csv(os.path.join(current_dir, "statEtendu.csv"), index=False, sep=";")


# Commenté pour éviter l'exécution
#current_dir = os.path.dirname(os.path.abspath(__file__))
#df = pd.read_csv(os.path.join(current_dir, "test_carte.csv"), sep=";")
#etendu_mois(df)