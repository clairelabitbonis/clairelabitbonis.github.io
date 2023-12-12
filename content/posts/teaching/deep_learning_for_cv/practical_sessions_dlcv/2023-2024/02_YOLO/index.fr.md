---
title: "DLCV2 | Le Bingo de YOLO !"
date: 2022-11-04T10:00:00+09:00
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
    name: "02 | YOLO !"
    identifier: dlcv-practical-sessions-2023-2024-02
    parent: dlcv-2023-2024-practical
    weight: 20
---
<center>

![Le Bingo de YOLO](images/le_bingo_de_yolo_v2.png)

</center>

## Présentation

Bonjour, bonjour ! Aujourd'hui, plusieurs objectifs :
* finir le *dataset* ;
* faire le *split* train/val/test ;
* développer une application de détection et visualisation dans un flux vidéo ;
* manipuler un apprentissage de YOLOv8.

C'est comme une grille de bingo à remplir. Plus vous en validez, mieux c'est.

On va le diviser en deux : une quête principale, et des quêtes annexes (des *gamers* par ici ?). La quête principale est l'objectif à atteindre pour terminer correctement le TP, les quêtes annexes sont à faire s'il vous reste du temps.

{{< alert type="warning" >}}
Attention, "Labellisation :frowning_face:" et "L'apprentissage dont vous êtes le héros" sont **nécessaires** pour que je puisse lancer les apprentissages pour la semaine prochaine. Considérez-les comme la quête principale. Si vous avez le temps, réalisez les quêtes annexes : "3,2,1, développez!", "Training COCO", "Feature visualization". 
{{< /alert >}}

Les quêtes annexes sont optionnelles, mais considérées comme des bonus pris en compte lors de l'évaluation :wink: 

## Quête principale
### Labellisez :frowning_face:

La semaine dernière dans CVAT, vous avez tou.te.s annoté votre classe d'objets. Nous devons pouvoir récupérer toutes vos données d'ici la fin de séance, sinon vos images ne seviront pas à l'entrainement (ce serait dommage). 

![Dataset](images/dataset_cvat.png)

{{< alert type="warning" >}}
Attention, en regardant certaines séquences, je me suis rendue compte que beaucoup d'annotations s'arrêtaient en cours de vidéo, que certaines qui étaient occultées étaient quand même labellisées comme visibles, etc. 
Je vous demande donc à tous et toutes de vérifier vos labels avant de les valider pour de bon.

:warning: Par ailleurs, changement de stratégie ; nous (les encadrant.e.s) nous chargerons nous-mêmes d'exporter les tâches et d'organiser le *dataset* sur le serveur GPU. La semaine dernière, certaines erreurs bizarres ont popé lors de la copie sur le serveur, alors on va s'éviter du tracas inutile en séance.
{{< /alert >}}

Quand votre labellisation est terminée, venez la valider.

### L'apprentissage dont vous êtes le héros

Pour celles et ceux qui n'ont pas divisé leur *dataset* en trois fichiers textes `train.txt`, `val.txt` et `test.txt` (cf. TP précédent), c'est l'heure ! 

Vous devez créer trois fichiers : `train.txt`, `val.txt` et `test.txt`. Dans chacun, vous mettrez la liste des chemins d'accès vers les images selon qu'elles doivent aller en base d'apprentissage, de validation ou de test. Par exemple, dans `train.txt` :

    ./velo/tic_et_tac/4/images/frame_000002.jpg
    ./velo/tic_et_tac/4/images/frame_000118.jpg
    ...
    ./velo/tic_et_tac/2/images/frame_000004.jpg
    ./velo/tic_et_tac/1/images/frame_000001.jpg
    ./velo/tic_et_tac/3/images/frame_000256.jpg

{{< alert type="danger" >}}
La répartition de vos données entre les différentes bases est une étape cruciale : 
* allez-vous mettre 3 séquences complètes en `train`, une en `val` et une en `test`, au risque d'avoir des exemples en test qui sont trop éloignés de ceux de la base d'apprentissage ?
* ou bien allez-vous plutôt mettre les débuts de séquence en `train`, les milieux en `val`, les fins en `test`, mais dans ce cas vous biaiserez l'apprentissage et obtiendrez des performances étrangement un peu trop hautes ? 
* vous pouvez aussi choisir la méthode bourrine et faire un random total sur la répartition...
{{< /alert >}}

**Spoiler alert :** la première option a tendance à légèrement *overfitter*...

![Overfitting](images/overfitting.png)

Quand vous avez vos trois fichiers, vous me les envoyez par mail (clairelabitbonis@gmail.com), avec le nom de chacun des membres du binôme, et votre classe labellisée.

### 3, 2, 1, développez !

On arrive enfin à YOLO, depuis le temps qu'on en parle. La première étape consiste à configurer votre *workspace* : allez voir l'annexe "Configuration du *workspace*" (elle porte bien son nom). Une fois que c'est fait, voilà les exigences à respecter :
* l'application doit détecter des objets dans un flux vidéo ;
* l'application doit afficher les boites englobantes de détection sur les images traitées ;
* l'application doit afficher l'analyse en temps réel, c'est-à-dire afficher les détections dès que l'analyse est faite ;
* l'application doit colorer les boites englobantes de manière unique en fonction de la classe détectée ;
* l'application ne doit pas être dépendante du nombre ni du nom des classes détectées ; 
* les couleurs choisies pour l'affichage des boites doivent être aussi belles qu'un arc-en-ciel en plein mois d'août :rainbow:.

Les contraintes logicielles sont :
* utiliser Python ;
* utiliser OpenCV ;
* utiliser YOLOv8 (ah bon !).

Pour cette première version et comme les apprentissages sur le *dataset* de cette année ne sont pas encore faits, vous utiliserez YOLO avec des poids pré-entrainés sur COCO. 

Pour réaliser cette quête, la toile de l'Internet est votre amie, avec notamment :
* la [doc d'Ultralytics](https://docs.ultralytics.com);
* [Google](https://www.google.fr);
* ChatGPT : :angry: bouuuh ChatGPT, en plus il connait même pas YOLOv8 parce que c'est trop récent, laissez tomber. [Même s'il est très fort](https://chat.openai.com/share/4c573574-bfad-4b17-a918-9db9fc16f0e1). On appelle ça la _dissonance cognitive_ :

![Dissonance cognitive](images/dissonance_cognitive.png)

## Quêtes secondaires
### Training COCO128
Pour pouvoir voir YOLO en action, vous allez pouvoir lancer un apprentissage sur vos machines. Et afin d'éviter de voir vos PC s'envoler vers l'infini et au-delà, on va le faire sur un tout petit *dataset* : COCO 128, qui est une extraction du *dataset* COCO  [Common Objects in Context](https://cocodataset.org/#home).

Toujours, la [doc d'Ultralytics](https://docs.ultralytics.com/modes/train/#key-features-of-train-mode) vous indique comment faire. Vous pouvez voir comment est écrit le fichier du *dataset*, il est dans `ultralytics/cfg/datasets/coco128.yaml`. Vous serez ravis d'apprendre que le *dataset* COCO permet d'entrainer YOLO à détecter des brocolis.

Quand vous lancez votre script de `train`, vous pouvez ensuite le monitorer avec Tensorboard. Pour cela, ouvrez un autre terminal et entrez `tensorboard --logdir=runs` pour indiquer qu'il faut monitorer le dossier dans lequel YOLO stocke les apprentissages. Il vous ouvre un monitoring sur [https://localhost:6006](https://localhost:6006) par défaut.

## Annexes
### Configuration du *workspace*