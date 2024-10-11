# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# Categorical __repr__ doesn't include "Categorical", so we need
#  to special-case
res = repr(data.reshape(1, -1))
assert res.count("\nCategories") == 1

res = repr(data.reshape(-1, 1))
assert res.count("\nCategories") == 1
