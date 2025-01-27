# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# we dont cast date objects to timestamps, matching Index constructor
v = date.today()

cat = Categorical([v, v])
assert cat.categories.dtype == object
assert type(cat.categories[0]) is date
