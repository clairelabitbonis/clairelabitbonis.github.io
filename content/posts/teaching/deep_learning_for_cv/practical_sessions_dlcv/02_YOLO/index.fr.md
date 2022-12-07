---
title: "DLCV-TP-01 | Le Bingo de YOLO !"
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
    name: "01 | YOLO !"
    identifier: dlcv-practical-sessions-02
    parent: dlcv-practical-sessions
    weight: 20
---

<center>

![Le Bingo de YOLO](images/le_bingo_de_yolo.png)

</center>

## Présentation

L'objectif du TP du jour est d'utiliser le *dataset* construit la semaine dernière pour entrainer YOLOv5 à détecter les classes d'objets annotées.
Voyez-le comme une grille de Bingo à remplir. Plus vous en validez, mieux c'est. 

{{< alert type="warning" >}}
Attention, "la moulinette des labels" et "split, split, split" sont **nécessaires** pour lancer l'apprentissage en fin de séance. Considérez-les comme la quête principale. Si vous avez le temps, réalisez les quêtes annexes : "seeing data augmentation", "et la valeur du poids est...", "detect with coco.pt" et "où est Charlie ?". 
{{< /alert >}}

Les quêtes annexes sont optionnelles, mais considérées comme des bonus pris en compte lors de l'évaluation :wink: 

### Arborescence du *dataset*
Après réorganisation du *dataset* à la suite des TPs de la semaine dernière, l'arborescence est comme suit : 

![Arborescence du dataset](images/arborescence.png)

### Lancer le code en mode *debug*
Dans l'onglet *debug*, cliquez sur "créer un fichier launch.json". Vous pouvez ensuite configurer le `.json` comme ci-dessous, et adapter les paramètres d'appel :

![Launch .JSON](images/launchjson.png)

Vous pouvez ensuite ajouter une configuration pour le *debug* du fichier `train.py` par exemple.

## Quête principale
### La moulinette des labels

{{< alert type="danger" >}}
***/!\ DANGER /!\\*** 

Vous allez travailler dans les dossiers du *dataset* directement. Ne vous trompez pas, n'écrasez pas vos fichiers de labels ou ceux de vos camarades, ce serait dommage, il faudrait tout ré-annoter... :angel:
{{< /alert >}}

La semaine dernière dans CVAT, vous avez tous annoté votre classe d'objet indépendamment des autres binômes. Dans vos fichiers de labels, votre numéro de classe est donc `0`, quelle que soit votre classe. Or pour entrainer un détecteur multi-classes, chaque classe doit porter un indice différent.

> Dans la vraie vie, on crée un projet dans CVAT qui contient toutes les classes d'objets, on ajoute des tâches au projet, on labellise les *jobs*, et à l'export toutes les annotations portent les bons numéros de classes. Mais **(1)** la configuration de CVAT a été *légèrement* chaotique, donc pas de projet, donc pas les bons numéros, et **(2)** de toutes façons, le quotidien de l'ingé *deep learning* n'est fait que de moulinettes et de scripts Python en tout genre, ça tombe bien !

Votre mission est donc de vous placer dans votre dossier, et de remplacer dans chacun des fichiers de label `frame_xxxxxx.txt` le numéro de classe par celui qui vous correspond, d'après le mappage suivant :

```python
  0: claire
  1: pierre
  2: bague
  3: chaise
  4: ecouteurs
  6: gourdes
  6: lunettes
  7: montre
  8: voiture
  9: chauve
  10: lentilles
  11: ordinateur
  12: sac
  13: stylo
  14: velo
```

> **Exemple** avec le fichier `frame_00256.txt` de la classe `gourdes` :
>
> Avant : ![Avant moulinette](images/label_a_changer.png)
>
> Après : ![Après moulinette](images/gourde_label.png)

A vous de trouver la meilleure manière de le faire : à la main (ça peut marcher, mais vous y serez encore la semaine prochaine), avec un script *bash*, un script Python, en utilisant des librairies comme `glob` pour parcourir les dossiers, etc.

### *Split, split, split!*
Avant de lancer l'apprentissage, il faut séparer la base en trois sous-ensembles : apprentissage, validation, et test. Pour cela, YOLOv5 charge un fichier `yaml` qui contient les informations sur les classes et les fichiers contenant l'information du *split*. Par exemple, pour le détecteur de Claire / Pierre vu en cours :

![YAML](images/yaml.png)

