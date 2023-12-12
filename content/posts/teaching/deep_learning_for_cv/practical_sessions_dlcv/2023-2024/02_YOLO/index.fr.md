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
### Labellisation :frowning_face:

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

Quand vous avez vos trois fichiers, vous me les envoyez par mail (clairelabitbonis@gmail.com), avec le nom de chacun des membres du binôme, et votre classe labellisée.

### Training COCO

Une fois qu'on aura les trois sous-ensembles pour l'ensemble des classes, on pourra les regrouper dans trois fichiers principaux `train.txt`, `val.txt` et `test.txt` pour tout le *dataset*. Puis on sera en mesure de lancer l'apprentissage correspondant à la configuration que vous avez tirée au sort. 

> Pour cette étape, nous vous demandons simplement de construire la ligne de commande avec les bons paramètres pour votre configuration. Nous (corps enseignant) lancerons les apprentissages en dehors des heures de TP d'ici la semaine prochaine, pour éviter de surcharger le serveur d'un coup. Il faut également avoir rassemblé au préalable toutes les données que vous aurez construites aujourd'hui avant de pouvoir lancer un apprentissage.

Une fois la moulinette et le *split* réalisés, il vous faudra *uploader* votre dossier sur le serveur GPU, à l'emplacement temporaire suivant : `/scratch/labi/DLCV/dataset/tmp/b/<classe>/<votre_dossier>`.

## Quêtes annexes
### *Detect with coco.pt*
Lancez `detect.py` avec les poids `yolov5s.pt` (qui sont pré-entrainés sur COCO) sur des images de votre *dataset* et visualisez les résultats dans `runs/detect/`. Faites-le tourner en mode *debug* pour pouvoir faire du pas à pas, ça vous servira pour la suite.

### Et la valeur du poids est...
Prenez votre date de naissance, additionnez tous les chiffres entre eux récursivement, jusqu'à tomber sur un seul chiffre, \\(x\\).
Prenons \\(j\\) votre jour de naissance et \\(m\\) votre mois de naissance.

> **Exemple** : je suis née le 8 décembre 1991, \\(8+1+2+1+9+9+1 = 31 \rightarrow x = 3+1 = 4\\) ; \\(j=8\\) ; \\(m=12\\).

Quelle est la valeur du poids du filtre de convolution n° \\(j\\) de la couche \\(x\\), à l'indice `[0,0]` du canal \\(m\\) ?

Doliprane ?

Affichez aussi le contenu de la *feature map* après le *backbone*, pour voir.

### *Seeing data augmentation*
> Cette étape sera possible à la séance prochaine, quand le *training* sera correctement configuré.

On veut voir du MixUp ! Modifiez le code pour qu'au moment de l'apprentissage on puisse visualiser la *data augmentation* faite par YOLO. S'il n'y a jamais de MixUp, c'est qu'il est désactivé dans le fichier de configuration des hyperparamètres. Changez les hyperparamètres qui vont bien pour que le MixUp soit effectué avec une probabilité de 0.25.

Vous pouvez aussi afficher le résultat de la mosaïque et d'autres transformations par exemple.
 
### Où est Charlie ? *(ou l'activation du mode hardcore)*

Pour appréhender le fonctionnement de YOLOv5, on peut répondre à un ensemble de questions. Pour en trouver les réponses, plusieurs techniques : Google, fouiner dans le code, exécuter en mode *debug*... L'idée n'est pas de répondre de manière exhaustive (certaines questions peuvent être *tricky* quand on débute en PyTorch), mais d'enclencher la réflexion sur les questions que l'on se pose quand on utilise un réseau. Cela dit, l'objectif est quand même de répondre au maximum de questions :wink:

Les voilà en vrac, on dit merci à Pierre :

#### Questions générales
- Combien de classes y a-t-il dans le *dataset* VisDrone ?
- Quel est le ratio entre le nombre de poids de YOLOv5-S et YOLOv5-L ?
- Quelle différence entre YOLOv5-p2 et YOLOv5-p6 ?
- Que contient le `model.pt` sauvegardé ?
- Quelles tâches d'apprentissage peuvent être réalisées avec YOLO ?
- Quels optimiseurs sont disponibles dans YOLO ?
- Comment fonctionne le *early stopping* dans YOLO ?

#### Questions sur le modèle en lui-même
- Quelle est la *loss* utilisée en détection ?
- Quels types différents de convolutions sont utilisés par YOLO ?
- Quelles couches composent le module "Conv" de YOLO ?
- Quelle différence entre Bottleneck et Bottleneck CSP ?
- Dans un module PyTorch, quelle fonction doit être implémentée pour faire passer les *inputs* dans le réseau ?
- Dans un module PyTorch, quelle fonction doit être implémentée pour que l'apprentissage des poids soit possible ?
- Que fait le SPP ?
- Comment fonctionne et à quoi sert le Focus ? Par quoi aurait-on pu le remplacer ?
- Le Concat est-il utilisé pour fusionner des couches ou bien des *batches* ? (Pourquoi ?)
- Donnez la structure de la sortie de YOLO en détection (bon courage !).

#### Compréhension générale
- Que prédira le réseau si on donne le fichier de configuration avec 80 classes (COCO) mais sur notre *dataset* ?
- Que prédira le réseau avec nos poids sur le *dataset* COCO ?
- Par quoi aurait-on pu remplacer la fonction d'activation SiLU ?
- Proposez une autre approche remplaçant le Concat.
- A quoi sert le *dropout* de YOLO ?
- Est-il possible de *freezer* toutes les couches ? Que se passerait-il ?
- Par quoi peut-on remplacer la fonction UpSample de YOLO ?
- Mieux vaut utiliser YOLOv5-M ou ResNet50 ? Pourquoi ?
- Mieux vaut utiliser YOLOv5-L ou YOLOv5-X ? Pourquoi ?
- Combien de coups de tête Zidane a-t-il donné de plus qu'Ancelotti ?




