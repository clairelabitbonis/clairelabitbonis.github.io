---
title: "00 | Présentation"
date: 2022-11-04T10:00:00+09:00
description: ""
summary: ""

math: true 
highlight: true
hightlight_languages: ["python","bash"]

authors: ["Claire Labit-Bonis"]

hero: featured.png

tags: ["Teaching"]

menu:
  sidebar:
    name: "00 | Présentation"
    identifier: dlcv-practical-sessions-00
    parent: dlcv-practical-sessions
    weight: 10
---

## Objectifs pédagogiques

L'objectif de ces séances de travaux pratiques est de toucher à toutes les étapes de l'ingénierie du *deep learning*, à savoir :
- l'**acquisition** et l'**annotation** de données, 
- l'**apprentissage** de réseaux de convolution, 
- l'**évaluation** des performances de la tâche apprise,
- la **visualisation** des résultats obtenus.

Pour cela, notre point de départ sera le détecteur d'objets très largement connu et utilisé par les communautés scientifique mais aussi industrielle : [YOLO](https://arxiv.org/pdf/1506.02640.pdf) (You Only Look Once). Nous travaillerons avec la [version 5](https://github.com/ultralytics/yolov5) sortie en 2020. 

> A la fin des TPs, vous saurez comment utiliser YOLOv5, comment l'entrainer sur vos propres données, et comment l'évaluer. 

## Déroulement des séances

>**Un·e pour tou·te·s, tou·te·s pour un·e !**
>
>Parce que l'union fait la force, que la joie et la bonne humeur facilitent l'apprentissage -- des humains --, les séances de travaux pratiques se dérouleront dans un contexte à la fois collectif et individuel, pas toujours sur les postes de travail, et toujours dans l'intérêt de la compréhension. Nous aurons tou·te·s un rôle à jouer, à chacune des étapes.

Nous allons entrainer YOLOv5 à détecter plusieurs classes d'objets, à raison d'une classe d'objet par binôme. Le *dataset* que nous allons construire pour cela sera commun aux deux groupes de TPs qui se déroulent en parallèle (*e.g.*, groupes A1 \& A2, groupes B1 \& B2).

Pour cela, nous passerons par plusieurs étapes :

