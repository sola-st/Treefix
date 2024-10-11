# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_count.py

ser = Series(
    Categorical(
        [np.nan, 1, 2, np.nan], categories=[5, 4, 3, 2, 1], ordered=True
    )
)
result = ser.count()
assert result == 2
