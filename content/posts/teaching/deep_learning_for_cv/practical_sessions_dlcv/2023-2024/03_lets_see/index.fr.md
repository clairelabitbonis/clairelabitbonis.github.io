---
title: "DLCV2 | Tadaaaam !"
date: 2022-12-14T10:00:00+09:00
description: ""
summary: ""

draft: true
math: true 
highlight: true
hightlight_languages: ["python","bash"]

authors: ["Claire Labit-Bonis"]

hero: featured.png

tags: ["Teaching"]

menu:
  sidebar:
    name: "DLCV2 | Tadaaaam !"
    identifier: dlcv-practical-sessions-2023-2024-03
    parent: dlcv-2023-2024-practical
    weight: 30
---

## Présentation

Bonjour, bonjour ! Aujourd'hui, l'objectif est d'évaluer les performances de YOLOv8 sur le *dataset* qu'on a construit ensemble. On ne sera que deux encadrant.e.s pour les trois groupes, alors ça va être sportif. Mais YOLO, on a pas peur.

Comme indiqué dans le sujet de [présentation](https://clairelabitbonis.github.io/posts/teaching/deep_learning_for_cv/practical_sessions_dlcv/2023-2024/00_presentation/), vous devrez rendre début janvier une vidéo d'une dizaine de minutes qui décrit votre travail, et votre analyse des performances de YOLO sur le *dataset*.

Pour cela, vous allez aujourd'hui procéder à :
* une **analyse quantitative** des performances : interpréter des courbes de précision/rappel, des matrices de confusion, des temps de calcul, des tailles de réseau ;
* une **analyse qualitative** des performances : afficher les détections sur la base de *train*, de *test*, sur une nouvelle vidéo, sur de nouvelles images. Voir dans quels cas ça marche, dans quels cas ça marche pas ;

Ces analyses doivent être faites à un niveau **micro** où vous allez vous préoccuper de votre propre classe d'objet (celle que vous avez annotée) et comparer les différentes configurations de modèles, mais aussi à un niveau **macro** où vous allez vous comparer aux autres classes.

{{< alert type="danger" >}}
Il n'y a pas que ces analyses qui sont demandées pour le rendu. Il faut aussi parler du *dataset*, de votre propre expérience, etc. Regardez bien le sujet de [présentation](https://clairelabitbonis.github.io/posts/teaching/deep_learning_for_cv/practical_sessions_dlcv/2023-2024/00_presentation/).
{{< /alert >}}

Le sujet d'aujourd'hui est divisé en trois parties :
* [partie 1](#il-est-tres-beau-le-dataset) : un compte-rendu du *dataset* ainsi qu'une présentation des différents entrainements de YOLO, pour que vous puissiez avoir une vue globale des données, et si j'ai eu le temps je les aurai comparées au *dataset* de l'année précédente (on se voit dans seulement quelques heures, alors je pense honnêtement qu'on est laaaaaarge au niveau du temps qu'il me reste pour rédiger des choses...) ;
* [partie 2](#et-du-coup-ça-marche) : la description des scripts que j'ai écrits pour vous faciliter la vie, parce que je suis sympa ;
* [partie 3](#ce-que-vous-navez-pas-vu) : en vrac, ce que j'ai dû faire depuis la dernière séance pour qu'on ait un joli TP aujourd'hui.


## Il est TRES beau le *dataset*

### Répartition des classes

Ensemble, on a construit un TRES beau *dataset* qui nous permet de détecter plein de classes d'objets très utiles, bravo. On pourra par exemple automatiquement dire si on regarde un clip de JuL, de Damso, si on se balade en forêt à l'automne, ou si Dwayne Johnson se cache derrière un buisson - et ça, c'est vraiment super.

Le tableau ci-dessous indique le nombre d'images et la répartition des différentes classes entre les ensembles de *train*, *validation* et *test* :

 <center>

<img src="images/dataset_2023-2024.png" alt="Dataset" width="80%"/>

 </center>

Et en voilà une petite illustration :heart: :

 <center>

<img src="images/medley_dlcv_2023-2024.png" alt="Dataset" width="80%"/>

 </center>

### Analyse des labels
La quantité de labels par image et leur forme varie en fonction des classes annotées. Par exemple, les images de `prise` contiennent beaucoup plus d'instances que la classe `ballon`, pour un nombre équivalent d'images. Par ailleurs, et en mettant ça en regard de l'année passée, les objets ont globalement été plus répartis sur l'ensemble de l'image, là où ceux de l'année dernière étaient très au centre (figures en bas à gauche). Ma première intuition serait de dire que cette année on s'est accordés plus de libertés que l'année dernière sur le fait que les objets devaient être bien centrés, ne pas dépasser, etc. Un peu plus en mode *yolo* quoi.


On voit aussi que les labels de l'année dernière étaient en majorité verticaux, là où cette année on est un peu plus sur des boîtes horizontales (figures en bas à droite).

  <center>

<img src="images/labels_2022-2023.png" alt="Labels" width="45%"/>
<img src="images/labels_2023-2024.jpg" alt="Labels" width="45.1%"/>

 </center>


## Et du coup, ça marche ?

### Je suis sympa
