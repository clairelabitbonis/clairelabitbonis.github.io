---
title: "DLCV2 | All you need is data"
date: 2022-11-04T10:00:00+09:00
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
    name: "01 | All you need is data"
    identifier: dlcv-practical-sessions-2023-2024-01
    parent: dlcv-2023-2024-practical
    weight: 10
---

Tout ce dont vous avez besoin pour entrainer un détecteur d'objets est d'avoir des données qui représentent ces objets. 

## Etape 1 : acquisition

Prenez 5 vidéos de 10 secondes dans lesquelles se trouve la classe que vous voulez apprendre à détecter. Faites attention à ce que des objets appartenant aux classes des autres binômes ne se retrouvent pas dans vos séquences, sinon vous devrez les annoter aussi.

Créez sur votre session une arborescence de fichiers comme la suivante :

<center>

![Arborescence de fichiers](images/arborescence.png)

</center>

...dans laquelle il faut :
* remplacer `nom_de_classe` par le nom de la classe que vous annotez ;
* remplacer `noms_du_binome1` par vos noms de famille ;
* les dossiers 1 à 5 correspondent aux séquences 1 à 5.

Une fois acquises, copiez les vidéos sur votre PC et extrayez-en les *frames* avec `ffmpeg` dans les différents dossiers `images` : 

  ```bash
  ffmpeg -i <video.mp4> -vf fps=30 -start_number 0 <nom_de_classe>/<noms_du_binome>/<num_sequence>/images/frame_%06d.jpg
  ```

Vous devez avoir une arborescence 
<center>

![Arborescence de fichiers](images/arborescence_extract_images.png)

</center>





Connectez-vous avec vos identifiants INSA au serveur d'annotation CVAT : https://