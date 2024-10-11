# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py

# test the string repr
idx = simple_index
idx.name = "foo"
assert f"length={len(idx)}" not in str(idx)
assert "'foo'" in str(idx)
assert type(idx).__name__ in str(idx)

if hasattr(idx, "tz"):
    if idx.tz is not None:
        assert idx.tz in str(idx)
if isinstance(idx, pd.PeriodIndex):
    assert f"dtype='period[{idx.freqstr}]'" in str(idx)
else:
    assert f"freq='{idx.freqstr}'" in str(idx)
