# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
a = data[:3]
b = data[2:5]
r1, r2 = pd.Series(a).align(pd.Series(b, index=[1, 2, 3]))

# Assumes that the ctor can take a list of scalars of the type
e1 = pd.Series(data._from_sequence(list(a) + [na_value], dtype=data.dtype))
e2 = pd.Series(data._from_sequence([na_value] + list(b), dtype=data.dtype))
self.assert_series_equal(r1, e1)
self.assert_series_equal(r2, e2)
