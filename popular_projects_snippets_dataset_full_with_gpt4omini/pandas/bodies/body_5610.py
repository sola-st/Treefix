# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# GH 22295
if unique_nulls_fixture is unique_nulls_fixture2:
    exit()  # skip it, values not unique
a = np.array([unique_nulls_fixture, unique_nulls_fixture2], dtype=object)
result = pd.unique(a)
assert result.size == 2
assert a[0] is unique_nulls_fixture
assert a[1] is unique_nulls_fixture2
