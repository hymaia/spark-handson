# Installer Spark

## Prérequis

### Windows

Installer WSL et Ubuntu.

Pour travailler dans de bonnes conditions je recommande VScode avec le plugin **Remote Development**.

### Pour tout le monde

Installer poetry en suivant la [documentation du site officiel](https://python-poetry.org/docs/#installation)

Pour les mac M1 ou M2, il suffit de lancer :
```bash
brew install poetry
```

## Les dépendances

Pour installer les dépendances du projet, lancez la commande :

```bash
poetry install
```

Si besoin, vous pouvez changer la version de Python définie actuellement à `3.10`.

## Spark

### MacOS

```bash
brew install apache-spark
```

### Ubuntu

1. Ouvrez la page de [téléchargement de Spark](https://spark.apache.org/downloads.html) et suivez les instructions.
2. Dézippez et déplacez le contenu du dossier dans `/opt/spark`
3. Créez les variables d'environnements suivantes :

```bash
export PYSPARK_PYTHON=/usr/bin/python3
export SPARK_HOME=/opt/spark
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip
```

### Vérifier que ça fonctionne

Pour vérifier que l'installation est bonne, on lance les tests unitaires de l'exercice 0 :

```bash
poetry run pytest
```

Vous devez avoir un test au vert.

-> [Suivant](exo1.md)
