# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_bar.py
# test data is pre-selected for numeric values
data = DataFrame([[1, "a"], [2, "b"]])
result = data.style.bar()._compute().ctx
assert (0, 1) not in result
assert (1, 1) not in result
