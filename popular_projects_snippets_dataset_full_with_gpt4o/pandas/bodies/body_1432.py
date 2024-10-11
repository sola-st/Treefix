# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 32431
df = Series([1, "{1,2}", 1, nulls_fixture])
vc = df.value_counts(dropna=False)
result1 = vc.loc[nulls_fixture]
result2 = vc[nulls_fixture]

expected = 1
assert result1 == expected
assert result2 == expected
