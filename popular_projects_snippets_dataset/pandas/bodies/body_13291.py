# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
pytype = frame.dtypes[0].type
row = frame.iloc[0]
assert issubclass(pytype, np.floating)
tm.equalContents(row.values, [5.1, 3.5, 1.4, 0.2, "Iris-setosa"])
