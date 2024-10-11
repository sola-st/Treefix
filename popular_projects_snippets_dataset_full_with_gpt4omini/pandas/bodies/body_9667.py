# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_reductions.py
arr = period_array(
    [
        "2000-01-03",
        "2000-01-03",
        "NaT",
        "2000-01-02",
        "2000-01-05",
        "2000-01-04",
    ],
    freq="D",
)

result = arr.min()
expected = pd.Period("2000-01-02", freq="D")
assert result == expected

result = arr.max()
expected = pd.Period("2000-01-05", freq="D")
assert result == expected

result = arr.min(skipna=False)
assert result is pd.NaT

result = arr.max(skipna=False)
assert result is pd.NaT
