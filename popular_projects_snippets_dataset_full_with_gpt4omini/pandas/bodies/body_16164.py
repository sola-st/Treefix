# Extracted from ./data/repos/pandas/pandas/tests/series/test_iteration.py
for idx, val in string_series.items():
    assert val == string_series[idx]

# assert is lazy (generators don't define reverse, lists do)
assert not hasattr(string_series.items(), "reverse")
