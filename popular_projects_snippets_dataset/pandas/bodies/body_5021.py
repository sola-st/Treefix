# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_na_scalar.py
# GH 30013
result = {NA: "foo", hash(NA): "bar"}

assert result[NA] == "foo"
assert result[hash(NA)] == "bar"
