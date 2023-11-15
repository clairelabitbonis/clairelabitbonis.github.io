---
title: "DLCV-TP-00 | Présentation"
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
    name: "00 | Présentation"
    identifier: dlcv-practical-sessions-00
    parent: dlcv-practical-sessions
    weight: 10
---

Remote-SSH dans vscode vers srv-gei-gpu2
conda deactivate si (base) est activé par défaut
git clone --recursive https://github.com/ultralytics/ultralytics.git
cd ultralytics
python -m venv env
source env/bin/activate

Changer dans requirements : 
- torch>=1.8.0 -> torch==1.12.0 
- torchvision>=0.9.0 -> torchvision==0.13.0
pip install -e . 

pour sélectionner l'interpréteur, entrer le chemin à la main

mettre le dataset.yaml dans ultralytics/cfg/datasets/ à côté de coco128.yaml :

Contenu de dlcv.yaml :
  path: /scratch/labi/DLCV/dataset/final  # dataset root dir
  train: /scratch/labi/DLCV/dataset/final/train.txt
  val: /scratch/labi/DLCV/dataset/final/val.txt  
  test: /scratch/labi/DLCV/dataset/final/test.txt  

  # Classes
  nc: 15
  names: 
    ['claire', 'pierre', 'bague', 'chaise', 'ecouteurs', 'gourde', 'lunettes', 
    'montre', 'voiture', 'chauve', 'lentilles', 'ordinateur', 'sac', 'stylo', 'velo']


créer dossier scripts à la racine, avec 2 scripts, un pour train et un pour detect :
- train.py

  from ultralytics import YOLO

  # Load a model
  model = YOLO("yolov8n.yaml")  # build a new model from scratch
  model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

  # Use the model
  model.train(data="dlcv.yaml", epochs=3)  # train the model
  metrics = model.val()  # evaluate model performance on the validation set
  results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
  path = model.export(format="onnx")  # export the model to ONNX format
- detect.py



SUR le serveur srv-gei-gpu2 : python 3.9, donc torch==1.12.0 et torchvision==0.13.0 pour avoir CUDA avec

SUR les machines de TP en local : python 3.11, trop récent pour torch==1.12.0, donc il faut remettre le requirements.txt de base qui installera torch==2.0