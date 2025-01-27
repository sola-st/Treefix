# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
categories = np.arange(10).view("M8[D]")
values = categories[::2].copy()

cat = Categorical(values, categories=categories)
assert (cat == values).all()
