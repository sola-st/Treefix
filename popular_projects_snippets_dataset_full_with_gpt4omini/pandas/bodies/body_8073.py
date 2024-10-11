# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# 2845
vals = list(vals)  # Copy for each iteration
vals.append(nulls_fixture)
index = Index(vals, dtype=object)
# TODO: case with complex dtype?

formatted = index.format()
null_repr = "NaN" if isinstance(nulls_fixture, float) else str(nulls_fixture)
expected = [str(index[0]), str(index[1]), str(index[2]), null_repr]

assert formatted == expected
assert index[3] is nulls_fixture
