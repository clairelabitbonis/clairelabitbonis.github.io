---
title: "00 | Présentation"
date: 2022-07-16
description: ""
summary: ""

math: true 
highlight: true
hightlight_languages: ["python","bash"]

authors: ["Claire Labit-Bonis"]

# hero: featured.png

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

Pour cela, notre point de départ sera le détecteur d'objets très largement connu et utilisé par les communautés scientifique mais aussi industrielle : YOLO (You Only Look Once). Nous travaillerons avec la [version 5](https://github.com/ultralytics/yolov5) sortie en 2020. 

> A la fin des TPs, vous saurez comment utiliser YOLOv5, comment l'entrainer sur vos propres données, et comment l'évaluer. 

## Outils du TP et configuration du *workspace*


## Déroulement des séances

>**Un·e pour tou·te·s, tou·te·s pour un·e !**
>
>Parce que l'union fait la force et que la joie facilite l'apprentissage -- des humains --, les séances de travaux pratiques se dérouleront dans un contexte à la fois collectif et individuel, pas toujours sur les postes de travail, et toujours dans l'intérêt de la compréhension. Nous aurons tou·te·s un rôle à jouer, à chacune des étapes.

Nous allons entrainer YOLOv5 à détecter plusieurs classes d'objets, à raison d'une classe d'objet par binôme. Le *dataset* que nous allons construire pour cela sera commun aux deux groupes de TPs qui se déroulent en parallèle (*e.g.*, groupes A1 \& A2, groupes B1 \& B2).

Pour cela, nous passerons par plusieurs étapes, dont voici les grandes lignes :

* <mark>**étape 1 - acquisition**</mark> : chaque binôme prendra plusieurs séquences vidéo de la classe d'objets qu'il aura choisie parmi une liste proposée, et la mettra sur un serveur de données commun aux groupes A1/A2 et B1/B2 ;
* <mark>**étape 2 - annotation**</mark> : avec l'outil CVAT, chaque binôme annotera ses propres séquences d'images avec la classe d'objet choisie, de sorte qu'à la fin de la phase d'annotation, le groupe entier de TP aura collectivement construit un *dataset* multi-classes dont tout le monde bénéficiera pour faire ses apprentissages ;
* <mark>**étape 3 - prise en main du code de YOLOv5**</mark> : à la fin de cette étape, vous saurez appliquer sur vos propres images un modèle YOLOv5-s pré-entrainé sur COCO, entrer dans l'architecture du réseau et identifier ses différentes couches et leurs dimensions, visualiser la sortie de détection obtenue, etc. Pour parvenir à cette prise en main, un jeu de "où est Charlie ?" vous sera proposé et vous poussera à décortiquer l'exécution du code pas à pas. Vous devrez par exemple répondre à des questions comme "quelle est la taille du tenseur en sortie de la couche 17 pour une image d'entrée de 512x512x3 ?" ;
* <mark>**étape 4 - apprentissage de YOLOv5 sur notre *dataset***</mark> : 
* <mark>**étape 5 - analyse des performances**</mark> : 



#### Un *leaderboard* par groupe


## Modalités d'évaluation



## Planning des séances

<center>

| Groupe 	|                                       Dates                                      	|             Salles             	|    Intervenant·e   	|
|:------:	|:--------------------------------------------------------------------------------:	|:-----------------------------:	|:------------------:	|
|   A1   	| 30/11/2022 \ 12h30 - 15h15 <br /> 07/12/2022 \ 09h30 - 12h15 <br /> 14/12/2022 \ 15h30 - 18h15 	| GEI-111-A <br /> GEI-109-A <br /> GEI-111-A 	| Claire LABIT-BONIS 	|
|   A2   	| 30/11/2022 \ 12h30 - 15h15 <br /> 07/12/2022 \ 09h30 - 12h15 <br /> 14/12/2022 \ 15h30 - 18h15 	| GEI-111-B <br /> GEI-109-B <br /> GEI-111-B 	| Smail AIT BOUHSAIN 	|
|   B1   	| 30/11/2022 \ 15h30 - 18h15 <br /> 07/12/2022 \ 15h30 - 18h15 <br /> 14/12/2022 \ 09h30 - 12h15 	| GEI-111-A <br /> GEI-111-A <br /> GEI-109-A 	| Claire LABIT-BONIS 	|
|   B2   	| 30/11/2022 \ 15h30 - 18h15 <br /> 07/12/2022 \ 15h30 - 18h15 <br /> 14/12/2022 \ 09h30 - 12h15 	| GEI-111-B <br /> GEI-111-B <br /> GEI-109-B 	|    Pierre MARIGO   	|

</center>
