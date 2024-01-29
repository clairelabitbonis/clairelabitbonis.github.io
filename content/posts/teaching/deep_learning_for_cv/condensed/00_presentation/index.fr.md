---
title: "DLCV condensé | Présentation"
date: 2024-01-29T10:00:00+09:00
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
    name: "00 | Présentation"
    identifier: dlcv-condensed-00
    parent: dlcv-condensed
    weight: 10
---

## Objectifs pédagogiques

L'objectif de la formation est de toucher à toutes les étapes de l'ingénierie du *deep learning*, à savoir :
- l'**acquisition** et l'**annotation** de données pour la détection d'objets dans les images, 
- l'**apprentissage** de modèles YOLOv8 sur ces données, 
- l'**évaluation** des performances de la tâche apprise et la **visualisation** des résultats obtenus,
- le **portage** des réseaux entrainés, sur cible NVIDIA.


## Configuration des outils

Chaque étape nécessite des outils particuliers, listés ci-dessous :

| Etape                      | Outils                                     |
|----------------------------|--------------------------------------------|
| Général                    | OS : Ubuntu 22.04                          |
| Construction *dataset*     | ffmpeg, CVAT                               |
| Entrainement et évaluation | Ultralytics (YOLOv8), Python + librairies (OpenCV, PyTorch, Tensorboard, etc.) |
| Portage                    | TensorRT, tensorrtx                        |


### ffmpeg
`ffmpeg` sera utilisé pour extraire des images à partir d'un fichier vidéo, avant de les importer dans l'outil de labellisation. Sous Ubuntu, il faut juste faire un `sudo apt install ffmpeg`.

### CVAT
CVAT (Computer Vision Annotation Tool) sera utilisé pour la labellisation des données. Sa procédure d'installation est décrite [ici](https://opencv.github.io/cvat/docs/administration/basics/installation/). Elle installe également Docker sur la machine.

Une fois installé, CVAT est accessible depuis `<ip_de_la_machine>:8080` dans un navigateur Google Chrome.

### Ultralytics
Pour installer YOLOv8, exécuter dans un terminal :

```
cd <path/to/workspace>
git clone --recursive https://github.com/ultralytics/ultralytics.git
cd ultralytics
pip install -e .
pip install tensorboard
```
