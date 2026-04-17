### Exercice 6 — 🟡 Intermédiaire — Analyse de ventes
Tu as ce DataFrame de ventes :
```python
import pandas as pd

data = {
    "produit":    ["Laptop", "Téléphone", "Tablette", "Écran", "Clavier",
                   "Souris", "Laptop", "Téléphone", "Tablette", "Écran"],
    "categorie":  ["Informatique", "Mobile", "Mobile", "Informatique", "Accessoire",
                   "Accessoire", "Informatique", "Mobile", "Mobile", "Informatique"],
    "prix":       [800, 500, 300, 250, 50, 25, 900, 600, 350, 280],
    "quantite":   [5, 10, 8, 6, 20, 30, 3, 7, 4, 9],
    "mois":       ["Jan", "Jan", "Jan", "Jan", "Jan",
                   "Fev", "Fev", "Fev", "Fev", "Fev"],
}
df = pd.DataFrame(data)
```
1. Ajoute une colonne `total` = prix × quantite
2. Affiche le chiffre d'affaires total
3. Affiche le CA par catégorie
4. Affiche le produit le plus vendu (en quantité)
5. Compare le CA de janvier vs février

### Exercice 8 — 🔴 Difficile — Analyse complète RH
Tu es data analyst dans une entreprise. Voici le DataFrame des employés :
```python
data = {
    "nom":         ["Dupont","Durand","Moreau","Garcia","Petit",
                    "Roux","Fournier","Garnier","Mercier","Lemoine"],
    "departement": ["IT","RH","Finance","Marketing","IT",
                    "RH","Finance","Marketing","IT","RH"],
    "sexe":        ["F","F","M","F","M","M","F","M","M","F"],
    "age":         [30, 28, 35, 32, 40, 26, 29, 31, 45, 27],
    "salaire":     [3000,2800,3200,3100,4000,2600,2900,3050,4500,2700],
    "annees_exp":  [5, 3, 8, 6, 12, 2, 4, 7, 15, 3],
}
```
Produis un rapport complet :
1. Salaire moyen, min et max par département
2. Répartition hommes/femmes par département
3. Ajoute une colonne `categorie_age` : `"Junior"` (< 30), `"Senior"` (30-40), `"Expert"` (> 40)
4. Ajoute une colonne `prime` : 10% du salaire si `annees_exp` > 5, sinon 5%
5. Affiche les employés éligibles à une promotion (annees_exp > 7 ET salaire < 4000)
6. Exporte le DataFrame final en CSV et en Excel

Le but de lab est principalement d'aller à la découverte de l'utilisation de la lib pandas.