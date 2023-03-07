## Custom_controller :


### Qu'est-ce que c'est ?
> C'est une manette filaire totalement custom et crée par Devlowave qui tourne sur un raspberry pi pico equipé de circuitpython, dans ce repo il y'a :
> - le firmware du rpi pico
> - le code nécessaire à faire marcher la manette
> - les librairies nécessaires nottament pour faire l'interface entre la manette et l'ordinateur


### A quoi ça va servir ?
> A jouer a un PAC-MAN™ sur le thème de l'écologie (le repo n'est pas encore disponible)
> Cette mannette servira surtout à faire jouer les participants de l'armada de la participation, un festival ou Devlowave aura un stand


### Comment utiliser la manette ?
> - télechargez le repo sur votre ordinateur
> - prenez le document : "Circuit-python-8.0.3.uf2" situé dans le dossier : "firmware" et le mettre dans le dossier du RPI-PICO
> - prenez le code et le copier coller dans le dossier du RPI-PICO
> - mettez le dossier "adafruit_hid" dans le dossier du RPI-PICO
> - prenez une breadbord ou un pcb, des cables et des boutons puis soudez/branchez les cables selon le schéma suivant : (le schéma n'est pas encore disponible)
> - modifiez le fichier "code.py" et entrez le numéro des pins GPIO auquel les boutons sont connectés (pinout : https://pico.pinout.xyz/)
> - imprimez en 3d le modèle disponible dans le dossier "3D" (le modèle n'est pas encore disponible)
> - assemblez tous les composants dans le boitier imprimé précedemment
> - et voilà vous pouvez maintenant utiliser la manette en jeu
