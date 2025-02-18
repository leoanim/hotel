import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import os


def figure_med():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    df_total = pd.read_csv(os.path.join(current_dir, "statMed.csv"), sep=";")
    fig = px.line(df_total, x="date", y="median", markers=True, color_discrete_sequence = [ "#82DAD0"])
    return fig


def mediane_mois(df):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mediane = []
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
        mois = [i, df_mois["prices"].median()]
        mediane.append(mois)
    
    df_med = pd.DataFrame(data=mediane, columns=['date', 'median'])
    df_med.to_csv(os.path.join(current_dir, "statMed.csv"), index=False, sep=";")


# Commenté pour éviter l'exécution
#current_dir = os.path.dirname(os.path.abspath(__file__))
#df = pd.read_csv(os.path.join(current_dir, "test_carte.csv"), sep=";")
#mediane_mois(df)