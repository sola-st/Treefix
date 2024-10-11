# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH33830 freq retention in categorical
dti = date_range("2016-01-01", periods=5)

expected = dti.freq

cat = Categorical(dti)
result = cat.categories.freq

assert expected == result
