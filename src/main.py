from sklearn import svm
from sklearn import datasets

import mlflow

mlflow.sklearn.autolog()

iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train the model
clf = svm.SVC(gamma='scale')
clf.fit(X, y)
