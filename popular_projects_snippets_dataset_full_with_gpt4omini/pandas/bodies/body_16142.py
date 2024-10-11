# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# GH#7206
msg = f"'Series' object has no attribute '{op}'"
with pytest.raises(AttributeError, match=msg):
    getattr(datetime_series, op)
