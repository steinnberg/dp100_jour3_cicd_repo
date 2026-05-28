# DP-100 Jour 3 - CI/CD GitHub Actions Lab

Mini-repo pedagogique pour illustrer l'automatisation CI/CD appliquee au Machine Learning.

## Objectifs

- Structurer un repo ML minimal
- Executer des tests automatiquement
- Verifier la qualite du code avec Ruff
- Lancer un entrainement smoke-test
- Publier les artefacts du modele dans GitHub Actions

## Installation locale

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Lancer localement

```powershell
ruff check src tests
pytest -q
python src/train.py
```

Les artefacts sont crees dans `artifacts/` :

- `model.joblib`
- `metrics.json`

## Pipeline CI/CD

Le fichier `.github/workflows/ci.yml` lance automatiquement :

1. checkout du code
2. installation Python
3. installation des dependances
4. lint avec Ruff
5. tests unitaires
6. entrainement smoke-test
7. upload des artefacts

## Lien DP-100

Ce lab illustre la logique production autour d'un modele ML : tests, reproductibilite, qualite, artefacts et automatisation.
