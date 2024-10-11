# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
data = {"a": 0, "b": 1, "c": 2, "d": 3}

series = Series(data)
tm.assert_is_sorted(series.index)

data = {"a": 0, "b": "1", "c": "2", "d": datetime.now()}
series = Series(data)
assert series.dtype == np.object_

data = {"a": 0, "b": "1", "c": "2", "d": "3"}
series = Series(data)
assert series.dtype == np.object_

data = {"a": "0", "b": "1"}
series = Series(data, dtype=float)
assert series.dtype == np.float64
