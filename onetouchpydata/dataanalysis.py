import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age': [25, 32, 45, 20, 38, 55, 18, 39, 48, 27, 35, 40, 16, 29, 59],
    'Speed': [4, 3, 1, 4, 3, 2, 2, 3, 5, 2, 3, 2, 4, 3, 1],
    'Design': [5, 4, 2, 5, 4, 2, 2, 4, 3, 3, 4, 2, 5, 4, 1],
    'Duration': [3, 2, 2, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 1],
    'Controls': [2, 1, 2, 2, 1, 3, 1, 1, 3, 2, 1, 3, 2, 1, 1],
    'Difficulty': [4, 3, 1, 4, 3, 2, 1, 3, 2, 2, 3, 2, 4, 3, 1]
}

df = pd.DataFrame(data)

df.plot(x='Age', y=['Speed', 'Design', 'Duration', 'Controls', 'Difficulty'], kind='barh')

plt.xlabel('Scores')
plt.ylabel('Age')
plt.title('Survey Results')
plt.legend(loc='best')

plt.show()
