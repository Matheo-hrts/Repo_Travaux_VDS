Pour utiliser ce script il faut lors du lancment indiquer ce que vous compter faire (ex: ``python script_csv.py read`` si vous voulez lire un ficher) les différentes possibilité sont ``read write merge sort``.

Si vous choisissez de lire (read) vous serez demander quel fichier vous voulez lire, 
si ce fichier n'existe pas la question vous sera reposer 
(si le fichier se trouve dans un sous dossier il faut l'indiquer au formate 'chemin/vers/le/fichier.extension').

Si vous choisissez d'écrire (write) vous serez demander ce que vous voulez écrire au format 'file name,name,quantity,price,category'.

Si vous choisissez de fusionner (merge) tout les fichier du dossier CSV/ seront fuisonner en un seul .csv dans le dossier merged_csv/ si celui-ci n'existe pas il sera automatiquement creer.

Si vous choisissez de trier (sort) vous serez demander sur quel colonne vous voulez trier, ensuite vous aurez une prévisualisation du tri, 
vous serez ensuite demander si vous voulez sauvegarder ce fichier (si vous le voulez taper 'y' ou 'yes') 
vous serez alors demander comment voulez vous nommer le fichier (entrez n'importe quel nom sans extension).
