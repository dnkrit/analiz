import pandas as pd

data = {
    'Ученик': ['Ученик 1', 'Ученик 2', 'Ученик 3', 'Ученик 4', 'Ученик 5',
               'Ученик 6', 'Ученик 7', 'Ученик 8', 'Ученик 9', 'Ученик 10'],
    'Математика': [85, 78, 92, 88, 76, 95, 89, 84, 79, 91],
    'Физика': [89, 75, 94, 82, 77, 90, 85, 87, 78, 88],
    'Химия': [78, 81, 85, 80, 79, 88, 82, 86, 76, 90],
    'Литература': [92, 85, 87, 90, 84, 89, 91, 88, 82, 86],
    'История': [88, 82, 90, 86, 80, 87, 85, 89, 83, 84]
}

df = pd.DataFrame(data)

print("Первые строки DataFrame:")
print(df.head())

mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 для математики: {Q1_math}")
print(f"Q3 для математики: {Q3_math}")

IQR_math = Q3_math - Q1_math
print(f"IQR для математики: {IQR_math}")

std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)