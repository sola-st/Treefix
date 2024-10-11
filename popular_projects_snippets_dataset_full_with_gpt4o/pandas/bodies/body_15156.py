# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# https://docs.python.org/3/reference/datamodel.html#object.__repr__
# ...The return value must be a string object.

# (str on py2.x, str (unicode) on py3)

data = [8, 5, 3, 5]
index1 = ["\u03c3", "\u03c4", "\u03c5", "\u03c6"]
df = Series(data, index=index1)
assert type(df.__repr__() == str)  # both py2 / 3
