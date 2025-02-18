import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import os


def figure():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    df_total = pd.read_csv(os.path.join(current_dir, "stat.csv"), sep=";")
    fig = px.line(df_total, x="date", y="mean", markers=True, color_discrete_sequence = [ "#82DAD0"])
    return fig


def moyenne_mois(df):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    moyenne = []
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
        mois = [i, df_mois["prices"].mean()]
        moyenne.append(mois)
    
    df_moyenne = pd.DataFrame(data=moyenne, columns=['date', 'mean'])
    df_moyenne.to_csv(os.path.join(current_dir, "stat.csv"), index=False, sep=";")


# Commenté pour éviter l'exécution
#current_dir = os.path.dirname(os.path.abspath(__file__))
#df = pd.read_csv(os.path.join(current_dir, "test_carte.csv"), sep=";")
#moyenne_mois(df)

#df.loc[df['start_date']=='11-04-2022','start_date'] = "04-11-2022"
#df.loc[df['start_date']=='11-05-2022','start_date'] = "05-11-2022"
#df.to_csv(path+"/test_carte.csv", index = False,sep=";")

