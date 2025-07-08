import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def setup_plot():
    sns.set_theme(style="whitegrid")
    return ["#004aad", "#2bb4d4", "#2e2e2e", "#5ce1e6"]


def plot_data(
    X, y, colors, preds= None
):
    plt.figure(figsize=(12, 8))

    print(f"Shape de x : {X.shape}")
    print(f"Shape de y : {y.shape}")

    plt.scatter(X, y, color=colors[0], label="Données")
    plt.xlabel("X")
    plt.ylabel("y")
    if preds is not None:
        plt.plot(X, preds, color=colors[1], label="Prediction")
        plt.title("Prédiction du modèle")
    else:
        plt.title("Target vs features")

    plt.legend()
    plt.grid(True)

    plt.savefig('mon_graphique.png') 
    #plt.show()