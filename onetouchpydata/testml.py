import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from joblib import load

new_age = int(input("Enter the age: "))

new_data = pd.DataFrame({
    'Age': [new_age],
    'Speed': [4],
    'Design': [5],
    'Duration': [3],
    'Controls': [2],
    'Difficulty': [4]
})

model = load('onetouchml.joblib')

prediction = model.predict(new_data)

print(f"Prediction for age {new_age}: {prediction[0]}")