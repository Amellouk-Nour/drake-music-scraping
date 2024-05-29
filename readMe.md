# Analyseur de Paroles de Drake

## Description et Utilisation
Ce projet extrait des liens de chansons de Drake via une API (genius), analyse ces données pour récupérer les URL des pistes musicales, et télécharge les paroles pour identifier le mot le plus fréquemment utilisé. Le processus inclut le nettoyage des paroles pour enlever les caractères spéciaux et l'utilisation de `collections.Counter` pour analyser les mots.

### Installation et Exécution
1. **Clonez et préparez l'environnement :**
   ```bash
   git clone https://exemple.com/repertoire/projet_drake_analyse.git
   cd projet_drake_analyse
   python -m venv venv
   source venv/bin/activate  # Unix/MacOS 
     #or
   .\venv\Scripts\activate # pour Windows
   pip install -r requirements.txt
   ```

2. **Exécutez le script :**
   ```bash
   python Drake_any_song.py
   ```
   Cela génère `api.json` pour les données API, extrait les URL dans `links.json`, télécharge les paroles dans `mes musiques/` mais vous devez utilisez les fonctions misent à votre disposition, 
   ```bash
   python Drake_word.py
   ```
    et enfin détermine le mot le plus utilisé.

### Structure du projet
- `requirements.txt` : Dépendances.
- `Drake_any_song.py` : Script d'import des musiques.
- `Drake_word` : Script pour determiner le mot le plus dit par Drake.
- `api.json` : Données API.
- `links.json` : Liens des musiques.
- `mes musiques/` : Paroles téléchargées.

### Contribution
Les suggestions ou améliorations via pull requests ou issues sont bienvenues.

### Licence
Distribué sous la licence MIT.
