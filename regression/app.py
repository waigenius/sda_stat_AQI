import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
from utils import setup_plot, plot_data
from hypothesis.hypothesis_checker import check_all_hypotheses, format_check_report

if __name__ == "__main__":

    # Chargement de la plalette de couleur
    colors = setup_plot()
    
    # Chargement du dataset
    df = pd.read_csv('AQI_london.csv')
   

    target_column = 'AQI'

    # Colonne non nécessaire pour l'entrainement du modèle
    date_column = 'DATE'
    opinion_column = 'OPINION' # labellisé

    # Séparation des données en X et y
    y = df[target_column]
    X = df.drop(columns=[target_column, date_column, opinion_column])

   

    # Application du model
    modified_X = sm.add_constant(data=X)

    # Moindre Carrées Ordinaire (OLS)
    model = sm.OLS(endog=y, exog=modified_X)
    model = model.fit()

    print(model.summary())

    # Prédiction
    preds = model.predict(modified_X)

    #plot_data(X=X['PM2.5'], y=y, colors=colors, preds=preds)

    hypotheses = check_all_hypotheses(X, y, model)
    report = format_check_report(hypotheses)
    
    print(report)