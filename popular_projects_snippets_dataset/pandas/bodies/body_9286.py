# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# GH#31499 Hashtable.map_locations needs to work on np.str_ objects
cat = Categorical(["1", "0", "1"], [np.str_("0"), np.str_("1")])
assert all(isinstance(x, np.str_) for x in cat.categories)
