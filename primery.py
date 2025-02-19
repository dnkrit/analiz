import pandas as pd

data = {
    'набор А': [85, 90, 95, 100, 105],
    'набор Б': [70, 80, 90, 100, 110],
}

df = pd.DataFrame(data)
stdA = df['набор А'].std()
stdB = df['набор Б'].std()

print(f"стандартное отклонение 1 набор - {stdA}")
print(f"стандартное отклонение 1 набор - {stdB}")



import pandas as pd

data = {
    'Возраст': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    'Зарплата': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000],
}

df = pd.DataFrame(data)

print(f"Средний возраст - {df['Возраст'].mean()}")
print(f"Медианный возраст - {df['Возраст'].median()}")
print(f"Стандартное отклонение возраста - {df['Возраст'].std()}")

print(f"Средняя зарплата - {df['Зарплата'].mean()}")
print(f"Медианная зарплата - {df['Зарплата'].median()}")
print(f"Стандартное отклонение по зарплате - {df['Зарплата'].std()}")



import pandas as pd
import numpy as np

dates = pd.date_range(start='2022-07-26', periods=10, freq='D')

values = np.random.rand(10)

df = pd.DataFrame({'Date': dates, 'Value':values})

df.set_index('Date', inplace=True)

print(df)



import pandas as pd
import matplotlib.pyplot as plt

data = {'value': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)

df['value'].hist()
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

data = {'value': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)

df.boxplot(column='value')
plt.show()

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]

df_new.boxplot(column='value')
plt.show()



import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)

df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

df['department'] = df['department'].cat.add_categories(['Finansist'])
print(df['department'].cat.categories)

df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)

print(df)