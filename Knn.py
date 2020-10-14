from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
data = iris.data
target = iris.target

model = KNeighborsClassifier(n_neighbors=10)
model = model.fit(data, target)
pred = model.predict(data)
acc = accuracy_score(target, pred)

file = open("acc.txt", "w")
file.write(str(acc))
file.close()
