# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py

sklearn = import_module("sklearn")  # noqa:F841
from sklearn import (
    datasets,
    svm,
)

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, C=100.0)
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])
