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