import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from joblib import dump

data = {
'Age': [25, 32, 45, 20, 38, 55, 18, 39, 48, 27, 35, 40, 16, 29, 59],
    'Speed': [4, 3, 1, 4, 3, 2, 2, 3, 5, 2, 3, 2, 4, 3, 1],
    'Design': [5, 4, 2, 5, 4, 2, 2, 4, 3, 3, 4, 2, 5, 4, 1],
    'Duration': [3, 2, 2, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 1],
    'Controls': [2, 1, 2, 2, 1, 3, 1, 1, 3, 2, 1, 3, 2, 1, 1],
    'Difficulty': [4, 3, 1, 4, 3, 2, 1, 3, 2, 2, 3, 2, 4, 3, 1],
    'Opinion': ['Like', 'Like', 'Dislike', 'Like', 'Like', 'Dislike', 'Like', 'Like', 'Dislike', 'Like', 'Like', 'Dislike', 'Like', 'Like', 'Dislike']
}

df = pd.DataFrame(data)

X = df.drop('Opinion', axis=1)
y = df['Opinion']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred))

dump(clf, 'onetouchml.joblib')
