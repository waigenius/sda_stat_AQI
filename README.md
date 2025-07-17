# Prédiction de la Qualité de l'Air : Londres et Dubaï

Ce dépôt contient le code et l'analyse pour la prédiction de l'Indice de Qualité de l'Air (IQA) à Londres et Dubaï. Le projet utilise des Modèles Linéaires Robustes (RLM) pour comprendre les facteurs influençant l'AQI.

## Méthodologie

### Sources de données
Le projet utilise des données agrégées quotidiennement provenant de trois sources principales

### Hypothèses
* **Hypothèses nulles ($H_0$)**:
    * $H_0.a$: Aucune des variables explicatives, qu'il s'agisse des concentrations de polluants atmosphériques ou des indicateurs météorologiques, n'a d'effet statistiquement significatif sur la variable dépendante `log_AQI`.
    * $H_0.b$: Les coefficients des variables explicatives sont stables au cours du temps (il n'y a pas de changement significatif des effets entre les deux périodes).
* **Hypothèses alternatives ($H_1$)**:
    * $H_1.a$: Au moins une variable explicative, parmi les polluants ou les conditions météorologiques, exerce un effet significatif sur la qualité de l'air mesurée par `log_AQI`.
    * $H_1.b$: Au moins un coefficient diffère significativement entre les deux périodes.

### Sélection du modèle
Un **Modèle Linéaire Robuste (RLM)** a été choisi car il est moins sensible aux valeurs aberrantes (outliers) et aux violations des hypothèses classiques comme la normalité des erreurs.

### Équations du modèle

#### Londres
$Log AQI (Londres) = a_0 + a_1 \cdot PM2.5 + a_2 \cdot SO2 + a_3 \cdot Benzène + a_4 \cdot PRESSURE\_MAX\_MB + a_5 \cdot Toluène + a_6 \cdot HUMIDITY\_MAX\_PERCENT + a_7 \cdot PRECIP\_TOTAL\_DAY\_MM + a_8 \cdot O3 + a_9 \cdot WINDSPEED\_MAX\_KMH + a_{10} \cdot CLOUDCOVER\_AVG\_PERCENT + a_{11} \cdot weekday + a_{12} \cdot month + a_{13} \cdot saison\_hiver + a_{14} \cdot saison\_été + a_{15} \cdot saison\_printemps + a_{16} \cdot log\_AQI\_lag1$ 

#### Dubaï
$Log AQI (Dubaï) = a_0 + a_{1} \cdot PM2.5 + a_{2} \cdot SO2 + a_{3} \cdot HUMIDITY\_MAX\_PERCENT + a_{4} \cdot PRECIP\_TOTAL\_DAY\_MM + a_{5} \cdot O3 + a_{6} \cdot WINDSPEED\_MAX\_KMH + a_{7} \cdot CLOUDCOVER\_AVG\_PERCENT + a_{8} \cdot TimeIndex + a_{9} \cdot saison\_été + a_{10} \cdot log\_AQI\_lag1$ 


### Performance du Modèle Linéaire Robuste (RLM)

Les modèles RLM se sont avérés efficaces pour prédire l'IQA.

* **Londres**: $R^2 = 0.81$ [cite: 84, 147]
    * Le modèle explique 81% de la variance de l'IQA sur les données d'entraînement.
    * Il explique 78% de la variance sur les données de test non vues.
* **Dubaï**: $R^2 = 0.85$ 
    * Le modèle explique 86% de la variance de l'IQA sur les données d'entraînement.
    * Il explique 82% de la variance sur les données de test non vues.

### Principaux facteurs identifiés

* **Polluants**: PM2.5, SO2 
* **Variables météorologiques**: Humidité, vent 
* **Effets saisonniers et temporels** 

### Comparaison entre Londres et Dubaï :
| Variable                 | Londres (Coef.) | Dubaï (Coef.) | Interprétation                                          |
| :----------------------- | :------------- | :------------ | :------------------------------------------------------ |
| `const`                  | 1.780          | 1.265         | Plus grande constante à Londres                 |
| `PM2.5`                  | 0.010          | 0.007         | Effet significatif dans les deux villes           |
| `SO2`                    | -0.003         | -0.009        | Effet négatif, plus marqué à Dubaï |
| `HUMIDITY_MAX_PERCENT`   | 0.002          | 0.002         | Effet comparable                           |
| `PRECIP_TOTAL_DAY_MM`    | 0.005          | -0.009        | Effet opposé : positif à Londres       |
| `O3`                     | -0.0004        | 0.0001        | Effet négatif à Londres, quasi nul à Dubaï |
| `WINDSPEED_MAX_KMH`      | 0.0004         | 0.0008        | Effet très faible                            |
| `CLOUDCOVER_AVG_PERCENT` | 0.001          | 0.001         | Effet similaire                              |
| `TimeIndex`              | 0.000013       | 0.000035      | Effet faible mais positif                    |
| `saison_été`             | 0.046          | 0.054         | Effet saisonnier significatif dans les deux villes |
| `log_AQI_lag1`           | 0.494          | 0.485         | Forte persistance de l'AQI                    |

### cite_start]Variabilité des effets

* Les facteurs influençant l'IQA ne sont pas stables dans le temps et varient entre Londres et Dubaï.
* cite_start]Leurs effets varient selon les saisons, les conditions météorologiques et les comportements humains.


## Limites et Perspectives

### Limites 
* Données sur une seule année (2024).
* Absence de variables comme le trafic ou les événements locaux.

### Perspectives

* Étendre l'analyse à plusieurs années pour des séries temporelles plus longues.
* Tester des modèles d'apprentissage automatique (Machine Learning).
* Appliquer la méthodologie à d'autres villes pour généraliser.

## Sources de données

* **Jeu de données sur la qualité de l'air 2024**: [https://www.kaggle.com/datasets/youssefelebiary/air-quality-2024](https://www.kaggle.com/datasets/youssefelebiary/air-quality-2024) 
* **Données météorologiques**: [https://www.historique-meteo.net/](https://www.historique-meteo.net/)
* **Données sur le Toluène et le Benzène à Londres**: [https://uk-air.defra.gov.uk/data/](https://uk-air.defra.gov.uk/data/) 

## Références

* Gokmen, A., Ozyuguran, H. A., & Cekmecelioglu, D. (2012). "Time series analysis of air pollution data in Istanbul: An application of ARIMA models." [cite_start]Atmospheric Environment, 57, 107-113. 
* Jacob, D. J., & Winner, D. A. (2009). "Effect of climate change on air pollution." [cite_start]Atmospheric Environment, 43(1), 51-64. [cite: 151]
* Luo, B., Sun, J., Li, Z., Sun, Z., & Chen, H. (2020). "Characteristics of air pollution in China during the COVID-19 epidemic based on air quality monitoring data." [cite_start]Science of The Total Environment, 730, 139049. 
* Shao, P., Chen, W., Zhang, M., Su, X., Ma, J., Wang, Z., & Wang, Y. (2018). "Characterization of O3 formation and its response to precursors under different meteorological conditions in Beijing, China." Atmospheric Research, 214, 219-231.
* WHO (World Health Organization). (2021). WHO global air quality guidelines: particulate matter (PM2.5 and PM10), ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide. [cite_start]World Health Organization. 

## Contributeurs

* Patricia KOTO 
* Waï LEKONE ANTA 
