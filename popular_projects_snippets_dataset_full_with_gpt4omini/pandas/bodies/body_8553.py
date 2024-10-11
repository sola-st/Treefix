# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/35843
values = [
    Timestamp("2012-05-01T01:00:00.000000"),
    Timestamp("2016-05-01T01:00:00.000000"),
]
arr = pd.arrays.SparseArray(values)
result = Index(arr)
assert type(result) is Index
assert result.dtype == arr.dtype
