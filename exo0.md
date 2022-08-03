# Installer Spark

## Les dépendances

Pour installer les dépendances Spark du projet, lancez la commande :

```bash
poetry install
```

Si besoin, vous pouvez changer la version de Python définie actuellement à `3.8`.

## Spark

### MacOS

```bash
brew install apache-spark
```

### Ubuntu

1. Ouvrez la page de [téléchargement de Spark](https://spark.apache.org/downloads.html) et suivez les instructions.
2. Dézippez et déplacez le dossier dans `/opt/spark`
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
