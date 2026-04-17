import pandas as pd

# users = [
#     {"name": "Paul", "age": 20, "salary": 200},
#     {"name": "Marie", "age": 25, "salary": 300},
#     {"name": "Jean", "age": 30, "salary": 400},
# ]

# # Effectuer regroupement des valeurs par clés

# data = {
#     'name'   : [e['name'] for e in users],
#     'age'    : [e['age'] for e in users],
#     'salary' : [e['salary'] for e in users]
# }

# print(data)

# dtf  = pd.DataFrame(users)

# print(dtf)

# print(dtf['age'])

# print(dtf[dtf['age'] >= 30])

# print(dtf.describe())

# dtf['sexe'] = ['M', 'F', 'M']
# print(dtf)
# print(dtf[['age', 'name']])

# dtf.set_index('name', inplace=True)
# print(dtf.loc['Paul'])
# # print(dtf.iloc[2])


users = [
    {"name": "Paul", "age": 20, "salary": 200, "dept": "IT"},
    {"name": "Marie", "age": 25, "salary": 300, "dept": "HR"},
    {"name": "Jean", "age": 30, "salary": 400, "dept": "IT"},
    {"name": "Anna", "age": 28, "salary": 350, "dept": "HR"},
]

df = pd.DataFrame(users)

mean_salary = df.groupby('dept')['salary'].mean()
print(mean_salary)

df.groupby("dept").agg({
    "salary": ["mean", "sum"],
    "age": "max"
})