Situés dans le dossier `path`, les fichiers `train.txt`, `val.txt` et `test.txt` doivent contenir les chemins vers les images correspondantes :

![train.txt](images/train_txt.png)

A vous de jouer : toujours dans votre dossier (au même niveau que les dossiers 1/2/3/4/5), construisez ces trois fichiers (à l'aide d'une commande `shell`, d'un script ou autre). La répartition entre les trois *sets* est de l'ordre de 65% / 25% / 10%.

### Train

Une fois qu'on aura tous les trois sous-ensembles pour chaque classe, on pourra les regrouper dans trois fichiers principaux `train.txt`, `val.txt` et `test.txt` pour tout le *dataset*. Puis vous serez en mesure de lancer l'apprentissage correspondant à la configuration que vous avez tirée au sort. 

> Assurez-vous que l'apprentissage se lance et ne plante pas, puis ***arrêtez-le*** : nous (corps enseignant) lancerons les apprentissages en dehors des heures de TP d'ici la semaine prochaine, pour éviter de surcharger le serveur d'un coup. 

## Quêtes annexes
### *Seeing data augmentation*
Je veux voir du MixUp ! Modifiez le code pour qu'au moment de l'apprentissage on puisse visualiser la *data augmentation* faite par YOLO. S'il n'y a jamais de MixUp, c'est qu'il est désactivé dans le fichier de configuration. Changez les hyperparamètres qui vont bien pour que le MixUp soit effectué avec une probabilité de 0.25.

### Et la valeur du poids est...
Prenez votre date de naissance, additionnez tous les chiffres entre eux récursivement, jusqu'à tomber sur un seul chiffre, \\(x\\).
Prenons \\(j\\) votre jour de naissance et \\(m\\) votre mois de naissance.

> **Exemple** : je suis née le 8 décembre 1991, \\(8+1+2+1+9+9+1 = 31 \rightarrow x = 3+1 = 4\\) ; \\(j=8\\) ; \\(m=12\\).

Quelle est la valeur du poids du filtre de convolution n° \\(j\\) de la couche \\(x\\), à l'indice `[0,0]` du canal \\(m\\) ?

Doliprane ?

### *Detect with coco.pt*
Lancez `detect.py` avec les poids `yolov5s.pt` (qui sont pré-entrainés sur COCO) sur des images de votre *dataset* et visualisez les résultats dans `runs/detect/`.

### Où est Charlie ? *(ou l'activation du mode hardcore)*

Pour appréhender le fonctionnement de YOLOv5, on peut répondre à un ensemble de questions. Pour en trouver les réponses, plusieurs techniques : Google, fouiner dans le code, exécuter en mode *debug*... L'idée n'est pas de répondre de manière exhaustive (certaines questions peuvent être *tricky* quand on débute en PyTorch), mais d'enclencher la réflexion sur les questions que l'on se pose quand on utilise un réseau. Enfin, l'objectif est quand même de répondre au maximum :wink:

Les voilà en vrac, on dit merci à Pierre :

#### Questions générales
- Combien de classes y a-t-il dans le *dataset* VisDrone ?
- Quelle différence de poids y a-t-il entre YOLOv5-s et YOLOv5-l ?
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
- Que fait le SPP ?
- A quoi sert le Focus ? Par quoi aurait-on pu le remplacer ?
- Concat permet-il de fusionner des couches ou des *batches* ? (Pourquoi ?)
- Donnez la structure de la sortie de YOLO en classification

#### Compréhension générale
- Que prédira le réseau si on donne le fichier de configuration avec 80 classes (COCO) mais sur notre *dataset* ?
- Que prédira le réseau si on donne le fichier de configuration avec 80 classes (COCO) mais avec nos poids sur le *dataset* COCO ?
- Par quoi aurait-on pu remplacer la fonction d'activation SiLU (exemple : `common.py`, ligne 134) ?
- Proposez une autre approche remplaçant le Concat.
- A quoi sert le *dropout* de YOLO ?
- Est-il possible de *freezer* toutes les couches ? Que se passerait-il ?
- Par quoi peut-on remplacer la fonction UpSample de YOLO ?
- Mieux vaut utiliser YOLOv5-M ou ResNet50 ? Pourquoi ?
- Mieux vaut utiliser YOLOv5-L ou YOLOv5-X ? Pourquoi ?
- Qui de Zidane ou Ancelotti a gagné le *match* ?