* <mark>**étape 1 - acquisition**</mark> : chaque binôme prendra plusieurs séquences vidéo de la classe d'objets qu'il aura choisie parmi une liste proposée, et la mettra sur un serveur de données commun aux groupes A1/A2 et B1/B2 ;
* <mark>**étape 2 - annotation**</mark> : avec l'outil CVAT, chaque binôme annotera ses propres séquences d'images avec la classe d'objet choisie, de sorte qu'à la fin de la phase d'annotation, le groupe entier de TP aura collectivement construit un *dataset* multi-classes dont tout le monde bénéficiera pour faire ses apprentissages ;
* <mark>**étape 3 - prise en main du code de YOLOv5**</mark> : à la fin de cette étape, vous saurez appliquer sur vos propres images un modèle YOLOv5-S pré-entrainé sur COCO, entrer dans l'architecture du réseau et identifier ses différentes couches et leurs dimensions, visualiser la sortie de détection obtenue, etc. Pour parvenir à cette prise en main, un jeu de "où est Charlie ?" vous sera proposé et vous poussera à décortiquer l'exécution du code pas à pas. Vous devrez par exemple répondre à des questions comme "quelle est la taille du tenseur en sortie de la couche 17 pour une image d'entrée de 512x512x3 ?" ;
* <mark>**étape 4 - apprentissage de YOLOv5 sur notre *dataset***</mark> : l'idéal pour analyser les performances d'un jeu de paramètres donné (résolution des images d'entrée, taille du réseau, taille de *batch*, etc.) est de lancer autant d'apprentissages que de configurations possibles et de les comparer ensuite pour sélectionner celle qui est la meilleure. On peut ensuite afficher sur un même graphe différentes tailles de modèles, pour différentes résolutions, et comparer leur rapidité d'exécution à la *mean average precision* qu'ils réalisent sur un *dataset* donné, par exemple :

![Comparaison des performances de YOLOv5 sur COCO](images/perfs_yolov5.png)
*Source : https://github.com/ultralytics/yolov5*

>Un apprentissage dure plusieurs heures. Pour pouvoir comparer toutes ces configurations, il faut soit disposer de plusieurs serveurs GPU puissants qui peuvent faire tourner en parallèle plusieurs configurations, soit disposer de beaucoup de temps et être patient... 
>
>**Et puis, un apprentissage, ça consomme de l'énergie.**
>
>Il n'est donc pas envisageable que chaque binôme lance un apprentissage pour chaque jeu de paramètres puis fasse une analyse comparative des résultats. 
>
>**MAIS !, l'union fait la force, une fois de plus.**
>
>Chaque binôme se positionnera donc sur une configuration donnée et lancera l'apprentissage associé sur le *dataset* du groupe de TP.

* <mark>**étape 5 - analyse des performances**</mark> : une fois tous les apprentissages faits, chaque binôme pourra évaluer les performances de sa propre configuration, analyser les résultats de manière quantitative, *i.e.*, avec des chiffres, et de manière qualitative, *i.e.*, avec une visualisation "à l'oeil" des cas d'erreur et des cas qui fonctionnent. Une évaluation comparative sera également réalisable, puisque tout le monde aura accès aux résultats obtenus par les autres binômes, au travers d'un *leaderboard* commun au groupe.

## Modalités d'évaluation

Chaque binôme produira une capsule vidéo (c'est-à-dire une séquence vidéo) d'environ 5~10 minutes. Bien sûr, la pertinence du contenu importe plus que la longueur de la capsule ; libre à vous donc de décider du temps qu'il vous faut pour aborder, par exemple :
* les statistiques de vos acquisitions (la classe choisie, les différents contextes d'acquisition, le nombre d'images annotées, la stratégie d'annotation, le temps passé, les difficultés rencontrées...) ;
* l'analyse quantitative de vos résultats (métriques de performance, nombre d'*epochs* pour converger, rapidité d'exécution du modèle, répartition de la performance sur les différentes classes d'objets, potentiel *overfitting*, comparaison des métriques aux autres configurations et interprétation de cette comparaison...) ;
* l'analyse qualitative de vos résultats (visualisation de l'exécution du modèle, performances selon le contexte d'acquisition, selon la qualité de l'annotation...) ;
* d'autres idées que vous pourriez avoir.

Vous l'aurez compris, l'évaluation de votre travail ne dépendra pas de la performance de votre apprentissage (et donc de la configuration qui vous aura été attribuée), mais plutôt de l'analyse que vous serez capable d'en faire.

## Outils du TP et configuration du *workspace*



### Fichier partagé pour les tâches communes



### IDE et clone de YOLOv5

### CVAT pour l'annotation

### Serveur de données pour le *dataset*





## Planning des séances

<center>

| Groupe 	|                                       Dates                                      	|             Salles             	|    Intervenant·e   	|
|:------:	|:--------------------------------------------------------------------------------:	|:-----------------------------:	|:------------------:	|
|   A1   	| 30/11/2022 \ 12h30 - 15h15 <br /> 07/12/2022 \ 09h30 - 12h15 <br /> 14/12/2022 \ 15h30 - 18h15 	| GEI-111-A <br /> GEI-109-A <br /> GEI-111-A 	| Claire LABIT-BONIS 	|
|   A2   	| 30/11/2022 \ 12h30 - 15h15 <br /> 07/12/2022 \ 09h30 - 12h15 <br /> 14/12/2022 \ 15h30 - 18h15 	| GEI-111-B <br /> GEI-109-B <br /> GEI-111-B 	| Smail AIT BOUHSAIN 	|
|   B1   	| 30/11/2022 \ 15h30 - 18h15 <br /> 07/12/2022 \ 15h30 - 18h15 <br /> 14/12/2022 \ 09h30 - 12h15 	| GEI-111-A <br /> GEI-111-A <br /> GEI-109-A 	| Claire LABIT-BONIS 	|
|   B2   	| 30/11/2022 \ 15h30 - 18h15 <br /> 07/12/2022 \ 15h30 - 18h15 <br /> 14/12/2022 \ 09h30 - 12h15 	| GEI-111-B <br /> GEI-111-B <br /> GEI-109-B 	|    Pierre MARIGO   	|

</center>
