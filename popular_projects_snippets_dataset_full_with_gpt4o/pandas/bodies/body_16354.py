# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
for n in [777, 777.0, "name", datetime(2001, 11, 11), (1,), "\u05D0"]:
    for data in [[1, 2, 3], np.ones(3), {"a": 0, "b": 1}]:
        s = Series(data, name=n)
        assert s.name == n
