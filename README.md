# Bonnes pratiques de dév 

Pour permettre à d'autres personnes de s'approprier votre code, plusieurs choses sont nécessaires : 

<br/>

## Mise en place d'un environnement 

Installez, créez et activez votre virtualenv sur votre machine (Mac ou GitBash(compatible windows) / a voir pour Powershell Windows):

```bash
# Installation : 
pip install virtualenv

# Création :
virtualenv <ENV-NAME>

# Activation :
source venv/bin/activate

# Pour vérifier quel python est utilisé :
which python

# Instalaltion des requirements d'un nouveau projet : 
pip install -r requirements.txt
```

Je vous invite à tester tout ça en allant sur ma branche et en suivant les étapes précédente.

```bash
# Liste des branches distantes :
git branch -r 

# Changement de branche :
git checkout <nom de la branch sans le "ORIGIN">

```

Pour que python puisse trouver l'ensemble de vos packages et modules il est nécessaire d'exporter le chemin du projet dans le PYTHONPATH :

```bash
# Ce positionner à la racine du projet :
cd <RACINE-DU-PROJET>

# Export du répertoire courant dans PYTHONPATH :
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

<br/>

## Conteneurisation 

Bon tutoriel pour créer une image de votre application : https://digicactus.com/conteneuriser-vos-applications-python-part-1/#:~:text=Pour%20cela%2C%20nous%20utilisons%20avec,de%20configurer%20d'autres%20composants.&text=Ensuite%20nous%20cr%C3%A9ons%20un%20r%C3%A9pertoire,des%20autres%20fichiers%20de%20configuration.

Optimisation DockerFile : article de blog Alex (Faire attention à l'image de base utiliser)

Vous trouverez à la racine du projet un exemple de "dockerfile" fonctionnel sur ce projet. Vous pouvez installer docker sur vos machines en suivant la doc officielle.
Les étapes de déploiement de l'image sont les suivantes : 

```bash
# 1 - Création du dockerfile

# 2 - Build de l'image (après s'être placé à côté du dockerfile)
docker build -t <IMAGE-NAME>

# 3- Run de l'image 
docker run -p 0.0.0.0:8080 --name <APP-NAME> <IMAGE-NAME>
```

Vous avez du remarquer qu'il y avait un fichier .dockerignore en plus à la racine du projet. Celui-ci à la manière du .gitignore permet de filtrer ce qui va être copier lors de la création de l'image de l'application. Cela permet de ne pas la surcharger et qu'elle puisse être rapidement déployable. Dans certains cas c'est aussi dans un souci de sécurité et de confidentialité, pour ne pas stocker des données qui peuvent être sensible (comme des données utilisateurs, des crédentials et autres).

<br/>

## CICD (continuous Integration / Continuous Deployment)

Utilisation de GitHub Actions : 
Automatisation des tests, de la construction de l'image, de son enregistrement sur un image registry, puis de son déploiement sur un hébergeur (comme AWS).

Mise en place d'une stratégie de mise à jour de l'application. Les differents types : https://www.techtarget.com/searchitoperations/answer/When-to-use-canary-vs-blue-green-vs-rolling-deployment#:~:text=The%20canary%20deployment%20pattern%20is,version%2C%20rather%20than%20certain%20servers.

<br/>

## Architecture 

```
project/
|-- src/
|   |-- app
|      |-- __init__.py
|      |-- feature1
|          |-- __init__.py
|          |-- module1.py
|          |-- module2.py
|       |-- feature2
|          |-- __init__.py
|          |-- module1.py
|
|   |-- app_test/
|       |-- __init__.py
|       |-- feature1
|           |-- __init__.py
|           |-- module1.py
|           |-- module2.py
|       |-- feature2
|           |-- __init__.py
|           |-- module1.py
|
|-- main.py
|-- .gitignore
|-- requirements.txt
|-- README.md
```

Note : Mettre un fichier "\_\_init\_\_.py" dans chaque dossiers pour le balisage et permettre à python de pouvoir faire les imports des fonctions des autres dossiers

</br>

## Documentation

Pour faciliter la lecture et l'appropriation de votre code par un autre développeur il est nécessaire de documenter votre code.
Cela passe par l'écriture de différent document et de certaines bonnes pratiques.

</br>

### README

Le README est là pour accueillir une personne sur votre projet. Il doit expliquer l'objectif et la raison d'être de votre projet. 
Puis expliquer pas à pas comment faire fonctionner votre projet en local ou sur un service de conteneurisation comme docker.
Dans un monde merveilleux il pourrait même y avoir une partie expliquant comment participer à votre projet (Merge request, commentaire sur commit, pull request ...) 

</br>

### DocString 

Pour permettre à une personne de comprendre votre code sans qu'il est besoin de décortiquer chacune de vos fonctions il est nécessaire de bien nommer ses variables et de documenter ses fonctions. Cela revient à expliquer brièvement le but de la fonction et définir ses parametres d'entré et de sortie. Il y a différentes conventions d'écriture de cette documentation qu'on appellera "DocString" mais je vous recommande celle ci-dessous :

```python
def multiplication(a, b):
    """_summary_

    Args:
        a (float): A float
        a (float): Another float

    Returns:
        float: float of the product of a and b
    """
    product = a * b 
    return product


print(add_binary.__doc__)
```

Elle est générable automatiquement en tappant trois fois le double quotte """ en dessous de la première ligne de la fonction puis en faisant entrée.