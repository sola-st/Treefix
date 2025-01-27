# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py

# related GH#9217, make sure limit is an int and greater than 0
ser = Series([1, 2, 3, None])
msg = "|".join(
    [
        r"Cannot specify both 'value' and 'method'\.",
        "Limit must be greater than 0",
        "Limit must be an integer",
    ]
)
for limit in [-1, 0, 1.0, 2.0]:
    for method in ["backfill", "bfill", "pad", "ffill", None]:
        with pytest.raises(ValueError, match=msg):
            ser.fillna(1, limit=limit, method=method)
