# ant-algorithm

### La technologie

Le fait de choisir la technologie des algorithmes de colonies de fourmies dans le cadre d'une recherche d'optimisation de chemin est absolument cohérente. En effet comme pourrait le faire une colonie de fourmie l'algorithme va chercher à expérimenter plusieurs chemins et suivre les chemins qui lui parressent le plus cohérent. Ce calcul est fait en fonction de la valeur (le poids) que nous donnons à chaque proposition de chemin.
Une direction ce dessine alors entre les différents points qui auront obtenus les meilleurs résultats dans la fonction d'évaluation.


### Fonction d'évaluation

Après plusieurs tentatives et expérimentations j'ai défini la fonction d'évaluation de la manière suivante :
    * on défini la distance entre les deux données d'abscisse et on la met au carré
    * on fait de même pour les données données d'ordonné
    * finalement on met au carré l'addition des données qu'on a obtenus précédemment


### Structure de donnée

Utilisation des données de nantes métropoles
http://data.nantes.fr/donnees/detail/repertoire-des-voies-de-nantes-metropole/
elles sont présentent dans le fichier join `nantes-street.csv`
