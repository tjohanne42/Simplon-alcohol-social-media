import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

def print_plt_pie(df, title=""):
    values = np.array(df)
    labels = df.index.unique()
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = [0, ] * len(values)
    explode[random.randint(0, len(values) - 1)] = 0.1
    plt.pie(values, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    if title != "":
        plt.title(title)

df_math = pd.read_csv('student-mat.csv')
df_por = pd.read_csv('student-por.csv')
df_math['math'] = True
df_por['math'] = False
df_join = df_math.append(df_por, ignore_index=True)
df_join.loc[df_join['internet'] == 'no','internet'] = False
df_join.loc[df_join['internet'] == 'yes','internet'] = True
df_join["age"]= df_join["age"].astype(str) 
df_join.loc[df_join['age'] > '19', 'age'] = "20+"
df_join['Talc'] = df_join.Dalc + df_join.Walc
df_join['G'] = (df_join['G1'] + df_join['G2'] + df_join['G3']) / 3
print(df_join)
print(df_math.shape, df_por.shape, df_join.shape)
print(df_join.info())


# COMPARER LES DF
per = pd.DataFrame()
name = 'failures'
per[name + ' % math'] = df_math[name].value_counts() / df_math[name].value_counts().sum()
per[name + ' % por'] = df_por[name].value_counts() / df_por[name].value_counts().sum()
per[name + ' % join'] = df_join[name].value_counts() / df_join[name].value_counts().sum()
print(per)

"""
df = df_join['school'].value_counts() / df_join['school'].value_counts().sum()
print_plt_pie(df, "Repartition des ecoles")

df = df_join['internet'].value_counts() / df_join['internet'].value_counts().sum()
print_plt_pie(df, "Repartition d'internet")

df = df_join[(df_join.school == 'GP')]['internet'].value_counts() / df_join[(df_join.school == 'GP')]['internet'].value_counts().sum()
print_plt_pie(df, "Repartition d'internet dans l'ecole GP")

df = df_join[(df_join.school == 'MS')]['internet'].value_counts() / df_join[(df_join.school == 'MS')]['internet'].value_counts().sum()
print_plt_pie(df, "Repartition d'internet dans l'ecole MS")

df = df_join[(df_join.math == True)]['internet'].value_counts() / df_join[(df_join.math == True)]['internet'].value_counts().sum()
print_plt_pie(df, "Repartition d'internet etudiants math")

df = df_join[(df_join.math == False)]['internet'].value_counts() / df_join[(df_join.math == False)]['internet'].value_counts().sum()
print_plt_pie(df, "Repartition d'internet etudiants por")

df = df_join[(df_join.math == False)]['school'].value_counts() / df_join[(df_join.math == False)]['school'].value_counts().sum()
print_plt_pie(df, "Repartition d'ecole etudiants por")

df = df_join[(df_join.math == True)]['school'].value_counts() / df_join[(df_join.math == True)]['school'].value_counts().sum()
print_plt_pie(df, "Repartition d'ecole etudiants math")

df = df_join[(df_join.school == 'GP')]['address'].value_counts() / df_join[(df_join.school == 'GP')]['address'].value_counts().sum()
print_plt_pie(df, "Repartition d'address etudiants GP")

df = df_join[(df_join.school == 'MS')]['address'].value_counts() / df_join[(df_join.school == 'MS')]['address'].value_counts().sum()
print_plt_pie(df, "Repartition d'address etudiants MS")

df = df_join[(df_join.math == True)]['address'].value_counts() / df_join[(df_join.math == True)]['address'].value_counts().sum()
print_plt_pie(df, "Repartition d'address etudiants math")

df = df_join[(df_join.math == False)]['address'].value_counts() / df_join[(df_join.math == False)]['address'].value_counts().sum()
print_plt_pie(df, "Repartition d'address etudiants por")
"""
"""
	On peut voir que l'ecole MS est une ecole plus rurale (52.9% des etudiants habitent en R (rural))
	MS: 52.9% R (rural)
	GP: 18.3% R (rural)
"""

"""
df = df_join[(df_join.address == 'U')]['Dalc'].value_counts() / df_join[(df_join.address == 'U')]['Dalc'].value_counts().sum()
print_plt_pie(df, "Repartition Dalc pour habitants U")

df = df_join[(df_join.address == 'R')]['Dalc'].value_counts() / df_join[(df_join.address == 'R')]['Dalc'].value_counts().sum()
print_plt_pie(df, "Repartition Dalc pour habitants R")
"""
"""
	Consommation + importante zone rurale
"""
"""
plt.figure()
plt.subplot(2, 1, 1)
df = df_join[(df_join.Dalc >= 3)]['famrel'].value_counts() / df_join[(df_join.Dalc >= 3)]['famrel'].value_counts().sum()
print_plt_pie(df, "Relation famrel pour gros consommateurs")

plt.subplot(2, 1, 2)
df = df_join[(df_join.Dalc < 3)]['famrel'].value_counts() / df_join[(df_join.Dalc >= 3)]['famrel'].value_counts().sum()
print_plt_pie(df, "Relation famrel pour petits consommateurs")
plt.show()

tab = []
i = 1
while i <= 5:
	tab.append(df_join[df_join.famrel == i].Talc.sum() / df_join[df_join.famrel == i].Talc.count())
	i += 1
print(tab)

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5], tab)
ax.set(xlabel='famrel (1 bad 5 good)', ylabel='Talc (1 low - 10 high)', title='Consommation par rapport a la relation familiale')
ax.grid()
plt.show()

fig, ax = plt.subplots()
tab = []
tab.append(df_join[df_join.Pstatus == 'T'].Talc.sum() / df_join[df_join.Pstatus == 'T'].Talc.count())
tab.append(df_join[df_join.Pstatus == 'A'].Talc.sum() / df_join[df_join.Pstatus == 'A'].Talc.count())
ax.plot(['Living Together', 'Living Apart'], tab)
ax.set(xlabel="Parent's cohabitation", ylabel='Talc (1 low - 10 high)', title='Consommation par rapport au statut familial')
ax.grid()
plt.show()

fig, ax = plt.subplots()
tab = []
tab.append(df_join[df_join.famsize == 'LE3'].Talc.sum() / df_join[df_join.famsize == 'LE3'].Talc.count())
tab.append(df_join[df_join.famsize == 'GT3'].Talc.sum() / df_join[df_join.famsize == 'GT3'].Talc.count())
ax.plot(['less or equal to 3', 'greater than 3'], tab)
ax.set(xlabel="Family size", ylabel='Talc (1 low - 10 high)', title='Consommation par rapport a la taille de la famille')
ax.grid()
plt.show()

fig, ax = plt.subplots()
tab = []
tab2 = []
i = 0
while i <= df_join.absences.max():
	if df_join[df_join.absences == i].Talc.count() > 0:
		tab.append(df_join[df_join.absences == i].Talc.sum() / df_join[df_join.absences == i].Talc.count())
		tab2.append(i)
	i += 1
ax.plot(tab2, tab)
ax.set(xlabel="absences", ylabel='Talc (1 low - 10 high)', title='Consommation par rapport aux absences')
ax.grid()
plt.show()


fig, ax = plt.subplots()
tab = []
tab.append(df_join[df_join.activities == 'yes'].Talc.sum() / df_join[df_join.activities == 'yes'].Talc.count())
tab.append(df_join[df_join.activities == 'no'].Talc.sum() / df_join[df_join.activities == 'no'].Talc.count())
ax.plot(['no extra-curricular activities', 'extra-curricular activities'], tab)
ax.set(xlabel="extra-curricular activities", ylabel='Talc (1 low - 10 high)', title='Consommation par rapport aux activites extra scolaires')
ax.grid()
plt.show()
"""
print('min', df_join.failures.min())
print('max', df_join.failures.max())
fig, ax = plt.subplots()
tab = []
i = 1
while i <= 10:
	if df_join[df_join.Talc == i].failures.count() > 0:
		tab.append(df_join[df_join.Talc == i].failures.sum() / df_join[df_join.Talc == i].failures.count())
	i += 1
ax.plot(range(1, 10), tab)
ax.set(xlabel='Talc (1 low - 10 high)', ylabel='failures', title='Consommation par rapport aux failures')
ax.grid()
plt.show()


fig, ax = plt.subplots()
tab = []
i = 0
while i <= 4:
	tab.append(df_join[df_join.traveltime == i].Talc.sum() / df_join[df_join.traveltime == i].Talc.count())
	i += 1
ax.plot(range(0, 5), tab)
ax.set(xlabel='traveltime', ylabel='Talc (1 low - 10 high)', title='Consommation par rapport aux temps de trajet')
ax.grid()
plt.show()
"""

"""
