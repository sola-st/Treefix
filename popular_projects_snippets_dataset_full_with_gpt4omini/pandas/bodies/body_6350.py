# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# https://github.com/pandas-dev/pandas/issues/32276
c1 = Categorical.from_codes([-1, 0], categories=categories)
c2 = Categorical.from_codes([0, 1], categories=categories)

result = c1 != c2

assert result.all()
