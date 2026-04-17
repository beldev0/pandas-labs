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

dtf = pd.DataFrame(data)

dtf['total'] = dtf['prix'] * dtf['quantite']

print(dtf)

ca_total = dtf["total"].sum()
print(f"CA TOTAL  = {ca_total}")

ca_by_category = dtf.groupby('categorie')['total'].sum()
print(f'CA BY CATEGORY : {ca_by_category}')

most_sold = dtf.groupby('produit')['total'].sum().sort_values(ascending=False).head(1)
print(most_sold)

ca_cmp = dtf.groupby('mois')['total'].sum()
print(ca_cmp)
if ca_cmp['Jan'] > ca_cmp['Fev'] :
    print("CA Jan > CA Fev")
elif ca_cmp['Jan'] < ca_cmp['Fev']  :
    print("CA Fev > CA Fev")
else :
    print("CA égaux")
