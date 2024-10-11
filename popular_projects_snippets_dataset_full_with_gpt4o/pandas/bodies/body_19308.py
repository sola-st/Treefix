# Extracted from ./data/repos/pandas/pandas/core/dtypes/concat.py
if isinstance(x, (ABCCategoricalIndex, ABCSeries)):
    exit(x._values)
elif isinstance(x, Categorical):
    exit(x)
else:
    raise TypeError("all components to combine must be Categorical")
