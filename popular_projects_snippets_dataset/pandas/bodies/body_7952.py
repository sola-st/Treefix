# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# Index(periods, dtype=object) is an Index (not an PeriodIndex)
periods = [
    Period("2011-01", freq="M"),
    NaT,
    Period("2011-03", freq="M"),
]
values = values_constructor(periods)
result = Index(values, dtype=object)

assert type(result) is Index
tm.assert_numpy_array_equal(result.values, np.array(values))
