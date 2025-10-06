# IoT Alert Project

Un projet simple de simulation IoT qui surveille la température et les mouvements. Si un seuil est dépassé, une alerte est envoyée par e-mail.

## Fonctionnalités
- Simulation de capteurs de température et de mouvement
- Alerte automatique par e-mail
- Configuration personnalisable

## Installation
1. Cloner le projet :
   git clone https://github.com/memin-sd/IoT-Alert-Project.git
2. Entrer dans le dossier :
   cd IoT-Alert-Project
3. Installer les dépendances :
   pip install -r requirements.txt

## Utilisation
1. Créer un fichier `.env` et y ajouter :
   SENDER_EMAIL=ton_email@gmail.com
   RECIPIENT_EMAIL=email_destinataire@gmail.com
   EMAIL_PASSWORD=ton_mot_de_passe_app
2. Exécuter le script :
   python main.py

## Exemple d’affichage
Température: 32°C, Mouvement: 1  
Température dépassée !  
Email envoyé pour Température  


