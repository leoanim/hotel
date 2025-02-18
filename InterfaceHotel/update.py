import pandas as pd
from . import statMean
from . import statMedian
from . import statEtendu
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os


def update_table(stars_choice,date_choice,adulte_choice,enfant_choice,room_choice):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(os.path.join(current_dir, "test_carte.csv"), sep=";")
    df = df.drop(['gps'], axis=1)
    if stars_choice == 10:
        df = df
    else:
        df = df[(df['stars']==stars_choice)]
    if date_choice == "all" :
        df = df
    else:
        df = df[(df['start_date']==date_choice)]
    if adulte_choice == 10:
        df = df
    else:
        df = df[(df['nb_adulte']==adulte_choice)]
    if enfant_choice ==10:
        df = df
    else:
        df = df[(df['nb_enfant']==enfant_choice)]
    if room_choice == 10:
        df = df
    else:
        df = df[(df['nb_chambre']==room_choice)]
    df = df.drop(['nb_adulte','nb_enfant','nb_chambre'], axis=1)
    data=df.to_dict('records')
    return data

def update_graph(choice):
    if choice == "moyenne":
        fig=statMean.figure()
        return fig
    elif choice == "médiane":
        fig=statMedian.figure_med()
        return fig
    elif choice == "étendue":
        fig=statEtendu.figure_et()
        return fig