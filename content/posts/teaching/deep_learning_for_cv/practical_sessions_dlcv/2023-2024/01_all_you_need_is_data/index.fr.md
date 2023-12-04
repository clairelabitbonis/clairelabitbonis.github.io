---
title: "DLCV2 | All you need is data"
date: 2023-12-04T10:00:00+09:00
description: ""
summary: ""

draft: false
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

{{< alert type="success" >}}
Tout ce dont vous avez besoin pour entrainer un détecteur d'objets est d'avoir des données qui représentent ces objets. Et de les nettoyer (les données, pas les objets). Et de les trier. Et de les annoter. Et d'en jeter un peu parce qu'elles sont pas si bien. Et d'en rajouter encore parce qu'il y en a plus assez. Etc. :+1: 
{{< /alert >}}

## Acquisition

Prenez 5 vidéos de 10 secondes dans lesquelles se trouve la classe que vous voulez apprendre à détecter. 

Posez-vous des questions :
* est-ce que l'objet peut dépasser du cadre ?
* est-ce que j'ai suffisamment d'objets différents de la même classe ?
* est-ce que le contexte change entre les séquences ?
* etc.

{{< alert type="danger" >}}
Faites attention à ce que des objets appartenant aux classes des autres binômes ne se retrouvent pas dans vos séquences, sinon **_vous devrez les annoter aussi._**
{{< /alert >}}

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

Vous devez avoir une arborescence qui ressemble à ça à la fin :
<center>

![Arborescence de fichiers](images/arborescence_extract_images.png)

</center>

## Import des données dans CVAT

C'est là que le travail commence... Connectez-vous avec vos identifiants INSA au serveur d'annotation [CVAT](https://cvat.ens.insa-toulouse.fr/).

Pour chaque séquence vidéo, créez une nouvelle tâche :
<center>

![Nouvelle tâche](images/cvat_create_task.png)

</center>

Renseignez le nom de la tâche (par exemple `<nom-classe>_<numero-sequence>`), ajoutez un label du nom de la classe que vous annotez :

<center>

![Nouvelle tâche - Settings](images/cvat_create_task_settings.png)

</center>

Ajoutez ensuite (par *drag and drop*) toutes les `frame_XXXXXX.jpg` de la séquence en question.

<center>

![Nouvelle tâche - Add files](images/cvat_create_task_settings2.png)

</center>

Finissez par sélectionner le format d'annotation `YOLO 1.1` avant de `Submit & Open`.

<center>

{{< img src="images/cvat_create_task_settings3.png" style="width:50%;" align="center" title="Nouvelle tâche - Choose YOLO 1.1" >}}

![Nouvelle tâche - Choose YOLO 1.1](images/cvat_create_task_settings3.png)

</center>

L'interface de labellisation s'ouvre.

## Labellisation

