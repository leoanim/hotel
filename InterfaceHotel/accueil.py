from dash import html
import base64
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
image_filename = os.path.join(current_dir, 'sunset-view-to-denfense-in-paris-france.jpg')
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

accueil = html.Div([
        html.Div([
                html.P("Sur ce site vous pouvez consulter sous différentes formes des données sur les hotels à Paris", style={'font-size':'20px','font-weight':'bold'}),
                html.P("Dans l'onglet 'Recherche', vous pouvez afficher les hotels correspondants à vos critères, selon le nombre d'étoiles, la date de départ, le nombre d'adultes, d'enfants et de chambre", style={'textAlign':'center'}),
                html.P("Dans l'onglet 'Statistique', vous pouvez afficher les graphes des moyennes, médianes et étendue des prix selon les mois", style={'textAlign':'center'}),
                html.P("Dans l'onglet 'Carte', vous pouvez afficher la carte des hotels à Paris", style={'textAlign':'center'}),
        ]),
        html.Img(src="data:image/jpg;base64,{}".format(encoded_image.decode()),style={'textAlign':'center','width':'100%', 'height':'50%'})
])