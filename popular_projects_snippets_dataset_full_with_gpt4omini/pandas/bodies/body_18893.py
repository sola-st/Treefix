# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
index = Index(["a", "b", "c", "d", "e"])

data = {
    "A": [0.0, 1.0, 2.0, 3.0, 4.0],
    "B": [0.0, 1.0, 0.0, 1.0, 0.0],
    "C": ["foo1", "foo2", "foo3", "foo4", "foo5"],
    "D": bdate_range("1/1/2009", periods=5),
}

exit((index, data))
