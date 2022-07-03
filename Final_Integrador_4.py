import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

titanic = pd.read_csv('https://raw.githubusercontent.com/NotAyushXD/Titanic-dataset/master/train.csv', sep=',')
titanic.head(5)
titanic.info()
titanic.tail(5)


total_p1 = titanic.loc[titanic['Pclass'] == 1, 'Pclass'].sum()
print(f"En primera clase viajan un total de:{total_p1}")

titanic['Pclass'].value_counts().plot(kind='bar')