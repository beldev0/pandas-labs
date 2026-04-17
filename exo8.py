import pandas as pd

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

# 1. Salaire moyen, min et max par département

rapport = {}

dtf = pd.DataFrame(data)

print(dtf.groupby('departement')['salaire'].agg(['mean', 'sum', 'max']))

rapport['salaire'] = dtf.groupby('departement')['salaire'].agg(['mean', 'sum', 'max'])

# Répartition hommes/femmes par département

print(dtf.groupby(by=['departement', 'sexe']).size())

# Ajoute une colonne `categorie_age` : `"Junior"` (< 30), `"Senior"` (30-40), `"Expert"` (> 40)

rapport['categorie_age'] = dtf['age'].apply(lambda age: "Junior" if age < 30 else "Senior" if age <40 else "Expert")
print(dtf)

# dtf['categorie_age'] = "Junior" if dtf['age'] < 30 else if (dtf['age'] < 40 or dtf['age'] >=30 )

# Ajoute une colonne `prime` : 10% du salaire si `annees_exp` > 5, sinon 5%

# Affiche les employés éligibles à une promotion (annees_exp > 7 ET salaire < 4000)

rapport['promotion'] = (dtf[(dtf['annees_exp'] > 7) & (dtf['salaire'] < 4000)])

rapport.to_csv('rap.csv', index=False)
