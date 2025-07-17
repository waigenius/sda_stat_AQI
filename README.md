```markdown
# Prédiction de la Qualité de l'Air : Londres et Dubaï

Ce dépôt contient le code et l'analyse pour la prédiction de l'Indice de Qualité de l'Air (IQA) à Londres et Dubaï. Le projet utilise des Modèles Linéaires Robustes (RLM) et l'analyse de séries temporelles (SARIMAX) pour comprendre les facteurs influençant l'IQA et prévoir les valeurs futures.

## Table des matières

- [Introduction](#introduction)
- [Méthodologie](#méthodologie)
- [Résultats et Discussion](#résultats-et-discussion)
- [Travaux futurs (Analyse de séries temporelles)](#travaux-futurs-analyse-de-séries-temporelles)
- [Limites et Perspectives](#limites-et-perspectives)
- [Sources de données](#sources-de-données)
- [Références](#références)
- [Contributeurs](#contributeurs)

## Introduction

[cite_start]La qualité de l'air est une préoccupation environnementale essentielle ayant un impact sur la santé publique[cite: 1]. [cite_start]Ce projet vise à prédire l'Indice de Qualité de l'Air (IQA) pour deux grandes villes, Londres et Dubaï, en identifiant les facteurs d'influence clés et en développant des modèles prédictifs[cite: 3, 4, 5]. [cite_start]L'analyse se concentre sur la compréhension des différences entre ces facteurs dans les deux villes et leur évolution dans le temps[cite: 42].

## Méthodologie

### Sources de données
[cite_start]Le projet utilise des données agrégées quotidiennement provenant de trois sources principales[cite: 44].

### Tests statistiques
* [cite_start]**ANOVA (Analyse de la Variance)**: Utilisé pour les tests statistiques[cite: 45].
* [cite_start]**Hypothèses nulles ($H_0$)**[cite: 46]:
    * [cite_start]$H_0.a$: Aucune des variables explicatives, qu'il s'agisse des concentrations de polluants atmosphériques ou des indicateurs météorologiques, n'a d'effet statistiquement significatif sur la variable dépendante `log_AQI`[cite: 47].
    * [cite_start]$H_0.b$: Les coefficients des variables explicatives sont stables au cours du temps (il n'y a pas de changement significatif des effets entre les deux périodes)[cite: 48, 49].
* [cite_start]**Hypothèses alternatives ($H_1$)**[cite: 50]:
    * [cite_start]$H_1.a$: Au moins une variable explicative, parmi les polluants ou les conditions météorologiques, exerce un effet significatif sur la qualité de l'air mesurée par `log_AQI`[cite: 51].
    * [cite_start]$H_1.b$: Au moins un coefficient diffère significativement entre les deux périodes[cite: 52].

### Sélection du modèle
[cite_start]Un **Modèle Linéaire Robuste (RLM)** a été choisi car il est moins sensible aux valeurs aberrantes (outliers) et aux violations des hypothèses classiques comme la normalité des erreurs[cite: 53].

### Équations du modèle

#### Londres
[cite_start]$Log AQI (Londres) = a_0 + a_1 \cdot PM2.5 + a_2 \cdot SO2 + a_3 \cdot Benzène + a_4 \cdot PRESSURE\_MAX\_MB + a_5 \cdot Toluène + a_6 \cdot HUMIDITY\_MAX\_PERCENT + a_7 \cdot PRECIP\_TOTAL\_DAY\_MM + a_8 \cdot O3 + a_9 \cdot WINDSPEED\_MAX\_KMH + a_{10} \cdot CLOUDCOVER\_AVG\_PERCENT + a_{11} \cdot weekday + a_{12} \cdot month + a_{13} \cdot saison\_hiver + a_{14} \cdot saison\_été + a_{15} \cdot saison\_printemps + a_{16} \cdot log\_AQI\_lag1$ [cite: 55, 56, 57, 58, 59]

#### Dubaï
[cite_start]$Log AQI (Dubaï) = a_0 + a_{1} \cdot PM2.5 + a_{2} \cdot SO2 + a_{3} \cdot HUMIDITY\_MAX\_PERCENT + a_{4} \cdot PRECIP\_TOTAL\_DAY\_MM + a_{5} \cdot O3 + a_{6} \cdot WINDSPEED\_MAX\_KMH + a_{7} \cdot CLOUDCOVER\_AVG\_PERCENT + a_{8} \cdot TimeIndex + a_{9} \cdot saison\_été + a_{10} \cdot log\_AQI\_lag1$ [cite: 60]


### Performance du Modèle Linéaire Robuste (RLM)

[cite_start]Les modèles RLM se sont avérés efficaces pour prédire l'IQA[cite: 147].

* [cite_start]**Londres**: $R^2 = 0.81$ [cite: 84, 147]
    * [cite_start]Le modèle explique 81% de la variance de l'IQA sur les données d'entraînement[cite: 137].
    * [cite_start]Il explique 78% de la variance sur les données de test non vues[cite: 137].
* [cite_start]**Dubaï**: $R^2 = 0.85$ [cite: 109, 147]
    * [cite_start]Le modèle explique 86% de la variance de l'IQA sur les données d'entraînement[cite: 137].
    * [cite_start]Il explique 82% de la variance sur les données de test non vues[cite: 137].

### [cite_start]Principaux facteurs identifiés [cite: 147]

* [cite_start]**Polluants**: PM2.5, SO2 [cite: 147]
* [cite_start]**Variables météorologiques**: Humidité, vent [cite: 147]
* [cite_start]**Effets saisonniers et temporels** [cite: 147]

### [cite_start]Comparaison entre Londres et Dubaï [cite: 134]

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

### [cite_start]Variabilité des effets [cite: 135, 136]

* [cite_start]Les facteurs influençant l'IQA ne sont pas stables dans le temps et varient entre Londres et Dubaï[cite: 135, 147].
* [cite_start]Leurs effets varient selon les saisons, les conditions météorologiques et les comportements humains[cite: 136, 147].

## Travaux futurs (Analyse de séries temporelles)

[cite_start]Pour prédire les valeurs futures de l'IQA à partir des données historiques[cite: 138], un modèle SARIMAX a été exploré.

### Observations clés pour l'analyse des séries temporelles

* [cite_start]Le **PM2.5** est un contributeur majeur à l'IQA[cite: 139].
* [cite_start]Une **corrélation positive de 78%** existe entre le PM2.5 et l'IQA[cite: 140].
* [cite_start]Ils présentent une évolution temporelle similaire[cite: 140].
* [cite_start]Le **modèle SARIMAX** avec la **méthode Jenkins Box** est utilisé pour la prévision des séries temporelles[cite: 140].


## Limites et Perspectives

### [cite_start]Limites [cite: 147]

* [cite_start]Données sur une seule année (2024)[cite: 147].
* [cite_start]Absence de variables comme le trafic ou les événements locaux[cite: 147].

### [cite_start]Perspectives [cite: 148]

* [cite_start]Étendre l'analyse à plusieurs années pour des séries temporelles plus longues[cite: 148].
* [cite_start]Tester des modèles d'apprentissage automatique (Machine Learning)[cite: 148].
* [cite_start]Appliquer la méthodologie à d'autres villes pour généraliser[cite: 148].

## Sources de données

* [cite_start]**Jeu de données sur la qualité de l'air 2024**: [https://www.kaggle.com/datasets/youssefelebiary/air-quality-2024](https://www.kaggle.com/datasets/youssefelebiary/air-quality-2024) [cite: 158]
* [cite_start]**Données météorologiques**: [https://www.historique-meteo.net/](https://www.historique-meteo.net/) [cite: 158]
* [cite_start]**Données sur le Toluène et le Benzène à Londres**: [https://uk-air.defra.gov.uk/data/](https://uk-air.defra.gov.uk/data/) [cite: 158]

## Références

* Gokmen, A., Ozyuguran, H. A., & Cekmecelioglu, D. (2012). "Time series analysis of air pollution data in Istanbul: An application of ARIMA models." [cite_start]Atmospheric Environment, 57, 107-113. [cite: 149, 150]
* Jacob, D. J., & Winner, D. A. (2009). "Effect of climate change on air pollution." [cite_start]Atmospheric Environment, 43(1), 51-64. [cite: 151]
* Luo, B., Sun, J., Li, Z., Sun, Z., & Chen, H. (2020). "Characteristics of air pollution in China during the COVID-19 epidemic based on air quality monitoring data." [cite_start]Science of The Total Environment, 730, 139049. [cite: 152, 153, 154]
* Shao, P., Chen, W., Zhang, M., Su, X., Ma, J., Wang, Z., & Wang, Y. (2018). "Characterization of O3 formation and its response to precursors under different meteorological conditions in Beijing, China." [cite_start]Atmospheric Research, 214, 219-231. [cite: 154, 155]
* WHO (World Health Organization). (2021). WHO global air quality guidelines: particulate matter (PM2.5 and PM10), ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide. [cite_start]World Health Organization. [cite: 156, 157]

## Contributeurs

* [cite_start]Patricia KOTO [cite: 14]
* [cite_start]Waï LEKONE ANTA [cite: 15]
```
