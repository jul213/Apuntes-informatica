import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Cargar
train = pd.read_csv('/kaggle/input/titanic/train.csv')
test = pd.read_csv('/kaggle/input/titanic/test.csv')

# Unir para procesar ambos a la vez
full_data = [train, test]

# 1. Procesar Sexo
for dataset in full_data:
    dataset['Sex'] = dataset['Sex'].map({'female': 1, 'male': 0}).astype(int)

# 2. Rellenar Edad (Mediana por clase y sexo)
for dataset in full_data:
    dataset['Age'] = dataset.groupby(['Pclass', 'Sex'])['Age'].transform(lambda x: x.fillna(x.median()))

# 3. Crear Variable Familia
for dataset in full_data:
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1, 'IsAlone'] = 1

# 4. Limpiar variables que no usaremos
features = ['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'IsAlone']
# Rellenamos el Fare que falta en Test
test['Fare'] = test['Fare'].fillna(test['Fare'].median())

X_train = train[features]
y_train = train['Survived']
X_test = test[features]

# 5. Entrenar Modelo
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X_train, y_train)

# 6. Generar archivo para subir
predictions = model.predict(X_test)
output = pd.DataFrame({'PassengerId': test.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)

print("¡Listo! Sube el archivo 'submission.csv' a Kaggle.")