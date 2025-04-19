import pandas as pd
import numpy as np

class NaiveBayesClassifier:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.priors = {}
        self.likelihoods = {}

        for cls in self.classes:
            X_c = X[y == cls]
            self.priors[cls] = len(X_c) / len(X)
            self.likelihoods[cls] = {}
            for col in X.columns:
                self.likelihoods[cls][col] = {}
                for val in X[col].unique():
                    self.likelihoods[cls][col][val] = (
                        (X_c[col] == val).sum() + 1) / (len(X_c) + len(X[col].unique()))

    def predict(self, X):
        results = []
        for _, row in X.iterrows():
            probs = {}
            for cls in self.classes:
                prob = self.priors[cls]
                for col in X.columns:
                    val = row[col]
                    prob *= self.likelihoods[cls][col].get(val, 1e-6)
                probs[cls] = prob
            results.append(max(probs, key=probs.get))
        return results

# Sample dataset: [Outlook, Temp, Humidity, Wind, PlayTennis]
data = pd.DataFrame([
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
], columns=['Outlook', 'Temp', 'Humidity', 'Wind', 'PlayTennis'])

X = data.drop('PlayTennis', axis=1)
y = data['PlayTennis']

# Train
model = NaiveBayesClassifier()
model.fit(X, y)

# Predict
test = pd.DataFrame([['Sunny', 'Cool', 'High', 'Strong']], columns=X.columns)
prediction = model.predict(test)

print("Prediction for test input:", prediction[0])
